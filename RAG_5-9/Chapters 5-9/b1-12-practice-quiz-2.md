## 5.12 Chapter 5 Review Questions 2

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B1_Review2_01 }
:::::: { #59f08547-1391-42b1-8a73-4787e786f72d .qti-question .multiple-choice points="1" }

1\. Even in this highly skewed distribution, the mean can be a good model. What makes the mean a good model?

<img src="https://i.postimg.cc/NQ78rBTZ/image.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of Alcohol in NutritionStudy." />

::::::::: { .choices }

- [The mean balances the deviation above and below the mean.]{ .correct }
- The mean balances the number of values above and below the mean.
- The mean is the most common number in this distribution.
- All of the above are reasons why the mean is a good model.

:::::::::

::::::
:::

```{ data-ckcode=true #B1_Code_Review2_01  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B1_Review2_02 }
:::::: { #8fd51693-1bc5-4b00-a0f9-58223f508695 .qti-question .multiple-choice points="1" }

2\. Using the `NutritionStudy` data frame, make a histogram of `Alcohol`. What is represented on the y-axis?

::::::::: { .choices }

- Number of drinks consumed per week
- [Number of patients]{ .correct }
- The count of alcoholic drinks
- Number of variables

:::::::::

::::::
:::

::: { .qti-item #B1_Review2_03 }
:::::: { #1000efec-6b86-40af-aa24-7ea2e7599dce .qti-question .multiple-choice points="1" }

```
min Q1 median  Q3 max     mean       sd   n missing
  0  0    0.3 3.2 203 3.279365 12.32288 315       0
```

3\. Above are the favstats for `Alcohol`. The average number of drinks per week is 3.28 but the median is 0.3. The maximum value in this distribution is 203—that is a lot of alcoholic drinks per week (almost 30 per day)! That seems to be a mistake. Which of the following would change more if we were to exclude the maximum value from the analysis?

::::::::: { .choices }

- The median
- The minimum
- [The mean]{ .correct }
- All of these values (median, minimum, and mean) will change a lot.

:::::::::

::::::
:::

::: { .qti-item #B1_Review2_04 }
:::::: { #724e80b4-39e3-4af5-bd1e-11bdef6c66a3 .qti-question .multiple-choice points="1" }

4\. Which of the following word equations represents the hypothesis that smoking explains some of the variation in fat consumption.

::::::::: { .choices }

- Smoking = Fat consumption
- Fat consumption = Smoking
- Smoking = Fat consumption + other stuff
- [Fat consumption = Smoking + other stuff]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B1_Review2_05 }
:::::: { #73a4cf70-866d-4726-bc56-160c1864b1e7 .qti-question .multiple-choice points="1" }

5\. What would be true about the empty model for `Fat`?

::::::::: { .choices }

- The model would be the best way of explaining how many variables contribute to `Fat` (such as smoking status and gender).
- [The model would make the same prediction (the mean of `Fat`) for every person regardless of their values on other variables.]{ .correct }
- The model would predict a different value for `Fat` for each person, depending on their values on other variables.
- The model would predict 0 grams for every person's value on `Fat`.

:::::::::

::::::
:::

::: { .qti-item #B1_Review2_06 }
:::::: { #6c0f7c2e-c3d9-4277-84a2-4f70d6e74df4 .qti-question .multiple-choice points="1" }

6\. The mean of `Alcohol` is 3.279 drinks per week. A particular patient consumes 2 drinks per week. Which of the following symbols would be used to represent the value 2 in the notation of the General Linear Modal?

::::::::: { .choices }

- [$Y_i$]{ .correct }
- $b_0$
- $e_i$
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B1_Review2_07 }
:::::: { #e1bf689f-9e8c-4ebf-be48-81c99f9946f5 .qti-question .multiple-choice points="1" }

7\. The mean of `Alcohol` is 3.279 per week. A particular patient consumes 2 drinks per week. Which of the following represents the residual for this patient under the empty model?

::::::::: { .choices }

- $Y_i-b_0$
- 2 - 3.279
- $e_i$
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B1_Review2_08 }
:::::: { #734aa235-5093-4e79-bef5-ffddeeb80434 .qti-question .multiple-choice points="1" }

8\. Which of the following cannot be calculated from the `NutritionStudy` data set?

::::::::: { .choices }

- An estimate
- [A parameter]{ .correct }
- A statistic
- A simple model

:::::::::

::::::
:::

```{ data-ckcode=true #B1_Code_Review2_02  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B1_Review2_09 }
:::::: { #e712aebc-9761-4627-81b6-39aa6955b49f .qti-question .multiple-choice points="1" }

9\. Use `lm()` to fit the empty model for `Fat` in the `NutritionStudy` data frame. What is the coefficient?

::::::::: { .choices }

- [77.03]{ .correct }
- 57.0
- 65.12
- None of the above

:::::::::

::::::
:::

```{ data-ckcode=true #B1_Code_Review2_03  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B1_Review2_10 }
:::::: { #b0b8cbef-d4ce-4fde-9259-7fe77b09f9e4 .qti-question .multiple-choice points="1" }

10\. Use `lm()` to fit the empty model for `TV` in the `StudentSurvey` data frame. What can you say based on the output?

::::::::: { .choices }

- The mean of the distribution of hours spent viewing TV by students in this data frame is 6.504.
- The best-fitting number for the empty model is 6.504.
- 6.504 is an unbiased estimate.
- [All of the above]{ .correct }

:::::::::

::::::
:::

```{ data-ckcode=true #B1_Code_Review2_04  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B1_Review2_11 }
:::::: { #8ab913f9-83b2-482b-a461-85d2e36106ae .qti-question .multiple-choice points="1" }

11\. Take the `StudentSurvey` data frame and use `lm()` to fit the empty model for `GPA`. Save the results in an R object `empty_model_GPA`. What do you get when you run `empty_model_GPA` in R?

::::::::: { .choices }

- The "intercept"
- 3.158
- The mean for GPA
- [All of the above]{ .correct }

:::::::::

::::::
:::

```{ data-ckcode=true #B1_Code_Review2_05  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B1_Review2_12 }
:::::: { #af99e9ef-e8c4-4078-9f04-67f4099892cd .qti-question .multiple-choice points="1" }

12\. If you print the residuals for `empty_model_GPA`, what will you see?

::::::::: { .choices }

- 3.158
- [For each participant in the study, the difference between his/her GPA and the mean GPA]{ .correct }
- For each participant in the study, the model (that is, the mean) for GPA
- The GPA of each participant in the study

:::::::::

::::::
:::

```{ data-ckcode=true #B1_Code_Review2_06  data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B1_Review2_13 }
:::::: { #cdf519f5-fb00-41f4-88c7-d173e27acdef .qti-question .multiple-choice points="1" }

13\. Using the `StudentSurvey` data frame, create a faceted histogram for `Weight` by `Gender`. The group mean by gender is likely to be a better model for which gender?

::::::::: { .choices }

- Males
- [Females]{ .correct }
- The mean is an equally good model for males and females.
- A histogram cannot be used to answer this question.

:::::::::

::::::
:::

```{ data-ckcode=true #B1_Code_Review2_07 data-submittable=false }
%%% setup
require(coursekata)

%%% prompt
# run your code here

```

::: { .qti-item #B1_Review2_14 }
:::::: { #48e50b95-44dc-46c8-86c4-0af95c297258 .qti-question .multiple-choice points="1" }

14\. Take the `StudentSurvey` data frame and use `lm()` to fit the empty model for `SAT`. What is 1204?

::::::::: { .choices }

- An unbiased estimate of SAT
- The estimate of SAT that has the least error
- The mean SAT score
- [All of the above]{ .correct }

:::::::::

::::::
:::
