## 7.8 Using SS Error to Compare the Group Model to the Empty Model

To calculate the sum of squares error for each model, we don't have to add a new column to the data frame. We can, instead, just generate the residuals from each model, then square them and sum them.

In the code window below we have entered code to calculate the SS Total for the empty model. Add some code to calculate SS Error for the `Gender` model. (We already have created and saved the two models: `empty_model` and `Gender_model`.)

```{ data-ckcode=true #B3_Code_UsingSS_01 }
%%% setup
require(coursekata)

%%% prompt
# This codes saves the best fitting models
empty_model <- lm(Thumb ~ NULL, data=Fingers)
Gender_model <- lm(Thumb ~ Gender, data=Fingers)

# This code squares and sums the residuals from the empty model
sum(resid(empty_model)^2)

# Write code to square and sum the residuals from the Gender model

%%% solution
# This codes saves the best fitting models
empty_model <- lm(Thumb ~ NULL, data=Fingers)
Gender_model <- lm(Thumb ~ Gender, data=Fingers)

# This code squares and sums the residuals from the empty model
sum(resid(empty_model)^2)

# Write code to square and sum the residuals from the Gender model
sum(resid(Gender_model)^2)

%%% test
ex() %>% {
  check_function(., "sum", 1) %>%
    check_result() %>% check_equal()
  check_function(., "sum", 2) %>%
    check_result() %>% check_equal()
}
```

```
11880.2109191083
```

```
10546.0083744196
```

We can see from this output that we have, indeed, reduced our error by adding `Gender` as an explanatory variable into the model. Whereas the sum of squared errors around the empty model (SS Total) was 11,880, for the `Gender` model (SS Error) it was 10,546. We now have a quantitative basis on which to say that the `Gender` model is a better model *of our data* than the empty model.

This idea is visualized in the figure below.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_08_UsingSS_1.jpg" width=80%  alt="On the left, a single circle represents SS Total from the Empty Model of Thumb. An arrow from that circle points to a Venn diagram of two partially overlapping circles to the right. One circle is labeled as SS Error from the Gender Model of Thumb, and the other circle is labeled as Gender. The intersection where the two circles overlap is labeled as Error Reduced by Gender." /></p>

::: { .qti-item #b3_UsingSS_01 }
:::::: { #f26f7e3f-a38d-4b93-8dfa-7d9075c3aa00 .qti-question .multiple-choice points="1" }

What does the whole teal circle (on left) represent?

::::::::: { .choices }

- The parameter estimates of the empty model
- [SS Total, how much error there is in `Thumb`, after using the empty model to make predictions]{ .correct }
- SS Error, how much error there is in `Thumb` after we add `Gender` to the model

:::::::::

::::::

:::::: { #c6eae28d-c8a5-4d83-ad0c-a42babee276e .qti-question .multiple-choice points="1" }

What does the teal crescent shape (on right) represent?

::::::::: { .choices }

- The parameter estimates of the `Gender` model
- SS Total, how much error there is in `Thumb`, after using the empty model to make predictions
- [SS Error, how much error there is in `Thumb` after we add `Gender` to the model]{ .correct }

:::::::::

::::::
:::

### Using `supernova()` to Calculate SS Error

Although we have been building these calculations from the residuals up, we now will show you an easier way to summarize the various sums of squares using ANOVA (ANalysis Of VAriance) tables.

We introduced the `supernova()` function earlier as a way of getting SS Total for the empty model. We can use the same function to calculate the SS Error (and more!) from the `Gender` model and other group models.

We have created and saved two models in the code window below: `empty_model` and  `Gender_model` . Run the code as is and you will get the ANOVA table for the `empty_model`. Modify the `supernova()` code to get the ANOVA table for the `Gender_model`.

```{ data-ckcode=true #B3_Code_UsingSS_02 }
%%% setup
require(coursekata)

%%% prompt
empty_model <- lm(Thumb ~ NULL, data = Fingers)
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# try running the code as is
# then modify to create the ANOVA table for Gender_model
supernova(empty_model)

%%% solution
empty_model <- lm(Thumb ~ NULL, data = Fingers)
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# try running the code as is
# then modify to create the ANOVA table for Gender_model
supernova(Gender_model)

%%% test
ex() %>% {
    check_function(., "lm") %>% check_result() %>% check_equal()
    check_object(., "Gender_model") %>% check_equal()
    check_function(., "supernova") %>% check_result() %>%  check_equal()
}
```

<pre><code>
Analysis of Variance Table (Type III SS)
 Model: Thumb ~ Gender

                                SS  df       MS      F    PRE     p
 ----- --------------- | --------- --- -------- ------ ------ -----
 Model (error reduced) |  1334.203   1 1334.203 19.609 0.1123 .0000
 Error (from model)    | <mark>10546.008</mark> 155   68.039
 ----- --------------- | --------- --- -------- ------ ------ -----
 Total (empty model)   | <mark>11880.211</mark> 156   76.155
</code></pre>

Although there is a lot going on in this table, the highlighted numbers are the SS Error and SS Total that we previously calculated from the residuals. Notice that the ANOVA table for `Gender_model` calculates both the SS Error (labeled Error) and the SS Total (labeled Total, the error from the empty model).

::: { .qti-item #b3_UsingSS_02 }
:::::: { #a8df0063-f337-432b-a9c4-915034880bc5 .qti-question .multiple-choice points="1" }

What unit are these sums of squares measured in?

::::::::: { .choices }

- $cm$
- $mm$
- $cm^2$
- [$mm^2$]{ .correct }
- $inches$

:::::::::

::::::

:::::: { #b2668b4f-571a-4b94-9ab9-5fa2a321201c .qti-question .multiple-choice points="1" }

Why do you think the sum of squares for the empty model is greater than that for the `Gender` model? (Check all that apply.)

::::::::: { .choices }

- Because the empty model is better than the `Gender` model
- Because the empty model is larger than the `Gender` model
- [Because the `Gender` model explains more variation, which results in less leftover error]{ .correct }
- Because the empty model does not explain any variation but the `Gender` model does explain some of the variation
- Because the `Gender` model is based on smaller values (such as 1 and 2) rather than thumb length, which has larger values (such as 60)

:::::::::

::::::
:::

SS Total is the smallest SS we could have without adding an explanatory variable to the model. It represents the total variation in the outcome variable that we would want to explain. Taking that as our starting point, we can reduce the error by adding an explanatory variable into the model (in this case `Gender`).

Adding an explanatory variable to the model can decrease the sum of squares for error, but it can’t increase it. If the new model does not make better predictions than the empty model then the sum of squares would stay the same. But it’s rare for an explanatory variable to have no predictive value at all.
