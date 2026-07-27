## 9.3 Interpreting the Parameter Estimates for a Regression Model

Previously, we used the `lm()` function to fit the `Height` model of `Thumb` and saved it as `Height_model`:

```
Height_model <- lm(Thumb ~ Height, data = Fingers)
```

Let's now look at the parameter estimates for this model and see how to interpret them. Use the code block below to print out the parameter estimates for the height model.

```{ data-ckcode=true #B5_Code_Regression_01 }
%%% setup
library(coursekata)

%%% prompt
# saves the Height model
Height_model <- lm(Thumb ~ Height, data = Fingers)

# print it out

%%% solution
# saves the Height model
Height_model <- lm(Thumb ~ Height, data = Fingers)

# print it out
Height_model

%%% test
ex() %>% check_output_expr("Height_model")
```

```
Call:
lm(formula = Thumb ~ Height, data = Fingers)

Coefficients:
(Intercept)       Height
    -3.3295       0.9619
```

::: { .qti-item #b5_Regression_01 }
:::::: { #f5f885b3-323a-484e-b37e-0504e2e26174 .qti-question .multiple-choice points="1" scoring="partial" }

What is the -3.33 in the output above? (Check all that apply.)

::::::::: { .choices }

- [$b_0$]{ .correct }
- $b_1$
- $X_i$
- The slope of a regression line
- The difference between two groups
- [The intercept (the value of $Y_i$ when $X_i = 0$)]{ .correct }

:::::::::

::::::

:::::: { #498ac7b3-8adb-4dee-816c-4fff3c15cd0a .qti-question .multiple-choice points="1" scoring="partial" }

What is the 0.96 in the output above? (Check all that apply.)

::::::::: { .choices }

- $b_0$
- [$b_1$]{ .correct }
- $X_i$
- [The slope of a regression line]{ .correct }
- The difference between two groups
- The intercept (the value of $Y_i$ when $X_i = 0$)

:::::::::

::::::
:::

The `Intercept` corresponds to $b_0$ and the `Height` coefficient corresponds to $b_1$. We can write our fitted model as:

$$\text{Thumb}_i=-3.33 + 0.96\text{Height}_i+e_i$$

Or, equivalently, using GLM notation, it can be written:

$$Y_i=-3.33 + 0.96X_i+e_i$$

::: { .qti-item #b5_Regression_02 }
:::::: { #bef320d9-3ddd-4f3f-9535-348933be4130 .qti-question .multiple-choice points="1" scoring="partial" }

What would this model predict as the thumb length of a student with a height of 0? (Check all that apply.)

::::::::: { .choices }

- [$b_0$]{ .correct }
- $b_1$
- [$b_0 + b_1(0)$]{ .correct }
- [-3.33]{ .correct }
- 0.96
- -3.33 + 0.96

:::::::::

::::::
:::

$b_0$, which is -3.33, is the y-intercept. It's the predicted $Y_i$ (`Thumb`) when $X_i$$ (`Height`) equals 0.

Neither a height of 0 inches nor a thumb length of -3.33 mm are possible. Not all predictions from a regression model make sense. We should always be thinking about which values of the predictors, and which predictions, are reasonable.

### How Regression Models Make Predictions

We can use the `Height` model to predict the thumb length of students of different heights (just like we used the `Height2Group` model to predict the thumb length of short and tall groups of students).

::: { .qti-item #b5_Regression_03 }
:::::: { #a562c349-1bd6-40eb-97e4-f1d9d00d8874 .qti-question .multiple-choice points="1" }

We can write the fitted `Height` model like this:

$\text{Thumb}_i=-3.33+0.96\text{Height}_i+e_i$.

Which part of this equation would be used to predict the thumb length of a new student?

::::::::: { .choices }

- $\text{Thumb}_{i}=-3.33 + 0.96\text{Height}_{i}+e_{i}$
- $-3.33 + 0.96\text{Height}_{i}+e_{i}$
- [$-3.33 + 0.96\text{Height}_{i}$]{ .correct }

:::::::::

::::::
:::

Recall that thumb length (and predicted thumb length) are expressed in millimeters. $b_0$ (-3.33) is the predicted thumb length in millimeters for a student with a height of 0 inches. If we stretch out the x-axis to include 0, we would expect the regression line to cross the y-axis at -3.33. (Notice, however, that in the plot below that there are no actual students who are 0 inches in height, for obvious reasons!)

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/SSJNHhwG.png" width=80%  alt="A scatter plot of Thumb by Height overlaid with the regression line in red. A vertical arrow points to the part of the regression line where the x-axis equals zero and has the caption: when Height equals zero, predicted Thumb equals -3.33." /></p>

The $b_1$ estimate (0.96) is the slope: for every 1 unit increase in `Height`, our model predicts a 0.96 unit increase in `Thumb`. The fact that height is measured in inches and thumb length in millimeters is not a problem; the regression line is a function (the $b_0 + b_1Height_i$ part) that takes in inches and then makes a prediction  in millimeters. This means that students who are 1 inch taller are predicted by our model to have thumbs that are 0.96 millimeters longer (on average). Here’s a visual representation:

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th>default scale</th>
            <th>zooming in</th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Z4XCrCvx.png" alt="On the left, a scatter plot of Thumb predicted by Height with the regression model overlaid. The plot is depicted at the default scale, thus, the slope appears very small and difficult to see." /></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/1s7Dbmn8.png" alt="On the right, a scatter plot of Thumb predicted by Height with the regression model overlaid. The plot is depicted at a zoomed in scale, thus, it is easier to point out that the slope, or b-sub-1, of the model can be represented as the vertical distance the regression line rises (a rise of 0.96), for every one unit increase in Height." /></p></td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b5_Regression_04 }
:::::: { #5e9cc93c-6d72-4401-9548-60f5ffd1681c .qti-question .multiple-choice points="1" }

Which of these expressions would generate the height model's predicted thumb length for a student who is 71 inches tall?

::::::::: { .choices }

- [$-3.33 + 0.96(71)$]{ .correct }
- $-3.33 + 0.96+(71)$
- $71 + 0.96$
- $71X_i$

:::::::::

::::::
:::

The predicted thumb length of a student who is 71 inches tall is 64.83 mm. This is the value of $Y$ (`Thumb`) on the regression line when $X$ (`Height`) is 71, as visualized below:

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/RS1DT606.png" width=80%  alt="A scatter plot of Thumb by Height overlaid with the regression line in red. A dashed line extends from the x-axis where Height equals 71 up to the regression line. It intersects with a point along the regression line where the predicted Thumb equals 64.83" /></p>

::: { .qti-item #b5_Regression_05 }
:::::: { #48295537-f614-4b52-bba6-e63042bf5cf9 .qti-question .multiple-choice points="1" }

Which of these expressions would generate the height model's predicted thumb length for a student with a height of -10 inches?

::::::::: { .choices }

- $-3.33 - 10$
- $-3.33 + 0.96 - 10$
- $0.96 - 10$
- [$-3.33 + 0.96 * -10$]{ .correct }

:::::::::

::::::
:::

### Regression Coefficients are Not Symmetrical

When you fit a regression model, it matters which variable is the outcome and which is the explanatory variable. For example, if you fit the model `Thumb ~ Height` you won't get the same y-intercept and slope you would if you fit the model `Height ~ Thumb`.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <tbody>
        <tr>
            <td style="width:50%"><pre><code>Call:
lm(formula = Thumb ~ Height, data = Fingers)

Coefficients:
(Intercept)       Height
    -3.3295       0.9619  </code></pre></td>
            <td style="width:50%"><pre><code>Call:
lm(formula = Height ~ Thumb, data = Fingers)

Coefficients:
(Intercept)        Thumb
     56.391        0.159  </code></pre></td>
        </tr>
    </tbody>
</table>
<br>

The reason for this is that the units, and the distributions of the variables, are different. If the outcome is `Thumb`, then the slope is the adjustment to predicted thumb length for a one-inch increase in height. But if the outcome is `height`, then the slope is the adjustment to predicted *height* length for a one-millimeter increase in thumb length. These are two entirely different things.
