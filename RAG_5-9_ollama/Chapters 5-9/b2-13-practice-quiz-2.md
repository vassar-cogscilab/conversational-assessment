## 6.13 Chapter 6 Review Questions 2

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B2_Review2_01 }
:::::: { #a7e804d3-c39d-4b73-862e-8bff2864bcd2 .qti-question .multiple-choice points="1" }

1\. Below is the histogram for `WgtGain4`. What would you get if you were to total up the height (the "count") of all the bars?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/YMf7d6D4.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of WgtGain4 in FatMice18." />

::::::::: { .choices }

- [The number of mice in the `FatMice18` data frame]{ .correct }
- The sum of squares
- The total amount of weight gained in grams
- They would sum to 0

:::::::::

::::::
:::

::: { .qti-item #B2_Review2_02 }
:::::: { #81794146-71bf-4457-9179-f7f5ab43e47b .qti-question .multiple-choice points="1" }

2\. The histogram below shows the distribution of `WgtGain4` in the `FatMice18` data frame. Based on the sample we have, what is our best estimate for the likelihood of a mouse in a future study gaining more than 15 grams of weight?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/YMf7d6D4.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of WgtGain4 in FatMice18. Among all 18 data points, there is only one data point above 15." />

::::::::: { .choices }

- [1/18]{ .correct }
- More than two standard deviations
- 0.001
- 15/ `WgtGain4`

:::::::::

::::::::: { .feedback }

test

:::::::::

::::::
:::

::: { .qti-item #B2_Review2_03 }
:::::: { #77c14bb6-a1d9-45aa-b07b-361a1c7be41b .qti-question .multiple-choice points="1" }

3\. Consider the mouse who gained the least amount of weight in this study (circled in red in the jitter plot below). What is true about the residual of this mouse from the empty model?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/LRPg6W5r.png" class="lrn-image-center" width="500" height="333" alt="A jitter plot of the distribution of WgtGain4 by Light with a horizontal line showing the mean. Data points in LD condition are all below the mean, and data points in LL condition are all above the mean. The lowest point in LD condition is circled in red." />

::::::::: { .choices }

- The residual is large and positive.
- [The absolute value of the residual is relatively large.]{ .correct }
- Because this point is relatively far away, the residual is more variable.
- When a data point is much lower than the mean, the residual should be 0, because the residuals higher than the mean balance those that are lower than the mean.

:::::::::

::::::
:::

::: { .qti-item #B2_Review2_04 }
:::::: { #4e50b0d3-6473-434e-b545-b51fdbeb3295 .qti-question .multiple-choice points="1" }

4\. If you've calculated the variance for `WgtGain4`, what have you found?

::::::::: { .choices }

- Roughly the total squared residual from the empty model, in squared grams
- [Roughly the average squared residual from the empty model, in squared grams]{ .correct }
- Roughly the average residual from the empty model, in grams
- The sum of the residuals from the mean

:::::::::

::::::
:::

::: { .qti-item #B2_Review2_05 }
:::::: { #c481ad7e-465a-4783-a411-7f92a43a2163 .qti-question .multiple-choice points="1" }

5\. If the z score for a mouse's weight gain is -0.7, what does that mean?

::::::::: { .choices }

- The mouse's weight gain is 70% lower than the average mouse in the distribution.
- [The mouse's weight gain is 0.7 standard deviations lower than the mean of `WgtGain4`.]{ .correct }
- This mouse lost 0.7 grams of weight.
- The mouse's weight gain is lower than 70% of the entire sample.

:::::::::

::::::
:::

```{ data-ckcode=true #B2_Code_Review2_01  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B2_Review2_06 }
:::::: { #8c920488-94d1-4ad6-b559-541a86c64586 .qti-question .multiple-choice points="1" }

6\. Using the `FatMice18` data frame, run `favstats()` on `WgtGain4`. At what value would the sum of squared errors (sum of squares) be lowest?

::::::::: { .choices }

- 3
- [8.39]{ .correct }
- 0
- You can never be sure of the value at which the sum of squares would be lowest.

:::::::::

::::::
:::

```{ data-ckcode=true #B2_Code_Review2_02  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B2_Review2_07 }
:::::: { #8dfd32b1-32dc-4473-8648-3330e2ca6cc0 .qti-question .multiple-choice points="1" }

7\. Fit the NULL or empty model of `WgtGain4` in the `FatMice18` data frame. What is the sum of squares for this model?

::::::::: { .choices }

- [186.28]{ .correct }
- 17
- 10.957
- 0

:::::::::

::::::
:::

::: { .qti-item #B2_Review2_08 }
:::::: { #ca686a6e-e762-4d66-a72f-26e6eab60a11 .qti-question .multiple-choice points="1" }

You've just run the following code:

```
tally(~ WgtGain4 > 10, data = FatMice18, format="proportion")
```

You've gotten the following output:

```
WgtGain4 > 10
        TRUE     FALSE
0.2222222 0.7777778
```

8\. What can you now say?

::::::::: { .choices }

- Approximately 22% of mice gained more than 10 grams of weight.
- If another mouse were randomly selected and added to this data set, the likelihood that it would gain more than 10 grams would be 22%.
- [Both of the above]{ .correct }
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B2_Review2_09 }
:::::: { #0405828d-3696-43d9-b3b6-272b8d635515 .qti-question .multiple-choice points="1" }

9\. Let's say we want to compare the `Light` model for weight gain (WgtGain4 = Light + error) to the empty model (WgtGain4 = mean + error). What does the "mean" in the empty model word equation refer to?

::::::::: { .choices }

- [The mean of `WgtGain4` for all the mice]{ .correct }
- The mean of `WgtGain4` for the first `Light` condition
- The mean of `Light`
- The mean of the residuals

:::::::::

::::::
:::

::: { .qti-item #B2_Review2_10 }
:::::: { #437b4fff-0ff3-4ff2-82ed-605fefde27bb .qti-question .multiple-choice points="1" }

10\. If we add more mice to the study, which of these would certainly not be affected?

::::::::: { .choices }

- [$\beta_0$]{ .correct }
- $b_0$
- $\bar{Y}$
- $n$

:::::::::

::::::
:::

```{ data-ckcode=true #B2_Code_Review2_03  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B2_Review2_11 }
:::::: { #6a25221d-4e05-449b-b25a-5952efee3bf2 .qti-question .multiple-choice points="1" }

`StudentSurvey` is a data frame with 362 observations on the following 17 variables:

- `Year` Year in school
- `Gender` Student's gender: F or M
- `Smoke` Smokers? No or Yes
- `Award` Preferred award: Academy or Nobel or Olympic
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

11\. Using the `StudentSurvey` data frame, run `favstats` on `Siblings`. At what point would the sum of squared errors (sum of squares) be lowest?

::::::::: { .choices }

- 1
- [1.7]{ .correct }
- 0
- 2

:::::::::

::::::
:::
