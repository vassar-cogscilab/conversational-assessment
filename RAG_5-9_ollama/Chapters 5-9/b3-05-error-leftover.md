## 7.5 Error Leftover From the Group Model

Previously, we calculated residuals from the empty model of `Thumb` by starting with the actual thumb length for each student, and then subtracting the predicted value based on the model. In the empty model, all students had the same predicted value.

::: { style="text-align: center;" }
**DATA = MODEL PREDICTION + RESIDUAL**

**RESIDUAL = DATA - MODEL PREDICTION**
:::

For the `Gender` model of `Thumb` we will use the same method, the only difference being that this time there will be two different model predictions, depending on the gender of the student. Still, the predicted thumb length for each student, which depends on their gender, is subtracted from their actual thumb length to get the residuals.

::: { .qti-item #b3_ErrorN_01 }
:::::: { #d8f6124d-3152-4851-ae60-88b610c76e4b .qti-question .multiple-choice points="1" scoring="partial" }

Which of the following equations hold true regardless of whether we are talking about the empty model or the `Gender` model? (Check all that apply.)

::::::::: { .choices }

- residual = empty model + `Gender` model
- [residual = `Thumb` - prediction]{ .correct }
- [**ERROR = DATA - MODEL**]{ .correct }
- **MODEL = ERROR**
- **ERROR = DATA + MODEL**

:::::::::

::::::
:::

The residuals for 6 example students are represented in the plots below for both the empty model (left) and `Gender` model (right). Notice that the placement of the 6 data points is the same from one model to the other; the actual thumb lengths of these students don't change.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th>Residuals from the Empty Model</th>
            <th>Residuals from the Gender Model</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_05_ErrorLeftover_1.jpg" width=100%  alt="On the left, a jitter plot of the distribution of Thumb by Gender, overlaid with a horizontal line in blue showing the empty model for Thumb. A few residuals are drawn above and below the empty model as vertical lines from the data points to the model. The plot caption reads: Residuals from the Empty Model." /></p>
</td>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_05_ErrorLeftover_2.jpg" width=100%  alt="On the right, a jitter plot of the distribution of Thumb by Gender, overlaid with a red horizontal line in each group showing the group mean. The residuals of the same few data points from the jitter plot on the left are drawn above and below the mean lines as vertical lines from the data points to the mean lines. The plot caption reads: Residuals from the Gender model." /></p>
</td>
        </tr>
    </tbody>
</table>

The predictions and residuals of the two models, however, are different. For the empty model, each student's residual is calculated in relation to the mean `Thumb` of all students in the dataset. For the `Gender` model, each student's residual is calculated in relation to the predicted `Thumb` for their gender.

Something to keep in mind as well is that looking at residuals can help you interpret your data. Take, for example, the male student whose thumb length is circled in the plots below. Looking at residuals can help you see something interesting about this student.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th>In relation to the empty model, this student has a larger than average thumb length.</th>
            <th>In relation to the gender model, the same student has a slightly below average thumb length given that they are male.</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_05_ErrorLeftover_3.jpg" width=100%  alt="On the left, a jitter plot of the distribution of Thumb by Gender, overlaid with a horizontal line in blue showing the empty model for Thumb. A single residual in the male group is drawn above the empty model as a vertical line from the data point to the model." /></p>
</td>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_05_ErrorLeftover_4.jpg" width=100%  alt="On the right, a jitter plot of the distribution of Thumb by Gender, overlaid with a red horizontal line in each group showing the group mean. The residual for the same data point as in the jitter plot on the left appears is now below the line for the male group." /></p>
</td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b3_ErrorN_02 }
:::::: { #4583e2a5-5171-4a61-961d-a622845ebda5 .qti-question .multiple-choice points="1" }

Why is the thumb length (circled in the figures above), higher than the empty model prediction but lower than the gender model prediction?

::::::::: { .choices }

- because the student's thumb has shrunk down a bit
- [because his thumb length is larger than the empty model would predict but a smaller than what the gender model would predict]{ .correct }

:::::::::

::::::
:::

### Using R to Calculate Residuals from the Gender Model

Just as we earlier used the `predict()` function to generate a predicted thumb length to each student in the data frame, we can use the `resid()` function to calculate the residual for each student. We've done that with the code below, and printed out the data table for just the 6 students we have been looking at.

```
Fingers$Gender_predict <- predict(Gender_model)
Fingers$Gender_resid <- resid(Gender_model)
head(select(Fingers, Gender, Thumb, Gender_predict, Gender_resid))
```

```
     Gender Thumb Gender_predict Gender_resid
1 female    64    58.25585  5.744152
2 female    56    58.25585 -2.255848
3 female    52    58.25585 -6.255848
4   male    66    64.70267  1.297333
5   male    70    64.70267  5.297333
6   male    62    64.70267 -2.702667
```

::: { .qti-item #b3_ErrorN_03 }
:::::: { #037d5aea-97b9-465f-b8e8-a673204ce40a .qti-question .essay points="1" max-words="100" }

Take a look at the output above. Is it still true that **DATA = MODEL + ERROR**? Explain how you can tell from the output?

::::::::: { .feedback }

Yes, **DATA = MODEL + ERROR**. You can confirm this by adding `Sex_predict` plus `Sex_resid` for each row. The sums are each equal to `Thumb`.

:::::::::

::::::

:::::: { #e1424d8c-d6a9-44ac-a1c4-6be9abc0e450 .qti-question .multiple-choice points="1" }

The GLM notation for the `Gender` model is:

$$
Y_i=b_0+b_{1}X_i+e_i
$$

What notation would be used to represent the column `Gender_predict` in the R output above?

::::::::: { .choices }

- $Y_i$
- $b_0$
- $b_0 + b_1$
- [$b_0 + b_{1}X_{i}$]{ .correct }
- $e_i$

:::::::::

::::::

:::::: { #62d67088-ab27-4c8d-a46c-9884590fc515 .qti-question .multiple-choice points="1" }

What notation would be used to represent the column `Gender_resid` in the R output above?

::::::::: { .choices }

- $Y_i$
- $b_0$
- $b_0+b_1$
- $b_0+b_1$
- [$e_i$]{ .correct }

:::::::::

::::::
:::
