## 9.4 Comparing Regression Models to Group Models

### Comparing the `Height2Group` Model and the `Height` Model

We now know how to specify and fit two different kinds of models: group models (e.g., `Height2Group_model`) and regression models (`Height_model`), let's just think for a bit on what the similarities and differences are between these models.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th>Symbol</th>
            <th>Group Model<br>$Y_i=b_0+b_1X_i+e_i$<br>$\text{Thumb}_i=b_0+b_1\text{Height2Grouptall}_i+e_i$</th>
            <th>Regression Model<br>$Y_i=b_0+b_1X_i+e_i$<br>$\text{Thumb}_i=b_0+b_1\text{Height}_i+e_i$</th>
    </thead>
    <tbody>
        <tr>
            <td>$Y_i$</td>
            <td>Thumb length of a student <i>i</i></td>
            <td>Thumb length of a student <i>i</i></td>
        </tr>
        <tr>
            <td>$b_0$</td>
            <td><mark>Predicted thumb length when $\text{Height2Group}_i = 0$)</mark><br>(mean thumb length for short group)</td>
            <td><mark>Predicted thumb length when $\text{Height}_i=0$</mark><br>(y-intercept for regression line)</td>
        </tr>
        <tr>
            <td>$b_1$</td>
            <td><mark>Adjustment to predicted thumb length for a tall student</mark><br>(the mean difference between the two group means)</td>
            <td><mark>Adjustment to predicted thumb length for a one-unit increase in height</mark><br>(the slope of the regression line)</td>
        </tr>
        <tr>
            <td>$X_i$</td>
            <td>Height2Group of a student <i>i</i>, coded as 0=not-tall, 1=tall</td>
            <td>Height of a student <i>i</i> in inches</td>
        </tr>
        <tr>
            <td>$e_i$</td>
            <td>Error for student <i>i</i></td>
            <td>Error for student <i>i</i></td>
        </tr>
        <tr>
            <td>visualization of the model</td>
            <td style="width:45%"><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/X3NPF6hs.png" alt="A jitter plot of Thumb by Height2Group with the model predictions in red." /></p></td>
            <td style="width:45%"><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/4sRzgLBg.png" alt="A scatter plot of Thumb by Height with the model predictions in red." /></p></td>
        </tr>
    </tbody>
</table>
<br>

### Fitting a Regression Model By Accident When You Don’t Want One

Although R is pretty smart about knowing which model to fit, it won’t always do the right thing. If you code the grouping variable with character strings such as "female" and "male" or "short" and “tall,” R will make the right decision to fit a group model because it knows the variable must be categorical. But if you code the same grouping variable as 1 and 2 (maybe you forget to make it a factor), R may get confused and fit the model as though the explanatory variable is quantitative.

For example, we’ve added a new variable to our `Fingers` data called `GenderNum`. Here is what the data look like.

```
 Thumb  Gender GenderNum
1    66   male         2
2    64 female         1
3    56 female         1
4    70   male         2
5    52 female         1
6    62   male         2
```

If you take a look at the variables `Gender` and `GenderNum`, they have the same information. Students 2, 3, and 5 are in one group and students 1, 4, and 6 are in another group. If we fit a model with `Gender` (and call it the `Gender_model`) or `GenderNum` (and call it the `GenderNum_model`), we would expect the same estimates. Let’s try it.

```{ data-ckcode=true #B5_Code_Comparing_01 }
%%% setup
require(coursekata)

Fingers$GenderNum <- as.numeric(Fingers$Gender)

%%% prompt
# fit a model of Thumb length based on Gender
Gender_model <- lm()

# fit a model of Thumb length based on GenderNum
GenderNum_model <- lm()

# this prints the parameter estimates from the two models
Gender_model
GenderNum_model

%%% solution
# fit a model of Thumb length based on Gender
Gender_model <- lm(Thumb ~ Gender, data=Fingers)

# fit a model of Thumb length based on GenderNum
GenderNum_model <- lm(Thumb ~ GenderNum, data=Fingers)

# this prints the parameter estimates from the two models
Gender_model
GenderNum_model

%%% test
ex() %>% {
    check_object(., "Gender_model") %>% check_equal()
    check_object(., "GenderNum_model") %>% check_equal()
    check_output_expr(., "Gender_model
GenderNum_model")
}
```

```
Call:
lm(formula = Thumb ~ Gender, data = Fingers)

Coefficients:
(Intercept)   Gendermale
     58.256        6.447
```

```
Call:
lm(formula = Thumb ~ GenderNum, data = Fingers)

Coefficients:
(Intercept)    GenderNum
     51.809        6.447
```

::: { .qti-item #b5_Comparing_01 }
:::::: { #341796e6-8e59-4666-902f-958f1ae2ff5a .qti-question .multiple-choice points="1" }

Which parameter estimate is different in the `Gender` model versus the `GenderNum` model?

::::::::: { .choices }

- [$b_0$, the predicted thumb length when $X_i=0$]{ .correct }
- $b_1$, the adjustment to predicted thumb length for a 1 unit increase in $X_i$

:::::::::

::::::

:::::: { #8a18c37f-ff1e-4ffe-b344-71eb955792c9 .qti-question .essay points="1" max-words="200" }

Why aren't the parameter estimates in the `GenderNum` model identical to those of the `Gender` model?

::::::
:::

Because `Gender` is a factor (i.e., a categorical variable), `lm()` fits a group model. But for `GenderNum`, `lm()` thinks the 1 or 2 coding refers to a quantitative variable. Because we did not tell R to treat `GenderNum` as a factor, it fits a regression line instead of a two-group model. If it does that, the meaning of the estimates will not be what you expect for the group model.

The $b_1$ estimate will be the same as in the two-group model; because it represents the adjustment in thumb length for a one unit change in $X_i$. For `Gender`, a 1-unit change is to go from not male ($X_i=0$) to male ($X_i=1$). For $GenderNum$, a 1-unit change similarly goes from not male ($X_i=1$) to male ($X_i=2$).

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%">$b_1$ of the $Gender$ model,<br>a group model</th>
            <th style="width:50%">$b_1$ of the $GenderNum$ model,<br>an accidental regression model</th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b5_04_Fitting_1.jpg" alt="On the left, a representation of b-sub-one of the Gender model, a group model, as a jitter plot of Thumb predicted by Gender (female and male), with the model overlaid as horizontal lines at the mean of each group. The horizontal distance between each group is labeled as the one unit change in Gender, and the vertical distance between each group mean is labeled to say that we adjust predicted Thumb by 6.45." /></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b5_04_Fitting_2.jpg" alt="On the right, a representation of b-sub-one of the GenderNum model, an accidental regression model, as a jitter plot of Thumb predicted by Gender (female and male), with the model overlaid as a regression line running through the mean of each group. The horizontal distance between each group is labeled as the one unit change in GenderNum, and the vertical distance between each group mean is labeled to say that we adjust predicted Thumb by 6.45." /></p></td>
        </tr>
    </tbody>
</table>
<br>

But the $b_0$ estimate will be different in the `GenderNum` model, where it represents the y-intercept of the regression line, or the predicted thumb length when $X_i$ equals 0. This makes no sense, however, when there are only two groups and they are coded 1 and 2. This is an accidental regression model.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%">$b_0$ of the $Gender$ model</th>
            <th style="width:50%">$b_0$ of the $GenderNum$ model</th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b5_04_Fitting_3.jpg" alt="On the left, a representation of b-sub-zero of the Gender model as a jitter plot of Thumb predicted by Gender (female and male), with the model overlaid as horizontal lines at the mean of each group. The line for the mean of the female group is labeled to say when Gender equals zero, predicted Thumb equals 58.26." /></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b5_04_Fitting_4.jpg" alt="On the right, a representation of b-sub-zero of the GenderNum model as a jitter plot of Thumb predicted by Gender (female and male), with the model overlaid as a regression line running through the mean of each group. The point of the regression line nearest to the y-axis, where GenderNum equals zero, is labeled to say when GenderNum equals zero, predicted Thumb equals 51.81." /></p></td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b5_Comparing_02 }
:::::: { #a8509b24-3cb6-4778-ade9-cbc4c52ac401 .qti-question .essay points="1" max-words="200" }

What do you think would happen if we coded the `GenderNum` groups 0 and 1 instead of 1 and 2? Why?

::::::::: { .feedback }

If we did that, 0 would mean "not male" and 1 would mean "male" (just like the dummy coded values of $X_i$ in the `Sex` model. This change would make the parameter estimates of the `SexNum` model identical to those of the `Sex` model.

:::::::::

::::::
:::
