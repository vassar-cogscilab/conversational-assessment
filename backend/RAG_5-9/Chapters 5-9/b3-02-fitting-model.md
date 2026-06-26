## 7.2 Using R to Fit the Group Model

Now that we know what the `Gender` model does – i.e., that it produces two different values for the predictions, one for students of each gender – let's use R to fit the model to the data and see how  the model makes these predictions.

::: { .qti-item #b3_RtoFit_01 }
:::::: { #ae1aae97-4e92-4a71-b35e-75105e0e4284 .qti-question .multiple-choice points="1" }

Let's see if you can figure out how to fit the `Gender` model of `Thumb`. To find the best-fitting empty model (the mean), we wrote:

`lm(Thumb ~ NULL, data = Fingers)`

Which of these lines of code do you think we would use to fit the `Gender` model?

::::::::: { .choices }

- `lm(Gender ~ NULL, data = Fingers)`
- `lm(Thumb ~ Thumb, data = Fingers)`
- [`lm(Thumb ~ Gender, data = Fingers)`]{ .correct }
- `lm(Fingers ~ Thumb, data = Gender)`

:::::::::

::::::
:::

In the code block below, we have filled in the code to fit the `Gender` model and save it as `Gender_model`. Use the pipe operator (%>%) to overlay model predictions of the `Gender` model on the jitter plot: `gf_model(Gender_model)`.

```{ data-ckcode=true #B3_Code_RtoFit_01 }
%%% setup
require(coursekata)

%%% prompt
# find best fitting model
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# add code to visualize the new model on the jitter plot
gf_jitter(Thumb ~ Gender, data = Fingers, width = .1)

%%% solution
# find best fitting model
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# add code to visualize the new model on the jitter plot
gf_jitter(Thumb ~ Gender, data = Fingers, width = .1) %>%
  gf_model(Gender_model)

%%% test
ex() %>% {
  check_function(., "gf_model") %>%
    check_arg("object") %>%
    check_equal()
  check_or(.,
    check_function(., "gf_model") %>%
      check_arg("model") %>%
      check_equal(),
    override_solution(., "gf_jitter(Thumb ~ Gender, data = Fingers) %>% gf_model(Thumb ~ Gender)") %>%
      check_function(., "gf_model") %>%
        check_arg("model") %>%
        check_equal()
  )
}
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_02_UsingR_1.jpg" width=80%  alt="A jitter plot of the distribution of Thumb by Gender in the Fingers data frame, overlaid with a red horizontal line in each group showing the group mean." /></p>

If you want to change the color of the model (as we did for the figure above), you can add in the argument `color = "red"` to the `gf_model()` function.

### Generating Predictions from the `Gender` Model

The `Gender` model in the visualization is represented by two lines because it generates two different predictions depending on the Gender of the person. Let’s use the `predict()` function to see how this works.

```{ data-ckcode=true #B3_Code_RtoFit_02 }
%%% setup
require(coursekata)

%%% prompt
# we have saved the Gender model for you
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# write code to generate predictions using this model
# no need to save the predictions

%%% solution
# we have saved the Gender model for you
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# write code to generate predictions using this model
# no need to save the predictions
predict(Gender_model)

%%% test
ex() %>%
  check_function("predict") %>%
  check_result() %>%
  check_equal()
```

Notice that now, instead of just generating a single number (like the empty model’s 60.1), these predictions are a mix of two numbers (64.7 and 58.3). Using the code below, we have saved these predictions back into `Fingers` as a new variable called `Gender_predict` and printed out `Gender`, `Thumb`, and `Gender_predict` for 6 of the students.

```
Fingers$Gender_predict <- predict(Gender_model)
head(select(Fingers, Gender, Thumb, Gender_predict))
```

```
  Gender Thumb Gender_predict
1   male 66.00       64.70267
2 female 64.00       58.25585
3 female 56.00       58.25585
4   male 58.42       64.70267
5 female 74.00       58.25585
6 female 60.00       58.25585
```

The `Gender` model looks at the gender of each student before making its prediction. If the student is male, the model predicts the thumb length as 64.7 mm, and if female, it predicts 58.3 mm.

::: { .qti-item #b3_RtoFit_02 }
:::::: { #425ec377-26a3-4825-86b4-874cccd59946 .qti-question .multiple-choice points="1" }

What is the variable `Gender_predict`?

::::::::: { .choices }

- the prediction of the gender of the student
- [the prediction of a student's thumb length based on their gender]{ .correct }
- the difference between the gender model and the empty model's predictions

:::::::::

::::::
:::

We can run `favstats()` to confirm that these two model predictions are, in fact, the mean thumb lengths for students of each gender.

```
favstats(Thumb ~ Gender, data=Fingers)
```

<pre><code>  Gender min Q1 median     Q3   max     <mark>mean</mark>       sd   n missing
1 female  39 54     57 63.125 86.36 58.25585 8.034694 112       0
2   male  47 60     64 70.000 90.00 64.70267 8.764933  45       0</code></pre>

Yes, they are: the means of the two gender groups in the `favstats()` output are the same as the model predictions generated by the `Gender_model`.

### Interpreting the `lm()` Output  for the `Gender` Model

We have fit the `Gender` model using `lm()` and then used this model to generate predictions. However, we have not yet looked at the best-fitting parameter estimates for the model.

Recall that for the empty model we estimated one parameter ($b_0$), the mean. For the two-group `Gender` model we are going to estimate two parameters ($b_0$ and $b_1$). Based on the model predictions, we might expect these parameter estimates to be the mean for each gender. Let's find out.

In the code block below we have fit and saved the `Gender` model in the R object `Gender_model`. Add some code to print out the model so we can look at the parameter estimates.

```{ data-ckcode=true #B3_Code_RtoFit_03 }
%%% setup
require(coursekata)

%%% prompt
# we have saved the Gender model for you
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# print out the best fitting parameter estimates

%%% solution
# we have saved the Gender model for you
Gender_model <- lm(Thumb ~ Gender, data = Fingers)

# print out the best fitting parameter estimates
Gender_model

%%% test
ex() %>% check_output_expr("Gender_model")
```

```
Call:
lm(formula = Thumb ~ Gender, data = Fingers)

Coefficients:
(Intercept)   Gendermale
     58.256        6.447
```

As expected, we see two parameter estimates. But these are not the two estimates we might have expected from looking at the graph and predictions. We expected to get the two gender group means: around 58 and 65.

The estimate labeled `Intercept` in the output (58.256) seems like the mean thumb length of female students. But how should we interpret the second estimate (6.447), the one labeled `Gendermale`?

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_02_Interpreting_1.jpg" width=80%  alt="Jitter plot of Thumb predicted by Gender (female and male), with the mean of each group overlaid as a horizontal line. The line for the mean of female is labeled with the letter A, the line for the mean of male is labeled with the letter C, and the distance between the two group means is drawn with a vertical line and labeled with the letter B." /></p>

::: { .qti-item #b3_RtoFit_03 }
:::::: { #10b6bb4e-8446-477e-9bb3-7b307a57fa23 .qti-question .multiple-choice points="1" }

Where in this plot do you see the parameter estimate labeled `Intercept` (58.256)?

::::::::: { .choices }

- [A]{ .correct }
- B
- C

:::::::::

::::::

:::::: { #ed9c7dde-1127-4f36-bcc4-7d2dfeb362f8 .qti-question .multiple-choice points="1" }

Where in this plot do you see the parameter estimate labeled `Gendermale` (6.447)?

::::::::: { .choices }

- A
- [B]{ .correct }
- C

:::::::::

::::::
:::

<pre><code>
Call:
lm(formula = Thumb ~ Gender, data = Fingers)

Coefficients:
(Intercept) <mark>Gendermale</mark>
     58.256      <mark>6.447</mark>
</code></pre>

Taking a closer look at the output of the model created by using `lm()`, the label `Gendermale` for the second parameter estimate is actually useful. Although it might have been nice for R to insert some punctuation between `Gender` and `male`, it nevertheless tells us that the second estimate is the adjustment needed to get from the mean of the first group, which is referred to as `Intercept`, to the mean of the second group, `male`.

Sure enough, this works: 58.3 + 6.4 = 64.7. This  is the gender model's predicted thumb length for a male student.

### The Parameter Estimates $b_0$ and $b_1$

Whereas the empty model was a one-parameter model (producing only one estimate,  $b_0$, for the grand mean), the `Gender` model is a two-parameter model ($b_0$ and $b_1$). One of the parameters represents the mean for female students, the other is the amount that must be added to get the mean for males (as seen in the picture below).

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_02_TheParameter_1.jpg" width=80%  alt="A jitter plot of the distribution of Thumb by Gender, overlaid with a red horizontal line in each group showing the group mean. The line for the female group is labeled as b-sub-zero, the line for the male group is not labeled, and there is a vertical line in between them to indicate the distance between the two group means and it is labeled as b-sub-1." /></p>

The output of `lm()` shows us the values of $b_0$ and $b_1$ that best fit the data.

```
Call:
lm(formula = Thumb ~ Gender, data = Fingers)

Coefficients:
(Intercept)   Gendermale
     58.256        6.447
```

::::::::: { .qti-item #b3_RtoFit_04_r5.8 }
:::::: { #115e3c2d-237b-4e67-bcdb-f502ab5b84f6 .qti-question .association
points="1" }
Match the output of `lm()` with the appropriate GLM symbols ($b_0$ and $b_1$).
::: associations

- [`(Intercept)`]{match="1"}
- [`Gendermale`]{match="2"}
:::
::: choices

1. $b_0$
2. $b_1$
:::
::::::
:::::: { #5a63747c-75f1-418f-9ebe-bd4caa2f8325 .qti-question .association
points="1" }
Match the best-fitting values with the appropriate GLM symbols.
::: associations

- [58.3]{match="1"}
- [6.4]{match="2"}
:::
::: choices

1. $b_0$
2. $b_1$
:::
::::::
:::::: { #cfeeeddb-c545-4119-8d3b-fc2c92ba92b9 .qti-question .association
points="1" }
Match the GLM symbols with the meaning of these values.
::: associations

- [$b_0$]{match="1"}
- [$b_1$]{match="2"}
:::
::: choices

1. the mean thumb length of females
2. the adjustment that must be added to get the mean thumb length of males
:::
::::::
:::::::::

The $b_0$ parameter estimate represents the mean of the first group (`female`). The $b_1$ represents the quantity that must be added to $b_0$ in order to get the model prediction for the second group, which in this case is `male`.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_02_TheParameter_2.jpg" width=80%  alt="A jitter plot of the distribution of Thumb by Gender in the Fingers data frame, overlaid with a red horizontal line in each group showing the group mean. The line for the female group is labeled as b-sub-zero, the line for the male group is labeled b-sub-zero plus b-sub-1, and there is a vertical line in between them to indicate the distance between the two group means and it is labeled as b-sub-1." /></p>
