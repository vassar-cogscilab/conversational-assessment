## 8.3 Comparing the Fit of the Two- and Three-Group Models

### Examining the Fit of the Three-Group Model

You have already done the following: created the `Height3Group` categorical explanatory variable; examined the mean thumb lengths of students in each of the three groups; fit the `Height3Group` model using `lm()` and interpreted the model parameter estimates; and learned how to represent the three-group model using notation of the GLM.

The final step is to take a look at the ANOVA table so you can compare the fit of the `Height3Group` model to the empty model. Of course, you know how to do this using `supernova()`. Go ahead and get the ANOVA table for the `Height3Group` model.

```{ data-ckcode=true #B4_Extending_06 }
%%% setup
require(coursekata)

Fingers <- Fingers %>% mutate(
    Height2Group = factor(ntile(Height, 2), 1:2, c("short", "tall")),
    Height3Group = factor(ntile(Height, 3), 1:3, c("short", "medium", "tall"))
)
Height2Group_model <- lm(Thumb ~ Height2Group, data = Fingers)

%%% prompt
# creates best fitting Height3Group_model
Height3Group_model <- lm(Thumb ~ Height3Group, data = Fingers)

# use supernova() to print the ANOVA table for this model

%%% solution
# creates best fitting Height3Group_model
Height3Group_model <- lm(Thumb ~ Height3Group, data = Fingers)

# use supernova() to print the ANOVA table for this model
supernova(Height3Group_model)

%%% test
ex() %>% check_output_expr("supernova(Height3Group_model)")
```

Here’s the ANOVA table for the `Height3Group` model. Just for comparison, we pasted in the table for the `Height2Group` model right above it.

::: { .alert .alert-info }
**Height2Group Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height2Group

                               SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   830.880   1 830.880 11.656 0.0699 .0008
Error (from model)    | 11049.331 155  71.286
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11880.211 156  76.155
```

::: { .alert .alert-info }
**Height3Group Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height3Group

                               SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |  1690.440   2 845.220 12.774 0.1423 .0000
Error (from model)    | 10189.770 154  66.167
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11880.211 156  76.155
```

::: { .qti-item #Ch7_Extending_9 }
:::::: { #646936aa-1d32-4e7c-a853-1db1c00145b9 .qti-question .multiple-choice points="1" }

Look at the ANOVA table for the `Height3Group` model. What proportion of variation in thumb length is explained by this model?

::::::::: { .choices }

- [PRE (.1423)]{ .correct }
- $SS_{Model}$(1690.4)
- $SS_{Error}$(10189.8)
- $SS_{Total}$(11880.2)

:::::::::

::::::

:::::: { #bef52ea3-9a46-4323-80a1-81fba53e8a0f .qti-question .multiple-choice points="1" }

Compare the ANOVA tables for the `Height3Group` and `Height2Group` models. Why is the total SS the same for both models?

::::::::: { .choices }

- Both have the same explanatory variable.
- Both involve a categorical explanatory variable.
- Both involve a quantitative variable.
- [Both have the same outcome variable.]{ .correct }

:::::::::

::::::

:::::: { #37ead65c-a536-4751-801e-ee33bcf52c0f .qti-question .multiple-choice points="1" }

Which model is a better fit to the data?

::::::::: { .choices }

- [`Height3Group`]{ .correct }
- `Height2Group`

:::::::::

::::::

:::::: { #7786f1a7-83f0-4992-8cc3-e13229384340 .qti-question .multiple-choice points="1" scoring="partial" }

How can you tell which model is a better fit to the data? (Check all that apply.)

::::::::: { .choices }

- The better model has a larger SS total.
- [The better model has a larger PRE.]{ .correct }
- [The better model has a larger SS model.]{ .correct }
- [The better model has a small SS error (leftover error).]{ .correct }
- The better model has a smaller SS total.

:::::::::

::::::

:::::: { #abaf8733-d180-4d26-aa85-8cc70d85e203 .qti-question .multiple-choice points="1" }

Why do you think this model is better?

::::::::: { .choices }

- This model had less total variation to begin with.
- [This model produced more accurate predictions of `Thumb`, thus reducing the residuals.]{ .correct }
- This model makes a range of predictions for each person; it does not just make one prediction for each person.
- All two-group models are better than three-group models because they are simpler.
- This is just a coincidence.

:::::::::

::::::
:::

Later on or in more advanced classes you will learn how to compare these two models directly. But for now, we will only compare each model to the empty model.

### Improving Models by Adding Parameters

You probably noticed in the previous section that the three-parameter `Height3Group` model explained more variation than the `Height2Group` model; that is, it reduced the unexplained error more than the `Height2Group` model when compared with the empty model. You can see that by comparing the PREs (.14 versus .07, respectively).

If we look at histograms and jitter plots for the two-group model and the three-group model (below) you can get a sense of why this is. By adding more categories for height we are able to reduce the error variation around the mean height for each group.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/1PkFptXK.png" width=100% alt="A histogram of the distribution of Thumb by Height2Group at the upper left. A histogram of the distribution of Thumb by Height3Group at the upper right. A jitter plot of the distribution of Thumb by Height2Group at the lower left. A jitter plot of the distribution of Thumb by Height3Group at the lower right." /></p>

In general, the more parameters we add to a model the less leftover error there is after subtracting out the model. This isn't *always* the case, but typically more complex models do have higher PREs. Because the goal of the statistician is to reduce error, more complexity might seem like a good thing. And it is, but only to a point.

Let’s do a little thought experiment. You know already that the three-group model explained more variation than the two-group model. The four-group model would explain more than the three-group. And so on. What would happen if we kept splitting into more groups until each person was in their own group?

If each person were in their own group, the error would be reduced to 0. Why? Because each person would have their own parameter in the model. If each person had their own parameter, then the predicted score for that person would just be the person’s actual score. And there would be no residual between the predicted and actual score. All the variation would be explained by the model!

There are two problems with this. First, even though the model fits our data perfectly, it would not fit if we were to choose another sample (because the people would be different). Second, the purpose of creating a more complex model is to help us understand the Data Generating Process. It's okay to add a little complexity to a model *if* it leads to better understanding. But if we have as many parameters as we have people, we have added a lot of complexity without contributing to our understanding of the DGP.

**Although we can improve model fit by adding parameters to a model, there is always a trade-off involved between reducing error (by adding more parameters to a model), on one hand, and increasing the intelligibility, simplicity, and elegance of a model, on the other.**

This is a limitation of PRE as a measure of our success. If we get a PRE of .40, for example, that would be quite an accomplishment if we had only added a single parameter to the model. But if we had achieved that level by adding 10 parameters to the model, well, it’s just not as impressive. Statisticians sometimes call this "overfitting."

There is a quote attributed to Einstein that sums up things pretty well: "Everything should be made as simple as possible, but not simpler." A certain amount of complexity is required in our models just because of complexity in the world. But if we can simplify our model so as to help us make sense of complexity, and make predictions that are “good enough,” that is a good thing.

::: { .qti-item #Ch7_Extending_10 }
:::::: { #77d0a679-6262-4e04-a42c-1ccb8f29f92c .qti-question .multiple-choice points="1" }

The goal of making a statistical model isn't *just* to reduce error. We want to reduce error, sure, but what are other goals to keep in mind when building a model?

::::::::: { .choices }

- The model helps us understand something about the DGP.
- The model helps us make good enough predictions.
- The model balances simplicity and accuracy.
- [All of the above.]{ .correct }

:::::::::

::::::

:::::: { #26d0f2fe-5f9e-4f7b-9cdc-813c0669fcc3 .qti-question .multiple-choice points="1" }

What is the worst thing about PRE?

::::::::: { .choices }

- Nothing. It's the perfect statistic.
- PRE does not tell us how much error has been reduced relative to total error.
- PRE is one of many measures that tells us how much error has been reduced.
- [PRE does not tell us how much error has been reduced relative to how much complexity has been added to the model.]{ .correct }

:::::::::

::::::
:::
