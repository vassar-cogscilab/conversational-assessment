## 9.13 Chapter 13 Review Questions 2

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B4_Review2_01 }
:::::: { #88667d3c-63ff-4401-b93a-6da6207c30bb .qti-question .multiple-choice points="1" }

1\. You are interested in females' rating of how much they like their male dates (`LikeF`). In particular, you wonder if variation in `LikeF` is better explained by how attractive they think the male is (`AttractiveF`), or by how fun they think the males is (`FunF`). Which of these plots would best help you explore this question?

::::::::: { .choices }

- Box plot (i.e., `gf_boxplot`)
- [Scatter plots(i.e., `gf_point`)]{ .correct }
- Faceted histograms (i.e., `gf_histogram` with `gf_facet_grid`)
- All of the above would be able to depict these relationships equally clearly.

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_02 }
:::::: { #681bc988-73c8-451f-afed-2bfdfecadc76 .qti-question .multiple-choice points="1" }

```
Call:
lm(~formula = LikeF ~ AttractiveF, data = SpeedDate)

Coefficients:
(Intercept)  AttractiveF
     2.8607       0.5548


Call:
lm(formula = LikeF ~ IntelligentF, data = SpeedDate)

Coefficients:
(Intercept)  IntelligentF
     ~2.4104        0.4952
```

2\. We fit two models in which `LikeF` was the outcome variable. The first used `AttractiveF` as the explanatory variable, the second, `IntelligentF`. Based on the parameter estimates for the two models (shown above), can you tell which model explains more variation in `LikeF`?

::::::::: { .choices }

- Yes, the `AttractiveF` model explains more variation in `LikeF` because the parameter estimates for `AttractiveF` are larger than for `IntelligentF.`
- Yes, the `IntelligentF` model explains more variation in `LikeF` because the intercept for the `IntelligentF` model is closer to 0.
- No, it's not possible to compare models that have different explanatory variables.
- [No, it's not possible to tell from the parameter estimates how much variation has been explained by a model.]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_03 }
:::::: { #bfae6895-c7a8-465c-a565-1d8961aaec59 .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: LikeF ~ AttractiveF

                              SS  df      MS       F   PRE     p
----- --------------- | ------- --- ------- ------- ----- -----
Model (error reduced) | 245.113   1 245.113 121.185 .3797 .0000
Error (from model)    | 400.482 198   2.023
----- --------------- | ------- --- ------- ------- ----- -----
Total (empty model)   | 645.595 199   3.244


Analysis of Variance Table (Type III SS)
Model: LikeF ~ IntelligentF

                              SS  df     MS      F   PRE     p
----- --------------- | ------- --- ------ ------ ----- -----
Model (error reduced) |  99.106   1 99.106 35.907 .1535 .0000
Error (from model)    | 546.489 198  2.760
----- --------------- | ------- --- ------ ------ ----- -----
Total (empty model)   | 645.595 199  3.244
```

3\. We fit two models in which `LikeF` was the outcome variable. The first used `AttractiveF` as the explanatory variable, the second, `IntelligentF`. Above we show the analysis of variance tables produced by `supernova`() for the two models. Which of the following would make you think that the `AttractiveF` model explain more variation in `LikeF` than the `IntelligentF` model?

::::::::: { .choices }

- PRE for the `AttractiveF` model is greater than for the `IntelligentF` model.
- SS model for the `AttractiveF` model is greater than for the `IntelligentF` model.
- SS error is less for the `AttractiveF` model than for the `IntelligentF` model.
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_04 }
:::::: { #a11bbaaa-b482-4586-87ab-51d94b902933 .qti-question .multiple-choice points="1" }

4\. The plot below was made to explore whether variation in being liked (`LikeF`) might be explained by being perceived as fun (`FunF`). If we fit the empty model to this data, how would we depict it on this plot?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/SqgTcgfg.png" class="lrn-image-center" width="500" height="333" alt="A scatter plot of the distribution of LikeF by FunF in SpeedDating." />

::::::::: { .choices }

- [A horizontal line drawn at the mean of `LikeF`]{ .correct }
- A vertical line drawn at the mean of `FunF`
- A diagonal line that bisects the cloud of points
- You would not be able to represent the empty model visually because it is single number.

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_05 }
:::::: { #0d649519-a271-4730-a4f1-e5c7c58eafd3 .qti-question .multiple-choice points="1" }

A researcher wondered whether females liked males of the same race as them (`LikeF`) more than males of a different race. To investigate this question they created a new variable called called `RaceMatch` with this code:

```
SpeedDating$RaceMatch <- SpeedDating$RaceM == SpeedDating$RaceF
```

5\. We then fit a model of `LikeF` using `RaceMatch` as the explanatory variable. How would you represent this `RaceMatch` model in GLM notation?

::::::::: { .choices }

- $Y_i=b_1X_i+e_i$
- [$Y_i=b_0+b_1X_i+e_i$]{ .correct }
- $Y_i=b_0+b_1X_{1i}+b_2X_{2i}+e_i$
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_06 }
:::::: { #e84285c7-6d54-48b0-a2f1-f16616b27f73 .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: LikeF ~ AttractiveF

                              SS  df      MS       F   PRE     p
----- --------------- | ------- --- ------- ------- ----- -----
Model (error reduced) | 245.113   1 245.113 121.185 .3797 .0000
Error (from model)    | 400.482 198   2.023
----- --------------- | ------- --- ------- ------- ----- -----
Total (empty model)   | 645.595 199   3.244


Analysis of Variance Table (Type III SS)
Model: LikeF ~ IntelligentF

                              SS  df     MS      F   PRE     p
----- --------------- | ------- --- ------ ------ ----- -----
Model (error reduced) |  99.106   1 99.106 35.907 .1535 .0000
Error (from model)    | 546.489 198  2.760
----- --------------- | ------- --- ------ ------ ----- -----
Total (empty model)   | 645.595 199  3.244
```

6\. We fit two models in which `LikeF` was the outcome variable. The first used `AttractiveF` as the explanatory variable, the second, `IntelligentF`. Above we show the analysis of variance tables produced by `supernova()` for the two models. Why is the SS total the same value for the two models?

::::::::: { .choices }

- Both are based on residuals from the mean of the same explanatory variable.
- [Both are based on residuals from the mean of the same outcome variable.]{ .correct }
- All models that use the same data frame will have the same SS total.
- The explanatory variable for both models is a quantitative variable.

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_07 }
:::::: { #d1728f90-0e29-47af-85e5-acf7a59316bb .qti-question .multiple-choice points="1" }

min Q1 median Q3 max  mean       sd   n missing
       2  7      8  9  10 7.845 1.425177 200       0

7\. Above we show the `favstats()` for females' ratings of their date's intelligence (`IntelligentF`). If the researchers collected a new sample of 200 speed dates, what value in this output would be different?

::::::::: { .choices }

- Standard deviation
- Mean
- Median
- [Most likely, all of the above]{ .correct }

:::::::::

::::::
:::

```{ data-ckcode=true #B4_Code_Review2_01  data-submittable=false }
%%% setup
require(coursekata)
SpeedDate <- na.omit(SpeedDating)

%%% prompt
# run your code here

```

::: { .qti-item #B4_Review2_08 }
:::::: { #5637ce23-42c1-40e1-9643-18831243c3aa .qti-question .multiple-choice points="1" }

8\. Using the `SpeedDating` data frame, fit a model in which `LikeF` is the outcome variable and `FunF` is the explanatory variable. Based on the model, what would you predict a male's `LikeF` rating would be if his `FunF` rating was 0?

::::::::: { .choices }

- 0
- 0.5904
- [2.5013]{ .correct }
- 2.5013 + 0.5904

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_09 }
:::::: { #56d49a15-8b06-4e7c-9fbc-1766133c6e85 .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: LikeF ~ IntelligentF

                              SS  df     MS      F   PRE     p
----- --------------- | ------- --- ------ ------ ----- -----
Model (error reduced) |  99.106   1 99.106 35.907 .1535 .0000
Error (from model)    | 546.489 198  2.760
----- --------------- | ------- --- ------ ------ ----- -----
Total (empty model)   | 645.595 199  3.244
```

9\. Which of the following would be a correct interpretation of the number 3.244 in the `supernova()` table above?

::::::::: { .choices }

- It is, roughly, the total number of ratings in the data frame.
- It is, roughly, the total number of squared means based on the empty model.
- [It is, roughly, the average squared residual from the Grand Mean.]{ .correct }
- It is, roughly, the standard deviation around the Grand Mean.

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_10 }
:::::: { #302684d1-0943-4852-8c06-f26afc355558 .qti-question .multiple-choice points="1" }

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/BqMhXm7m.png" class="lrn-image-center" width="500" height="333" alt="A is the distance between data points in a group model and the predicted value for data points from the group model. B is the distance between the predicted value for data points from the group model and the grand mean from the empty model. C is the distance between data points in a group model and the grand mean from the empty model. " />

10\. The orange circles in the diagram above represent data points and the two red horizontal line segments represent the group model. Which distance would be used to calculate the sum of squares error?

::::::::: { .choices }

- [A]{ .correct }
- B
- C
- None of these

:::::::::

::::::
:::

::: { .qti-item #B4_Review2_11 }
:::::: { #ef6a6782-059b-43d9-9b84-3fd7cf66cceb .qti-question .multiple-choice points="1" }

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/mBzSTLGp.png" class="lrn-image-center" width="500" height="333" alt="A is the distance between data points and the predicted value for data points from the regression model. B is the distance between the predicted value for data points from the regression model to the grand mean from the empty model. C is the distance between data points and the grand mean from the empty model. " />

11\. The diagram above represents data points as orange dots and a red diagonal line as the regression model. Which distance would represent the **reduction in error** of the regression model compared to the empty model?

::::::::: { .choices }

- A
- [B]{ .correct }
- C
- None of these

:::::::::

::::::
:::
