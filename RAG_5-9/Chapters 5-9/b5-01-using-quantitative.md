# Chapter 9 - Models with a Quantitative Explanatory Variable

## 9.1 Using a Quantitative Explanatory Variable in a Model

`Height2Group` is a categorical variable. The `Height2Group` model is what we might call a *group model* because it uses the group mean as the best prediction of thumb lengths for each group (in this case, short and tall people).

Not all models are group models, however. If we want to use a quantitative variable as an explanatory variable we will need to adjust our model a bit. Models that use quantitative predictors are often referred to as *regression models*.

### The `Height` Model of `Thumb`

One quantitative variable in the `Fingers` data frame that might explain some of the variation in `Thumb` is `Height`: the height of a student in inches. (Note: `Height` is measured in inches but `Thumb` is measured in millimeters.)

::: { .qti-item #b5_Quantitative_01 }
:::::: { #792d5ba9-6949-421d-ab17-1ccfb13e50e2 .qti-question .multiple-choice points="1" scoring="partial" }

How might we represent the idea that height explains some of the variation in thumb lengths in a word equation? (Check all that apply.)

::::::::: { .choices }

- **DATA = Thumb + ERROR**
- [**Thumb = Height + Other Stuff**]{ .correct }
- [**Thumb = Height + Error**]{ .correct }
- **Thumb = Mean + Error**
- **Height2Group = Height + Error**

:::::::::

::::::
:::

Previously, we created a scatter plot to visualize the relationship between `Thumb` and `Height`. We've reprinted that scatter plot below.

```
gf_point(Thumb ~ Height, data = Fingers)
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/y79h4hX5.png" width=80%  alt="A scatter plot of Thumb by Height." /></p>

As we noted previously, it does appear that if we know the height of a student we can make a better guess as to their thumb length than if we didn't have this information. Taller students tend to have longer thumbs, and shorter students, shorter thumbs. We call a pattern like this a *positive relationship* because as one variable goes up, so does the other.

::: { .qti-item #b5_Quantitative_02 }
:::::: { #105e8902-cbfb-4194-b505-7da5685dce60 .qti-question .multiple-choice points="1" scoring="partial" }

In a positive relationship, variables go up and down together. Which of the following represent a positive relationship? (Check all that apply.)

::::::::: { .choices }

- [If X is high, Y is high.]{ .correct }
- [If X is low, Y is low.]{ .correct }
- If X is high, Y is low.
- If X is low, Y is high.

:::::::::

::::::
:::

If we want to make specific predictions, and quantitatively compare the `Height` model to other models, we need to turn it into a statistical model, much like we did when we developed the `Height2Group` model. This time, however, we can't use group means as the model predictions because there are no groups! Instead, we will use a line, called the *regression line*, to make predictions.

A regression line is the simplest way to model the relationship between two quantitative variables. We overlaid the best-fitting regression line (or model) on the scatter plot below. This line shows the predicted thumb length of a student based on their height.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/4sRzgLBg.png" width=80%  alt="A scatter plot of Thumb by Height overlaid with the regression line in red." /></p>

We will learn how to fit a regression model (i.e., find the best-fitting line) using R in a moment, but first it's worth pointing out that the regression line is not just any line, just like the mean is not just any number.

Just as the group means are the points at which the sum of squared residuals are minimized for a group model, the regression line is the *exact line*, defined by its slope and y-intercept, from which the residuals are balanced and the sum of squared residuals is minimized for a model with a quantitative outcome and a quantitative predictor. Let's dig into what that really means.

### Predictions from the `Height` Model

We will use the `lm()` function to fit the `Height` model in the same way we did with the group model. You don't have to tell R that this is a regression model; R will guess, just based on the fact that your explanatory variable is quantitative, not categorical.

::: { .qti-item #b5_Quantitative_03 }
:::::: { #e0526ff5-6c87-4948-ad4d-071683d9eb21 .qti-question .multiple-choice points="1" }

Here's the code for using `lm()` to fit the group model with `Height2Group` as the explanatory variable.

`lm(Thumb ~ Height2Group, data = Fingers)`

How would we modify it if we want to use `Height` instead of `Height2Group` to explain the variation in `Thumb`?

::::::::: { .choices }

- `lm(Height ~ Height2Group, data = Fingers)`
- [`lm(Thumb ~ Height, data = Fingers)`]{ .correct }
- `lm(Thumb ~ Height2Group, data = Height)`
- `lm(Height ~ Thumb, data = Fingers)`

:::::::::

::::::
:::

Use the code window below to fit the `Height` model using `lm()`, and then save it into an object called `Height_model`. Then add some code to generate the model predictions, and save them as a new column in the `Fingers` data frame. (HINT: Consider using the `predict()` function.)

```{ data-ckcode=true #B5_Code_Quantitative_01 }
%%% setup
library(coursekata)

%%% prompt
# edit the Height2Group_model code to create Height_model
Height2Group_model <- lm(Thumb ~ Height2Group, data = Fingers)

# save the predictions of the Height_model as a new variable in Fingers
Fingers$Height_predict <-

# this code prints out the first 6 observations
head(select(Fingers, Thumb, Height, Height_predict))

%%% solution
# edit the Height2Group_model code to create Height_model
Height_model <- lm(Thumb ~ Height, data = Fingers)

# save the predictions of the Height_model as a new variable in Fingers
Fingers$Height_predict <- predict(Height_model)

# this code prints out the first 6 observations for 3 columns
head(select(Fingers, Thumb, Height, Height_predict))

%%% test
ex() %>% {
  check_object(., "Height_model") %>%
    check_equal()
  check_object(., "Fingers") %>%
    check_column("Height_predict") %>%
    check_equal()
}
```

```
 Thumb Height Height_predict
1 66.00   70.5       64.48330
2 64.00   64.8       59.00056
3 56.00   64.0       58.23105
4 58.42   70.0       64.00235
5 74.00   68.0       62.07859
6 60.00   68.0       62.07859
```

::: { .qti-item #b5_Quantitative_04 }
:::::: { #32ad258e-ef40-4a88-b3f2-2e01cae5d87f .qti-question .essay points="1" max-words="100" }

Let's examine the predictions from the `Height` model (above).

In what way are the predictions of the `Height` model different from the predictions generated by the `Height2Group` model?

::::::::: { .feedback }

The `Height2Group` model generates only two predictions, one for people categorized as short, another for those categorized as tall. The `Height` model generates a different prediction for every possible value of the `Height` variable, meaning that every student with a different height will get a different predicted thumb length. For students with the same height (e.g., the two students that are both 68 inches tall) the model will predict they have the same thumb length.

:::::::::

::::::
:::

We ran the code below to overlay the predicted thumb lengths of the `Height` model onto the original scatter plot depicting the actual thumb lengths. (The predictions are represented by red circles, accomplished by adding arguments for shape and color to the gf_point() function .)

```
Fingers$prediction <- predict(Height_model)

gf_point(Thumb ~ Height, data = Fingers) %>%
  gf_point(prediction ~ Height, shape = 1, size = 3, color = "firebrick")
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Wp1cF67b.png" width=80%  alt="A scatter plot of Thumb by Height. It is overlaid with all of the point predictions from the Height_model in red. The predictions are aligned along the same path as the regression line." /></p>

Each value of `Height` (e.g., 61, 62, 63) in the dataset gets a unique model prediction (represented by the red circles). See how all the predictions seem to fall in a straight line? This is no accident! It’s because the predictions were generated by the regression line that R fit to the data.

If we chain on `gf_model()` to our scatter plot, the best fitting model lies right on top of the model predictions.

```
gf_point(Thumb ~ Height, data = Fingers) %>%
  gf_point(prediction ~ Height, shape = 1, size = 3, color = "firebrick") %>%
  gf_model(Height_model, color="red")
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/2jRTgz1p.png" width=80%  alt="A scatter plot of Thumb by Height. It is overlaid with all of the point predictions from the Height_model in red, as well as the regression line. The point predictions are right on top of the regression line." /></p>

Note that there are at least two ways to overlay a regression model onto a scatter plot. The first is by using `gf_model()`, which requires that we specify the model we want to see on the plot (e.g., `gf_model(Height_model)`). The advantage of `gf_model()` is that it works for group models as well as regression models.

Another way is to chain on the function `gf_lm()` to the scatter plot. This method doesn't require you to specify a model (it figures that out from information in the scatter plot), but it only works for regression models.
