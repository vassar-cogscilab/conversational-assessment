## 9.8 Correlation

You might have heard of *Pearson’s r,* often referred to as a "correlation coefficient." Correlation is just a special case of regression in which both the outcome and explanatory variables are transformed into z-scores prior to analysis.

::: { .qti-item #b5_Correlation_01 }
:::::: { #768795f6-e0dc-4126-bc42-91dee957a2fd .qti-question .multiple-choice points="1" }

To transform a raw score (e.g., thumb length in mm) into a z-score, we take the residual (thumb length - mean) and divide by the standard deviation of the variable. What is a correct interpretation of the resulting z-score for thumb length?

::::::::: { .choices }

- [It tells you how many standard deviations above or below the mean a particular person's thumb length is.]{ .correct }
- It provides a way to convert a particular person's thumb length from millimeters into other units such as inches.
- It tells you the probability of this thumb length in the population.

:::::::::

::::::
:::

### Working with Standardized Variables

When we do a z-transformation on every value of a variable it is sometimes referred to as *standardizing* the variable. Let’s see what happens when we standardize the two variables we have been working with (`Thumb` and `Height`).

Use the code window below to create two new variables in the `Fingers` data frame: `zThumb` and `zHeight`. The function `zscore()` will standardize a variable by converting all of its values to z-scores.

```{ data-ckcode=true #B5_Code_Correlation_01 }
%%% setup
require(coursekata)

Fingers <- filter(Fingers, Thumb >= 33 & Thumb <= 100)

%%% prompt
# this transforms all Thumb lengths into z-scores
Fingers$zThumb <- zscore(Fingers$Thumb)

# modify this to do the same for Height
Fingers$zHeight <-

%%% solution
# this transforms all Thumb lengths into z-scores
Fingers$zThumb <- zscore(Fingers$Thumb)

# modify this to do the same for Height
Fingers$zHeight <- zscore(Fingers$Height)

%%% test
ex() %>% check_object("Fingers") %>% {
  check_column(., "zThumb") %>% check_equal()
  check_column(., "zHeight") %>% check_equal()
}
```

Because both variables are transformed into z-scores, the mean of each distribution will be 0, and the standard deviation will be 1.

In this chapter we have been using height to explain the variation we see in thumb lengths. Imagine we make two scatter plots, one using `Height` to explain `Thumb`, the other using `zHeight` to explain `zThumb`.

::: { .qti-item #Ch8_Correlation_2 }
:::::: { #c7eab246-fe6d-453d-b392-f32b81b5ec89 .qti-question .multiple-choice points="1" scoring="partial" }

In making these scatter plots, which variables would go on the y-axis? (Select 2.)

::::::::: { .choices }

- [`Thumb`]{ .correct }
- `Height`
- [`zThumb`]{ .correct }
- `zHeight`

:::::::::

::::::

:::::: { #e9302be7-2360-4386-826f-08a5dcef3961 .qti-question .multiple-choice points="1" }

Why?

::::::::: { .choices }

- Because the R code will not run if you do not select this variable for the y-axis.
- [Because of convention—we typically put the outcome variable on the y-axis.]{ .correct }
- Because of convention—we typically put the explanatory variable on the y-axis.
- Because of convention—we typically put the quantitative variable on the y-axis

:::::::::

::::::
:::

Let's go ahead and make these scatter plots. In the code window below, we have provided code to make a scatter plot of `Thumb` by `Height`. Modify the second line to make a scatter plot of `zThumb` by `zHeight`.

```{ data-ckcode=true #B5_Code_Correlation_02 }
%%% setup
require(coursekata)

Fingers <- Fingers %>%
  filter(Thumb >= 33 & Thumb <= 100) %>%
  mutate(
    zThumb = zscore(Thumb),
    zHeight = zscore(Height)
  )

%%% prompt
# this makes a scatter plot of the raw scores
# size makes the points bigger or smaller
gf_point(Thumb ~ Height, data = Fingers, size = 4)

# zThumb and zHeight have already been created for you
# modify the code below to make a scatter plot of the z-scores
gf_point( , data = Fingers, size = 4, color = "navy")

%%% solution
# this makes a scatter plot of the raw scores
# size makes the points bigger or smaller
gf_point(Thumb ~ Height, data = Fingers, size = 4)

# zThumb and zHeight have already been created for you
# modify the code below to make a scatter plot of the z-scores
gf_point(zThumb ~ zHeight, data = Fingers, size = 4, color = "navy")

%%% test
ex() %>% {
  check_function(., "gf_point", index = 1) %>% {
    check_arg(., "object") %>% check_equal()
    check_arg(., "data") %>% check_equal()
  }
  check_function(., "gf_point", index = 2) %>% {
    check_arg(., "object") %>% check_equal()
    check_arg(., "data") %>% check_equal()
  }
}
```

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto; margin-top: 1.5em;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%"><code>Thumb ~ Height</code></th>
            <th style="width:50%"><code>zThumb ~ zHeight</code></th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/7xf6rsqM.png" alt="A scatter plot of the distribution of Thumb by Height." /></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Mq7R6S5K.png" alt="A scatter plot of the distribution of zThumb by zHeight. The two distributions look the same except the scale of the axes." /></p></td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b5_Correlation_02 }
:::::: { #7dc679b2-5d9d-4a38-876e-c6271dda806b .qti-question .multiple-choice points="1" }

Compare the scatter plot of `Thumb` by `Height` (on the left, in black) with the scatter plot of `zThumb` by `zHeight` (on the right, in blue). How are they similar? How are they different?

::::::::: { .choices }

- They depict very different relationships between the variables on the x- and y-axes.
- The shape of the two scatter plots are very different.
- One of the distributions is much less variable than the other.
- [The scale of the axes are different but everything else is the same.]{ .correct }

:::::::::

::::::
:::

### Fitting the Regression Model to Standardized Variables

In the code window below we’ve provided the code to fit a regression line for `Thumb` based on `Height`. Add code to fit a regression model to the two transformed variables, predicting `zThumb` based on `zHeight`.

```{ data-ckcode=true #B5_Code_Correlation_03 }
%%% setup
require(coursekata)
Fingers <- Fingers %>%
  filter(Thumb >= 33 & Thumb <= 100) %>%
  mutate(
    zThumb = zscore(Thumb),
    zHeight = zscore(Height)
  )
Height_model <- lm(Thumb ~ Height, data = Fingers)

%%% prompt
# this fits a regression model of Thumb by Height
lm(Thumb ~ Height, data = Fingers)

# write code to fit a regression model predicting zThumb with zHeight

%%% solution
# this fits a regression model of Thumb by Height
lm(Thumb ~ Height, data = Fingers)

# write code to fit a regression model predicting zThumb with zHeight
lm(zThumb ~ zHeight, data = Fingers)

%%% test
ex() %>%
  check_function("lm", index = 2) %>%
  check_result() %>%
  check_equal()
```

In the table below we show the best-fitting parameter estimates along with the two scatter plots, this time with the best-fitting regression lines overlaid.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%"><code>Thumb ~ Height</code></th>
            <th style="width:50%"><code>zThumb ~ zHeight</code></th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Mq5PhtPG.png" alt="A scatter plot of the distribution of Thumb by Height." /></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/X41KfP19.png" alt="A scatter plot of the distribution of zThumb by zHeight. The two distributions look the same except the scale of the axes." /></p></td>
        </tr>
        <tr>
            <td><pre><code>Coefficients:
(Intercept)       Height
    -3.3295       0.9619  </code></pre></td>
            <td><pre><code>Coefficients:
(Intercept)      zHeight
 -2.074e-16    3.911e-01  </code></pre></td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b5_Correlation_03 }
:::::: { #dcf736ce-3c24-48c8-b955-abde26151838 .qti-question .multiple-choice points="1" }

What is the y-intercept for the model using `zHeight` to predict `` zThumb` ``?

::::::::: { .choices }

- Approximately -2.074
- Approximately 3.911
- [Approximately 0]{ .correct }

:::::::::

::::::
:::

Note that R will sometimes express parameter estimates in scientific notation. Thus, -2.074e-16 means that the decimal point is shifted 16 digits to the left. So, the actual y-intercept of the best-fitting regression line is -.00000000000000018, which is, for all practical purposes, 0.

::: { .qti-item #b5_Correlation_04 }
:::::: { #fbf7452a-a323-46f5-b328-8c7d5d489823 .qti-question .multiple-choice points="1" scoring="partial" }

Which of the following shows you the equation for the `zHeight_model`? (Check all that apply)

::::::::: { .choices }

- [$Y_i=.39X_i+e_i$]{ .correct }
- [$Y_i=0+.39X_i+e_i$]{ .correct }
- $Y_i=-1.8+3.9X_i+e_i$

:::::::::

::::::
:::

We know from earlier that the best-fitting regression line passes through the point of means, which is the point defined by the mean of both the outcome and explanatory variables, shown on the scatter plots below. Note that in the case of `zThumb` and `zHeight`, the mean of each is 0 and the point of means is (0,0).

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%">$\text{Thumb}_i = 3.33 + .96\text{Height}_i + e_i$</th>
            <th style="width:50%">$\text{zThumb}_i = .39\text{zHeight}_i + e_i$</th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/csJmj3jp.png" alt="A scatter plot of the distribution of Thumb by Height overlaid with regression line. The point of means (mean height, mean thumb length) is shown on the regression line." /></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/4sM3CRmB.png" alt="A scatter plot of the distribution of zThumb by zHeight overlaid with regression line. The point of means (0,0) is shown on the regression line." /></p></td>
        </tr>
    </tbody>
</table>
<br>

Because the mean of any standardized variable is 0, a regression line based on standardized variables will always have a y-intercept of 0, meaning that when x is 0, y will also be 0.

### Correlation coefficient: The slope of the standardized regression line

Let's now turn our attention to the slopes (the $b_1$ estimates) of both models, the one based on unstandardized variables and the one based on standardized variables.

::: { .qti-item #b5_Correlation_05 }
:::::: { #ff35b246-b20e-4538-bc21-7a4f1dd09a5d .qti-question .multiple-choice points="1" }

Compare the slopes of the regression line for the two models. In the unstandardized model, what does the slope (.96) mean?

::::::::: { .choices }

- [For every one inch of height, add on .96 mm to predicted thumb length.]{ .correct }
- For every one mm of height, add on .96 mm to predicted thumb length.
- For every one mm of thumb length, add on .96 in to predicted height.
- When height is equal to 0, the thumb length is .96 mm.

:::::::::

::::::

:::::: { #bfa28c41-7cb5-4410-85e3-f8bb8a2c14f8 .qti-question .multiple-choice points="1" }

What does the slope for the standardized model (.39) mean?

::::::::: { .choices }

- [For every one standard deviation increase of `Height`, add on .39 standard deviations to predicted `Thumb` length.]{ .correct }
- The standard deviation of `zThumb` is .39.
- The standard deviation of `zHeight` is .39.
- For every one inch of `Height`, add on .39 mm to predicted `Thumb` length.

:::::::::

::::::
:::

Notice that the slopes are different for the unstandardized and standardized regression lines (.96 versus .39). To interpret the unstandardized slope, you need to know something about how thumbs and heights are measured (e.g., mm and inches). But the standardized slope does not require that additional knowledge.

**The slope of the regression line between the standardized variables is called the correlation coefficient, or Pearson’s $r$.** The correlation coefficient is useful for assessing the strength of a bivariate relationship between two quantitative variables independent of the units on which each variable is measured.

To save you from having to transform variables into z-scores and then fit a regression line just to find out the correlation coefficient, R provides an easy way to directly calculate the correlation coefficient (Pearson’s $r$) from the raw scores: the `cor()` function. Try running the code in the window below.

```{ data-ckcode=true #B5_Code_Correlation_04 }
%%% setup
require(coursekata)

Fingers <- Fingers %>%
    filter(Thumb >= 33 & Thumb <= 100) %>%
    mutate(
        zThumb = zscore(Thumb),
        zHeight = zscore(Height)
    )

%%% prompt
# this calculates the correlation of Thumb and Height
cor(Thumb ~ Height, data = Fingers)

%%% solution
# this calculates the correlation of Thumb and Height
cor(Thumb ~ Height, data = Fingers)

%%% test
ex() %>% check_function("cor") %>% check_result() %>% check_equal()
```

```
[1] 0.3910649
```

Notice that the result of .39 is, exactly, the slope of the standardized regression line, meaning that an increase of 1 standard deviation in height will result in a .39 standard deviation in thumb length.

Correlation coefficients, because they are calculated using standardized variables, have certain characteristics. The most useful of these is that $r$ will always range from -1 to +1. An $r$ of 0 means that the two variables are not related. A positive $r$ means that the variables are positively and linearly related, while a negative $r$ means they are negatively and linearly related.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/nFgQhZKW.png" alt="A range of seven hypothetical scatter plot distributions appear arranged in a line from left to right. They display the expected distribution of points for various correlation coefficients, ranging from a correlation of positive one on the left, where all the points are arranged in a line that slopes upward, to a correlation of negative one on the right, where all the points are arranged in a line that slopes downward. The middle distribution is a scattered cloud of points and labeled as a correlation of zero. As the correlation gets further from zero, the points start to get closer to a line." /></p>

The further away from 0 $r$ is, the stronger the linear relationship between the two variables. Two variables with a correlation of +1 are perfectly related, meaning that a 1 SD increase in one of the variables will produce a 1 SD increase in the other. A correlation of -1 means that two variables are perfectly negatively related.

Note that a relationship between two variables can be highly systematic, but not linear, for example, in the plots on the left and center below. In these cases, even though there is a clear pattern in the scatter plots, the $r$ is close to 0 because the relationship is not linear.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/nFY1sXzW.png" alt="Three side-by-side hypothetical scatter plot distributions. Each distribution has a distinct shape and pattern, but none of them are a linear pattern. The first one appears to curve like a parabola and has a correlation of zero. The second one appears to have four unique quadrants where the points tend to be clumped together and has a correlation of zero. The third one appears to curve up and down in a wave pattern and has a correlation of point four. " /></p>

Even when the $r$ isn't necessarily close to 0, as in the plot on the right where the $r = .4$, it doesn't mean that a straight regression line is the best model for it (perhaps a curved one will be better).
