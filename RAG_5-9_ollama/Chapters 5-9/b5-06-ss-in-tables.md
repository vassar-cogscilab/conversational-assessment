## 9.6 Sums of Squares in the ANOVA Table

Finally, let’s use the ANOVA table to examine the fit of the height model. We have saved `Height_model` in the code block below. Use `supernova()` to generate the ANOVA table.

```{ data-ckcode=true #B5_Code_Assessing_01 }
%%% setup
require(coursekata)

%%% prompt
# this saves the Height_model
Height_model <- lm(Thumb ~ Height, data = Fingers)

# print the ANOVA tables for this model

%%% solution
# this saves the Height_model
Height_model <- lm(Thumb ~ Height, data = Fingers)

# print the ANOVA tables for this model
supernova(Height_model)

%%% test
ex() %>%
  check_function("supernova") %>%
  check_result() %>%
  check_equal()
```

Below we have printed out the resulting ANOVA table for the `Height_model` along with the one we produced earlier for the `Height2Group_model`.

::: { .alert .alert-info }
**Height Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height

                               SS  df       MS      F    PRE     p
----- --------------- | --------- --- -------- ------ ------ -----
Model (error reduced) |  1816.862   1 1816.862 27.984 0.1529 .0000
Error (from model)    | 10063.349 155   64.925
----- --------------- | --------- --- -------- ------ ------ -----
Total (empty model)   | 11880.211 156   76.155
```

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

::: { .qti-item #Ch8_Assessing_1 }
:::::: { #6e126cd3-9be5-4e1d-a94c-ded8f0418462 .qti-question .multiple-choice points="1" }

What is the outcome variable for the `Height2Group` model?

::::::::: { .choices }

- `Height`
- `Groups`
- `Gender`
- [`Thumb` length]{ .correct }

:::::::::

::::::

:::::: { #877e7c75-d46e-4533-a0c6-f9626b968370 .qti-question .multiple-choice points="1" }

What about for the `Height` model?

::::::::: { .choices }

- `Height`
- `Groups`
- `Gender`
- [`Thumb` length]{ .correct }

:::::::::

::::::

:::::: { #1870ee2b-910a-49d2-b6e6-5b477c533ec8 .qti-question .multiple-choice points="1" }

Look at the total sum of squares for both models. Why are they the same?

::::::::: { .choices }

- This is a coincidence. Most of the time SS Total would not be the same.
- This is because both models use some information about `Height` as the explanatory variable.
- [This is because both models have the same outcome variable. The SS Total is always the sum of squared residuals from the values of the outcome variable to the empty model of this variable.]{ .correct }

:::::::::

::::::
:::

SS Total is the sum of squared residuals from the empty model. Total sum of squares is only about the outcome variable, and isn’t affected by the explanatory variable or variables. When we use sum of squares to compare statistical models, we are modeling the same outcome variable.

### SS Error from Three Models

The table below summarizes the sums of squares leftover (SS Error) after fitting each of the three models we have been considering. All of these are calculated the same way, by summing the squared residuals from the model predictions.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th width=30%>Model</th>
            <th width=30%>Leftover SS</th>
            <th width=30%>Statistic Name</th>
    </thead>
    <tbody>
        <tr>
            <td>Empty model</td>
            <td>11,880</td>
            <td>Sum of Squares Total (SST)</td>
        </tr>
        <tr>
            <td><code>Height2Group</code> model</td>
            <td>11,049</td>
            <td>Sum of Squares Error (SSE)</td>
        </tr>
        <tr>
            <td><code>Height</code> model</td>
            <td>10,063</td>
            <td>Sum of Squares Error (SSE)</td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b5_ANOVA_01 }
:::::: { #664c3d32-2b74-4995-8f81-99e1cd390e5c .qti-question .multiple-choice points="1" scoring="partial" }

Which of the following statements are true based on the table above? (Check all that are true.)

::::::::: { .choices }

- [Both the `Height2Group` and `Height` models reduce error compared to the empty model.]{ .correct }
- Both the `Height2Group` and `Height` models have more leftover error than the empty model.
- [The SSEs are both smaller than the SST.]{ .correct }
- The SSEs are both larger than the SST.

:::::::::

::::::
:::

The more error there is leftover after fitting a model, the less of the total variation is explained. The empty model tells us how much total variation there is in the outcome variable. SS Error tells us how much of that error remains *unexplained* after fitting a more complex model.

::: { .qti-item #b5_ANOVA_02 }
:::::: { #8cb3dade-f99c-46ad-8de9-bb18d0ba9cc0 .qti-question .multiple-choice points="1" }

According to the leftover error in the table above, which model explains more of the variation in thumb length?

::::::::: { .choices }

- [The `Height` model because it has a smaller SS Error than the `Height2Group` model.]{ .correct }
- The `Height2Group` model because it has a smaller SS Error than the `Height` model.
- They explain the same amount of error because their SS Total is the same.

:::::::::

::::::
:::

### SS Model

SS Model is the amount by which the error is reduced under the complex model (e.g., the `Height` model) compared with the empty model. As developed previously for group models, SS Model is easily calculated by subtracting SS Error from SS Total. This is the same, regardless of whether you are fitting a group model or a regression model.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b5_06_SSModel_1.jpg" width=80%  alt="Diagram showing the partitioning of Sum of Squares. A circle representing SS Total from the Empty Model of Thumb is partitioned into SS Model (Error Reduced by the Explanatory Variable (e.g., Height or Gender) and SS Error (Error Unexplained by the Explanatory Variable). At the bottom, the entire circle is labeled with the equation SS Total = SS Model + SS Error." /></p>

It also is possible to calculate SS Model in the regression model directly, in much the same way we did for the group model. We simply take each person's predicted score under the regression model and calculate its distance from the prediction of the empty model. This is the amount by which the model has reduced each person's error compared with the empty model. We then square these distances and add them up to get SS Model.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%"><code>Height2Group</code> model's error reduced</th>
            <th style="width:50%"><code>Height</code> model's error reduced</th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b5-06-ss-model-table-graph1.png" alt="On the left, a jitter plot of Thumb predicted by Height2Group (short and tall), with the empty model overlaid as a blue horizontal line through the mean of Thumb, and Height2Group model overlaid as red horizontal lines through the mean of each group. The vertical distance between the predictions of each model is labeled as error reduced." /></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/194BFQKx.png" alt="On the right, a jitter plot of Thumb predicted by Height, with the empty model overlaid as a blue horizontal line, and the Height model is overlaid as a red, sloping regression line. The vertical distance between the predictions of each model is labeled as error reduced." /></p></td>
        </tr>
    </tbody>
</table>
<br>

::::::::: { .qti-item #Ch8_Assessing_3 }
:::::: { #3682eb68-3096-4a6d-bc42-dc4ba2aba6ce .qti-question .association
points="1" }
To summarize, which SS goes with which distances?
::: associations

- [SS Total]{match="3"}
- [SS Error]{match="2"}
- [SS Model]{match="1"}
:::
::: choices

1. From complex model's prediction to empty model's prediction
2. From data to complex model's prediction
3. From data to empty model's prediction
:::
::::::
:::::: { #92e87465-9f0b-4b68-be93-57607617b0b3 .qti-question .multiple-choice
points="1" }
If we were to run supernova on the `Height` model, which values would be
exactly the same as the supernova table of the `Height2Group` model?
::: choices

- SS Model
- SS Error
- [SS Total]{.correct}
:::
::::::
:::::::::
