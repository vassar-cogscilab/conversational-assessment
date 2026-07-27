## 7.11 Chapter 7 Review Questions

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B3_Review2_01 }
:::::: { #6b502907-9ebe-4550-85f6-9a4f68b726b1 .qti-question .multiple-choice points="1" }

The following set of questions is based on a data frame called `FatMice18`, which contains data for 18 mice. Mice were randomly assigned to one of two light treatments: LD (a normal light/dark cycle) or LL (light in the day and light at night as well). The researchers tracked the weight gained by each mouse (in grams) over four weeks of this light treatment.

The variables in the data frame are:

- `Light` Light treatment: LD = normal light/dark cycle or LL = bright light at night
- `WgtGain4` Weight gain in grams over a four week period
- `CageLoc` The location of the cage in the research lab (on the top row or bottom row)

Here's the result of running `head(FatMice18)`:

```
     Light WgtGain4    CageLoc
1    LL       10    top row
2    LL       10    top row
3    LL       11 bottom row
4    LL        9 bottom row
5    LL       12    top row
6    LL        9 bottom row
```

1\. If we run `lm()` to fit a model for `WgtGain4` that uses `Light` as an explanatory variable, how is error from the model calculated for each mouse?

::::::::: { .choices }

- The deviation of each mouse's `WgtGain4` from the Grand Mean of `WgtGain4`
- [The deviation of each mouse's `WgtGain4` from the mean `WgtGain4` for their `Light` group]{ .correct }
- The deviation of each `Light` group's mean to the Grand Mean of `WgtGain4`
- The deviation between the mean `WgtGain4` of the two `Light` groups

:::::::::

::::::
:::

::: { .qti-item #B3_Review2_02 }
:::::: { #32d9552d-e48d-431c-9b7d-422df34294c3 .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: WgtGain4 ~ Light

                              SS df      MS      F    PRE     p
----- --------------- | ------- -- ------- ------ ------ -----
Model (error reduced) | 112.500  1 112.500 24.398 0.6039 .0001
Error (from model)    |  73.778 16   4.611
----- --------------- | ------- -- ------- ------ ------ -----
Total (empty model)   | 186.278 17  10.95
```

2\. Above is the `supernova()` table for `Light_model`, which uses `Light` to explain variation in `WgtGain4`. What does the PRE of .60 mean?

::::::::: { .choices }

- There is a .60 chance that this explanatory variable helps us make better predictions of the outcome variable.
- [.60 of the sum of squares from the empty model is explained by the `Light` groups.]{ .correct }
- .60 of the sample has a relationship between `WgtGain4` and `Light` groups.
- .60 of the sum of squares from the `Light_model` is explained by the `Light` groups.

:::::::::

::::::
:::

::: { .qti-item #B3_Review2_04 }
:::::: { #6989ad73-1e7f-4158-b832-7bd5712758db .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: WgtGain4 ~ Light

                              SS df      MS      F    PRE     p
----- --------------- | ------- -- ------- ------ ------ -----
Model (error reduced) | 112.500  1 112.500 24.398 0.6039 .0001
Error (from model)    |  73.778 16   4.611
----- --------------- | ------- -- ------- ------ ------ -----
Total (empty model)   | 186.278 17  10.95

Coefficients:
(Intercept)      LightLL
     5.889        5.000
```

3\. Do these results show that light treatment (that is, being in the LL group) **causes** mice to eat more?

::::::::: { .choices }

- Yes, because the F statistic is quite large (around 24) and the PRE is also quite large.
- Yes, because this was an experimental design where mice were randomly assigned to two different light treatments.
- [No, because the experiment shows that light causes mice to gain more weight, but does not prove that their weight gain is caused by eating more.]{ .correct }
- No, because there may have been pre-existing differences between the mice (e.g., genetics, previous weight) that the experiment did not control for.

:::::::::

::::::::: { .feedback }

Test sample answer

:::::::::

::::::
:::

::: { .qti-item #B3_Review2_05 }
:::::: { #1585c35e-ea4f-4dcc-bca6-547141f9181d .qti-question .multiple-choice points="1" }

4\. Let's say we calculate the residuals from both the empty model and the complex model. What is similar about these two sets of residuals?

::::::::: { .choices }

- The values of the residuals from the empty model will be the same as the values of residuals from the complex model.
- [Both sets of residuals represent the difference between the data and the model's prediction.]{ .correct }
- Both sets of residuals represent the difference between the data and the Grand Mean.
- In both cases, the residuals can be reduced to near 0 simply by being careful with measurement and data entry.

:::::::::

::::::
:::

::: { .qti-item #B3_Review2_06 }
:::::: { #e78005e2-f917-465c-96bc-51b5cd7e8e53 .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: WgtGain4 ~ Light

                              SS df      MS      F    PRE     p
----- --------------- | ------- -- ------- ------ ------ -----
Model (error reduced) | 112.500  1 112.500 24.398 0.6039 .0001
Error (from model)    |  73.778 16   4.611
----- --------------- | ------- -- ------- ------ ------ -----
Total (empty model)   | 186.278 17  10.95
```

5\. Above is the supernova table for `Light_model`, which uses `Light` to explain variation in `WgtGain4`. Why does the table show a smaller sum of squares error (73.78) than sum of squares total (186.28)?

::::::::: { .choices }

- SS total should actually be smaller than the SS error. This must be an error in the code.
- [SS total is based on residuals from the Grand Mean. SS error is based on residuals left over after some of the total variation is explained by the difference in group means.]{ .correct }
- SS total depends on variation in the outcome variable (how much weight was gained). SS error depends on variation in the explanatory variable (whether the mouse is the LL or LD group).
- SS total is larger because the `Light` model it is calculated from is more complex. SS error is smaller because it is calculated from the more simple empty model.

:::::::::

::::::
:::

::: { .qti-item #B3_Review2_07 }
:::::: { #6948099b-5107-4bb7-a25f-c1020d66f473 .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: WgtGain4 ~ Light

                              SS df      MS      F    PRE     p
----- --------------- | ------- -- ------- ------ ------ -----
Model (error reduced) | 112.500  1 112.500 24.398 0.6039 .0001
Error (from model)    |  73.778 16   4.611
----- --------------- | ------- -- ------- ------ ------ -----
Total (empty model)   | 186.278 17  10.95

Analysis of Variance Table (Type III SS)
Model: WgtGain4 ~ CageLoc

                              SS df     MS     F    PRE     p
----- ----------------- ------- -- ------ ----- ------ -----
Model (error reduced) |  14.803  1 14.803 1.381 0.0795 .2571
Error (from model)    | 171.475 16 10.717
----- ----------------- ------- -- ------ ----- ------ -----
Total (empty model)   | 186.278 17 10.958
```

6\. Based on the two supernova tables above we would argue that `Light` (top table) explains more variation in `WgtGain4` than does `CageLoc` (the cage location, bottom table). What in the table would support this argument?

::::::::: { .choices }

- The relative sizes of PRE
- The relative sizes of SS Model
- [All of the above]{ .correct }

:::::::::

::::::
:::

```{ data-ckcode=true #B3_Code_Review2_01 data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B3_Review2_08 }
:::::: { #d3288cd4-74fd-4d19-9bfa-be7634c9107e .qti-question .multiple-choice points="1" }

7\. Using the `FatMice18` data frame, run `lm()` to fit the model for `WgtGain4`, using `Light` as an explanatory variable. If $Y_i=b_0+b_1X_i+e_i$ represents the fitted model, what is the value of $b_0$?

::::::::: { .choices }

- [5.889]{ .correct }
- 5.000
- Whether a mouse is in the LL group or not
- The number of mice in the LL group

:::::::::

::::::
:::

::: { .qti-item #B3_Review2_09 }
:::::: { #0b6adb48-aab3-4db3-9d87-490ed3f60049 .qti-question .multiple-choice points="1" }

```
                             SS df       MS     F    PRE     p
----- ----------------- ------- -- -------- ----- ------ -----
Model (error reduced) |  2638.1  1 2638.361          ?
Error (from model)    |  7845.3 80   98.079
----- ----------------- ------- -- -------- ------ ------ -----
Total (empty model)   | 10484.7 81  129.441
```

8\. Based on information in the `supernova()` table above, how would you calculate the approximate value of PRE?

::::::::: { .choices }

- [2638 divided by 10485]{ .correct }
- 2638 divided by 98
- 7846 divided by 10485
- Can't tell from the information given

:::::::::

::::::
:::

```{ data-ckcode=true #B3_Code_Review2_02 data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B3_Review2_10 }
:::::: { #c0584577-3e03-4bba-9636-ca5402b4068e .qti-question .multiple-choice points="1" }

`StudentSurvey` is a data frame with 362 observations on the following 17 variables:

- `Year` Year in school
- `Gender` Student's gender: F or M
- `Smoke` Smokers?  No or Yes
- `Award` Preferred award: Academy, Nobel, or Olympic
- `HigherSAT` Which SAT is higher? Math or Verbal
- `Exercise` Hours of exercise per week
- `TV` Hours of TV viewing per week
- `Height` Height (in inches)
- `Weight` Weight (in pounds)
- `Siblings` Number of Siblings
- `BirthOrder` Birth order, 1 = oldest
- `VerbalSAT` Verbal SAT score
- `MathSAT` Math SAT score
- `SAT` Combined Verbal + Math SAT
- `GPA` College grade point average
- `Pulse` Pulse rate (beats per minute)
- `Piercings` Number of body piercings

<span style="font-family:helvetica neue,helvetica,arial,sans-serif">9. Use `lm()` to explore the model that includes `Gender` to explain `Height` in the `StudentSurvey` data frame. How many inches must you add to the mean height for females to get the mean height for males?</span>

::::::::: { .choices }

- [5.151]{ .correct }
- 6.5695
- 4.783
- 6.112

:::::::::

::::::
:::

```{ data-ckcode=true #B3_Code_Review2_03 data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B3_Review2_11 }
:::::: { #4b18287a-4387-4c28-8170-ff53a01b69a4 .qti-question .multiple-choice points="1" }

10\. Again using `lm()` to explore the model that includes `Gender` to explain `Height` in the `StudentSurvey` data frame, what is the mean height for female?

::::::::: { .choices }

- 51.51
- [65.695]{ .correct }
- 70.846
- 63.896

:::::::::

::::::
:::

```{ data-ckcode=true #B3_Code_Review2_04 data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B3_Review2_12 }
:::::: { #c33a8558-601a-4825-8e88-71c3992d6237 .qti-question .multiple-choice points="1" }

11\. Fit a model using `Gender` to explain variation in `Piercings` and take a look at the parameter estimates. What would the model predict for a male student?

::::::::: { .choices }

- [The mean number of piercings for male is 0.171.]{ .correct }
- The mean number of piercings for male is 2.98 lower than the mean number of piercings for female.
- The error for male is 0.17.
- You should expect the next randomly chosen male to have 1.71 piercings.

:::::::::

::::::
:::

```{ data-ckcode=true #B3_Code_Review2_05 data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B3_Review2_13 }
:::::: { #920d815a-84e8-4d82-a0fe-db76ab5e77bd .qti-question .multiple-choice points="1" }

12\. Using the `StudentSurvey` data frame, run `favstats()` on `Siblings`. At what value would the sum of squared errors (sum of squares) be lowest?

::::::::: { .choices }

- 1
- [1.7]{ .correct }
- 0
- 2

:::::::::

::::::
:::
