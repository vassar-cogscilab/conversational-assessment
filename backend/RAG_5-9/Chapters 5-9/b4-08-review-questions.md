## 8.8 Chapter 8 Review Questions

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B3_Review1_01 }
:::::: { #6fb33278-555a-448e-a57e-90cbe1775edb .qti-question .multiple-choice points="1" }

Let's take a look at the number of hours spent exercising per week by this sample of students.

```
gf_histogram(~ Exercise, data = StudentSurvey, bins = 8)
```

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/mTmKz8hs.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of Exercise in StudentSurvey." />

1\. Why might the mean be a good simple model for this distribution?

::::::::: { .choices }

- Because the mean is the only statistically acceptable value of $b_0$.
- Because the mean is the most frequent value in this distribution.
- Because in all skewed distributions, the mean is the best model because it is different from the median.
- [Because the mean is a model that balances the deviations from the model and minimizes the sum of squared residuals.]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_02 }
:::::: { #7c44da40-6ec4-43e3-834b-37889db82794 .qti-question .multiple-choice points="1" }

2\. If we used this code to fit the empty model:

```
empty_model <- lm(Exercise ~ NULL, data = StudentSurvey)
```

And then used the `predict()` function to make a prediction for each student's number of hours exercised per week, what value would it predict for each student?

::::::::: { .choices }

- It would depend on how much they actually exercised.
- The value would be the mean number of hours exercised by that student that year and would vary for each student.
- [The value would be the mean number of hours exercised by this sample and would be the same for each student.]{ .correct }
- You would not be able to determine the value because it is represented by $b_0$.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_03 }
:::::: { #551498e3-1f7c-494e-8262-5bf08234549b .qti-question .multiple-choice points="1" }

3\. Having a low resting heart rate (recorded in the variable `Pulse`) is supposed to be an indicator of good cardiovascular health. Let's say we wanted to create three groups based on `Pulse`: low, medium, and high. Which of the following code would do that, and save the values in a new variable called `Pulse3Group`?

::::::::: { .choices }

- `Pulse3Group <- ntile(3)`
- [`StudentSurvey$Pulse3Group <- ntile(StudentSurvey$Pulse, 3)`]{ .correct }
- `StudentSurvey$Pulse3Group <- ntile(StudentSurvey$Pulse, 2)`
- `StudentSurvey <- ntile(StudentSurvey$Pulse3Group)`

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_04 }
:::::: { #25b199fa-58cc-4943-9b3e-fddf6d345a66 .qti-question .multiple-choice points="1" }

4\. Which of these options could be used to depict the relationship between `Exercise` and `Pulse3Group`?

::::::::: { .choices }

- `gf_boxplot(Exercise ~ Pulse3Group, data = StudentSurvey)`
- `gf_histogram(~ Exercise, data = StudentSurvey) %>% gf_facet_grid(Pulse3Group ~ .)`
- `gf_point(Exercise ~ Pulse3Group, data = StudentSurvey)`
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_05 }
:::::: { #bcc154f3-2246-44d5-aff1-a36749f8235d .qti-question .multiple-choice points="1" }

We are going to try and explain variation in `Exercise` hours with cardiovascular health (`Pulse3Group`).
Assume our model is the following:

> `Exercise` = `Pulse3Group` + other stuff

5\. If we write the model in GLM notation, which equation represents this `Pulse3Group` model?

::::::::: { .choices }

- $Y_i$ = $b_0$ + $e_i$
- $Y_i$ = $b_0$ + $b_1$$X_i$ + $e_i$
- [$Y_i$ = $b_0$ + $b_1X_{1i}$ + $b_2X_{2i}$ + $e_i$]{ .correct }
- $\text{Pulse3Group}_i$ = $b_0$ + $b_1\text{Exercise}_i$ + $e_i$

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_06 }
:::::: { #ac81475b-e8ab-4fdd-9aac-f9e83cd01178 .qti-question .multiple-choice points="1" }

We are going to try and explain variation in `Exercise` hours with cardiovascular health (`Pulse3Group`).
Assume our model is the following:

> `Exercise` = `Pulse3Group` + other stuff

6\. If we write the model in GLM notation, what does $Y_i$ represent?

::::::::: { .choices }

- [Each person's value for `Exercise`]{ .correct }
- The average `Exercise` for all participants
- The deviation between each person's `Exercise` and the average `Exercise` for all participants
- It might be any of the above, depending on which interpretation you're using.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_07 }
:::::: { #01beb7a3-edcb-4f77-9184-eb68f7e3c885 .qti-question .multiple-choice points="1" }

Here is a depiction of the relationship between `Exercise` and `Pulse3Group`.

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/X3hfJFnz.png" class="lrn-image-center" width="500" height="333" alt="A faceted histogram of the distribution of Exercise by Pulse3Group in StudentSurvey. " />

When `Pulse3Group` is included as an explanatory variable in our model of `Exercise`, we get this as the output of `lm(Exercise ~ Pulse3Group, data = StudentSurvey)`.

```
Call:
lm(formula = Exercise ~ Pulse3Group, data = StudentSurvey)

Coefficients:
        (Intercept)  Pulse3Groupmed    Pulse3Grouphigh
            10.3802         -0.8468            -3.1427
```

7\. Interpret the -3.14.

::::::::: { .choices }

- This is the number of people, on average, who have high pulse rates.
- [This represents the difference in average hours of exercise for people in the high pulse group relative to the low pulse group.]{ .correct }
- This represents the difference in average hours of exercise for people in the high pulse group relative to the medium pulse group.
- This represents the average hours of exercise per week for the high pulse group.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_08 }
:::::: { #9e72324d-114b-4302-bedb-a6ee64b06804 .qti-question .multiple-choice points="1" }

8\. In $Y_i = 10.38 - .85X_{1i} - 3.14X_{2i} + e_i$ what does $X_{1i}$ stand for?

::::::::: { .choices }

- [Whether someone is in the medium pulse group or not]{ .correct }
- The number of members in the medium pulse group
- The intercept for `Pulse3Groupmed`
- Whether someone is in the low or medium or high group

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_09 }
:::::: { #68df47ce-4006-40e4-a8b8-66fa9c919088 .qti-question .multiple-choice points="1" }

9\. When `Pulse3Group` is included in our model to explain variation in `Exercise`, how is error from this more complex model calculated?

::::::::: { .choices }

- The deviation of each person's `Exercise` from the Grand Mean for `Exercise`
- [The deviation of each person's `Exercise` from the mean `Exercise` of their `Pulse3Group`]{ .correct }
- The deviation of each `Pulse3Group`'s mean to the Grand Mean for `Exercise`
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_10 }
:::::: { #1d7cf70d-0bb6-4492-9868-174355ee7699 .qti-question .multiple-choice points="1" }

10\. When you add an explanatory variable to your model, what should be the effect on the Sum of Squares from the empty model?

::::::::: { .choices }

- [It should remain unchanged.]{ .correct }
- It should go up.
- It should go down.
- It depends on how much variation is accounted for by the explanatory variable.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_11 }
:::::: { #717f6d2a-070d-413b-9196-bebe531cf366 .qti-question .multiple-choice points="1" }

11\. If we express our model as $Y_i$ = $b_0$ + $b_1X_{1i}$ + $b_2X_{2i}$ + $e_i$ which part represents the model's prediction for `Exercise`?

::::::::: { .choices }

- $Y_i$
- $b_0$
- [$b_0$ + $b_1X_{1i}$ + $b_2X_{2i}$]{ .correct }
- $b_1X_{1i}$

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_12 }
:::::: { #86f085ef-f92f-4a4b-91e5-b6c5e0f673dd .qti-question .multiple-choice points="1" }

12\. We can calculate the residuals from both the empty model and the complex model. What is similar about these two sets of residuals?

::::::::: { .choices }

- The values of the residuals from the empty model will be the same as the values of the residuals from the complex model.
- [The residuals represent the difference between the data and the model's prediction.]{ .correct }
- The residuals represent the difference between the data and the Grand Mean.
- In both cases, the residuals can be reduced to near 0 simply by being careful with measurement and data entry.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_13 }
:::::: { #1067d9fb-022b-46ad-9fb3-702b3ff1166a .qti-question .multiple-choice points="1" }

13\. Imagine that you've calculated SS for both the empty model and the complex model for `Exercise`. What will be true about these SS?

::::::::: { .choices }

- [SS leftover from the empty model will be greater than the SS leftover from the complex model.]{ .correct }
- SS leftover from the empty model will be smaller than the SS leftover from the complex model.
- SS leftover from the empty model will be equal to the SS leftover from the complex model.
- In both cases the SS will be 0 because the residuals are balanced by the mean.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_14 }
:::::: { #bea733f5-2d94-4c23-b2a5-8e133fd787c4 .qti-question .multiple-choice points="1" }

We can calculate the residuals from the complex model and the mean residuals for the three groups with this code.

```
StudentSurvey$Residuals <- resid(Pulse3Group_model)
mean(Residuals ~ Pulse3Group, data = StudentSurvey)
```

Here is the output:

```
          low           med          high
-3.938696e-16  1.064014e-15 -1.234220e-15
```

14\. Have you done something wrong in R?

::::::::: { .choices }

- Yes! This looks wrong.
- [No. Means always balance residuals.]{ .correct }
- No. That's how we know we have a three-parameter model.
- Maybe. This outcome is very rare and it's worth checking the R code you used.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_15 }
:::::: { #a40c9dcc-0439-47b0-8641-966a2eb16109 .qti-question .multiple-choice points="1" }

15\. Imagine that you have both the empty model for `Exercise` and the complex model for `Exercise` (i.e., the model that includes `Pulse3Group`). What would you do if you wanted to compare how well they predict `Exercise`?

::::::::: { .choices }

- Compare the SS from each model
- Look at the reduction in error in the `Pulse3Group` model
- Examine the PRE
- [Any of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_16 }
:::::: { #014dfd77-54bf-4e66-814f-01586ef4da40 .qti-question .multiple-choice points="1" }

Here is the supernova table for `Pulse3Group_model.`

```
Analysis of Variance Table (Type III SS)
Model: Exercise ~ Pulse3Group

                            SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   594.286   1 594.286 18.931 0.0501 .0000
Error (from model)    | 11269.910 359  31.393
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11864.197 360  32.956
```

16\. Interpret the PRE.

::::::::: { .choices }

- There is a .05 chance that we have made a truly explanatory model.
- [.05 of the total variation in exercise hours is explained by the pulse groups.]{ .correct }
- .05 of the sample has a relationship between exercise hours and pulse groups.
- .05 of the complex model's sum of squares can be explained by `Pulse3Group`.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_17 }
:::::: { #efa214cf-01fb-462e-a26f-f2ced18b0a41 .qti-question .multiple-choice points="1" }

17\. Does this analysis prove that cardiovascular health (that is, being in a lower pulse group) **causes** students to exercise more?

::::::::: { .choices }

- Yes, because the F statistic is quite large (around 18.9), and the PRE is reasonable.
- Yes, because we have discovered the best fitting parameter estimates.
- No, this analysis actually shows that exercising more causes lower pulse rates.
- [No, you cannot prove causation from a correlational study design]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_18 }
:::::: { #eb2a58f0-c4ce-479b-98a0-d69c12051ec3 .qti-question .multiple-choice points="1" }

We were interested in whether the pulse groups also explain some of the variation we see in students' number of piercings.  Here is the supernova table for that model.

```
Analysis of Variance Table (Type III SS)
Model: Piercings ~ Pulse3Group

                            SS  df     MS     F    PRE     p
----- --------------- | -------- --- ------ ----- ------ -----
Model (error reduced) |   28.704   1 28.704 6.168 0.0169 .0135
Error (from model)    | 1670.725 359  4.654
----- --------------- | -------- --- ------ ----- ------ -----
Total (empty model)   | 1699.429 360  4.721
```

18\. Why does this table have a smaller Sum of Squares Total (1699) than the supernova table for `Exercise` explained by `Pulse3Group` (11864)?

::::::::: { .choices }

- The SS Total should never change. This must be an error in the code.
- [The SS Total depends on the variation in the outcome variable. `Piercings` is a different outcome variable so it has a different SS Total.]{ .correct }
- The SS Total depends on the variation in the explanatory variable. `Piercings` is a different explanatory variable so it has a different SS Total.
- The SS Total is always uniquely different. We should never expect it to be the same value.

:::::::::

::::::
:::

::: { .qti-item #B3_Review1_19 }
:::::: { #69046431-e2a4-42a3-a207-d7ebc6297ca4 .qti-question .essay points="1" max-words="100" }

19\. Take a look at the two supernova tables below. Based on these tables, we could argue that `Pulse3Group` explains more of the variation in `Exercise` than in `Piercings`. Explain why we would argue that in the space below.

```
Analysis of Variance Table (Type III SS)
Model: Exercise ~ Pulse3Group

                            SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   594.286   1 594.286 18.931 0.0501 .0000
Error (from model)    | 11269.910 359  31.393
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11864.197 360  32.956
```

```
Analysis of Variance Table (Type III SS)
Model: Piercings ~ Pulse3Group

                            SS  df     MS     F    PRE     p
----- --------------- | -------- --- ------ ----- ------ -----
Model (error reduced) |   28.704   1 28.704 6.168 0.0169 .0135
Error (from model)    | 1670.725 359  4.654
----- --------------- | -------- --- ------ ----- ------ -----
Total (empty model)   | 1699.429 360  4.721
```

::::::
:::

::: { .qti-item #B3_Review1_20 }
:::::: { #3e6640eb-48f0-40a6-b2f3-4a9e25e169f1 .qti-question .essay points="1" max-words="100" }

20\. Could we use sum of squares to argue that `Pulse3Group` explains more variation in `Exercise` than in `Piercings`?  Why or why not?

```
Analysis of Variance Table (Type III SS)
Model: Exercise ~ Pulse3Group

                            SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   594.286   1 594.286 18.931 0.0501 .0000
Error (from model)    | 11269.910 359  31.393
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11864.197 360  32.956
```

```
Analysis of Variance Table (Type III SS)
Model: Piercings ~ Pulse3Group

                            SS  df     MS     F    PRE     p
----- --------------- | -------- --- ------ ----- ------ -----
Model (error reduced) |   28.704   1 28.704 6.168 0.0169 .0135
Error (from model)    | 1670.725 359  4.654
----- --------------- | -------- --- ------ ----- ------ -----
Total (empty model)   | 1699.429 360  4.721
```

::::::
:::
