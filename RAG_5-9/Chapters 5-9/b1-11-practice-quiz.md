## 5.11 Chapter 5 Review Questions

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B1_Review1_01 }
:::::: { #50043d58-2540-4c44-b94d-6c9d6070dc77 .qti-question .multiple-choice points="1" }

1\. What is the observational unit in this data frame?

::::::::: { .choices }

- Rows
- [Bike commutes]{ .correct }
- Bikers
- Bikes

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_02 }
:::::: { #faab4c4c-1158-4df1-a5b6-922fff4ea972 .qti-question .multiple-choice points="1" }

2\. Let's say we wanted to write a word equation to explain the variation in the time it takes to bike to work. We think that the `Distance` of a person's commute is an important explanatory variable.  What would the word equation look like?

::::::::: { .choices }

- [**Time** = **Distance** + other stuff]{ .correct }
- **Distance** = **Time** + other stuff
- Other stuff = **Distance** + **Time**
- Model = **Time** + **Distance**

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_03 }
:::::: { #a60e3738-2048-43c9-8751-97bdf8e0bf4d .qti-question .multiple-choice points="1" }

3\. The average `Distance` of this person's bike commute is just over 27 miles. Imagine that you've discovered that one of your observations has been recorded incorrectly. Instead of a distance of around 27 miles, the distance for one of the commute has been entered as 54 miles! You make the correction to your data frame. How will the correction affect the mean?

::::::::: { .choices }

- The mean will be unaffected by the correction.
- The mean will be higher because of the correction.
- [The mean will be lower because of the correction.]{ .correct }
- It's impossible to say how the mean will be affected by the correction.

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_04 }
:::::: { #6a2cdb56-5495-4801-9d1c-82c05f9acc43 .qti-question .multiple-choice points="1" }

4\. How might you expect this correction (changing 54 back to 27) to affect the mean and the median?

::::::::: { .choices }

- Both the mean and median will be equally affected by this correction.
- The median will most likely be affected more than will the mean.
- [The median will most likely be affected less than will the mean.]{ .correct }
- It's impossible to say how the median will be affected by the correction.

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_05 }
:::::: { #74f67f22-0c41-473a-896d-0e81eb1d9930 .qti-question .multiple-choice points="1" }

5\. How would you create a plot to look at the distribution of `Distance`?

::::::::: { .choices }

- `gf_plot(~ Distance$BikeCommute)`
- `gf_histogram(~ Distance)`
- `gf_histogram(BikeCommute, Distance)`
- [`gf_histogram(~ Distance, data = BikeCommute)`]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_06 }
:::::: { #9f750bea-58c0-4d50-b8c0-91ee9e7df497 .qti-question .multiple-choice points="1" }

6\. Why is the mean a good model for this distribution?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ws288d2s.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of Distance in BikeCommute. " />

::::::::: { .choices }

- [Because the mean balances the deviations above and below the mean.]{ .correct }
- Because the mean balances the number of values above and below the mean.
- Because the mean is the midpoint of the range.
- All of the above are reasons why the mean is a good model.

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_07 }
:::::: { #41d14397-1ca2-4eef-ac8b-d8f564774632 .qti-question .multiple-choice points="1" }

7\. This bike rider has an intuition that the kind of bike he uses affects the top speed he can reach on the bike. To get a sense of the distribution of top speed, he looks at the output. Which function created this output?

```
  min   Q1 median      Q3 max     mean       sd  n missing
29.58 32.4  33.59 34.7425  36 33.55571 1.478628 56       0
```

::::::::: { .choices }

- [`favstats()`]{ .correct }
- `tally()`
- `arrange()`
- `head()`

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_08 }
:::::: { #ca6e2216-668b-44ea-8c43-6f14b7ce2472 .qti-question .multiple-choice points="1" }

8\. Below is a histogram for `TopSpeed`. What R code created the line that indicates the mean?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/sVKgW0TV.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of TopSpeed in BikeCommute with a vertical line in blue showing the mean. " />

::::::::: { .choices }

- [`gf_vline(xintercept = 33.6, color = "blue")`]{ .correct }
- `gf_mean(mean = 33.6, color = "blue")`
- `gf_mean(33.6, color = "blue")`
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_09 }
:::::: { #e6503f3d-8a91-495c-84ab-6e0049c03dc6 .qti-question .multiple-choice points="1" }

9\. Which of the following statements are true about the empty model of `TopSpeed`?

::::::::: { .choices }

- The model would be the best way of explaining how many variables contribute to `TopSpeed` (such as time of year and type of bike).
- [The model would include only the mean of `TopSpeed`.]{ .correct }
- The model would predict a different `TopSpeed` depending on the situation.
- None of the above.

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_10 }
:::::: { #d6a8cdf8-6ae7-4832-b29b-fbe8aa0ca6e6 .qti-question .multiple-choice points="1" }

10\. What R code would you use to fit the empty model for `TopSpeed`?

::::::::: { .choices }

- `gf_histogram(NULL ~ TopSpeed, data = BikeCommute)`
- `NULL(TopSpeed, data = BikeCommute)`
- [`lm(TopSpeed ~ NULL, data = BikeCommute)`]{ .correct }
- `gf(TopSpeed ~ NULL, data = BikeCommute)`

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_11 }
:::::: { #7ca9cb35-8b8c-49bc-8688-7902626aa882 .qti-question .multiple-choice points="1" }

11\. If the mean for `TopSpeed` is 33.6, what will the empty model predict for each observation's `TopSpeed`?

::::::::: { .choices }

- A value within one quarter of 33.6
- 0
- [33.6]{ .correct }
- It's impossible to say

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_12 }
:::::: { #67293cef-9c03-43fc-8686-1e6924b424c2 .qti-question .multiple-choice points="1" }

12\. Consider the idea that DATA = MODEL + ERROR. If the mean of `TopSpeed` is 33.6 and a given observation has a `TopSpeed` of 23.6, what is the data?

::::::::: { .choices }

- -10
- 33.6
- 57.2
- [23.6]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_13 }
:::::: { #fa160cc1-8cb2-482c-9b96-f741f0d008a2 .qti-question .multiple-choice points="1" }

13\. If the mean of `TopSpeed` is 33.6 and a given observation has a `TopSpeed` of 23.6, what is the residual?

::::::::: { .choices }

- [-10]{ .correct }
- 33.6
- 57.2
- 23.6

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_14 }
:::::: { #89e08747-ce19-4d2a-a4f6-f6356528b67f .qti-question .multiple-choice points="1" }

14\. Imagine you make three histograms: one for `TopSpeed`, one for the predicted values based on the empty model for `TopSpeed`, and one for the residuals. Which two distributions will have a similar shape?

::::::::: { .choices }

- `TopSpeed` and the predicted values
- [`TopSpeed` and residuals]{ .correct }
- Predicted values and residuals
- No two of these distributions will have a similar shape.

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_15 }
:::::: { #d3cae3d9-1989-4272-9d45-687347dad549 .qti-question .multiple-choice points="1" }

15\. The mean of `TopSpeed` is 33.6 and a given observation has a `TopSpeed` of 23.6. What part of this GLM notation represents 23.6?

$Y_i=\overline{Y}+e_i$

::::::::: { .choices }

- [$Y_i$]{ .correct }
- $\overline{Y}$
- $e_i$
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_16 }
:::::: { #b33c8a87-95ad-4310-9007-b372d9733302 .qti-question .multiple-choice points="1" }

16\. In GLM notation, which of the following represents the model (or prediction)?

::::::::: { .choices }

- $Y_i$
- [$b_0$]{ .correct }
- $e_i$
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_17 }
:::::: { #3e5a08e0-e0b5-4535-a4d3-cde497abf22d .qti-question .multiple-choice points="1" }

17\. What notation <u>cannot</u> be used to represent the mean of the sample?

::::::::: { .choices }

- $Y_i$
- $\beta_0$
- $\mu$
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_18 }
:::::: { #ec9de2ad-e63e-4360-8060-aaf4aa667a02 .qti-question .multiple-choice points="1" }

18\. What notation <u>can</u> be used to represent the mean of the population?

::::::::: { .choices }

- $\beta_0$
- $\mu$
- [Both of the above]{ .correct }
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B1_Review1_19 }
:::::: { #325e9de4-6789-40c0-b127-80448872d71b .qti-question .essay points="1" max-words="100" }

19\. What is the "population" that the `TopSpeed` empty model is trying to understand?

::::::
:::

::: { .qti-item #B1_Review1_20 }
:::::: { #2b43dc9d-83fe-40a1-ab3a-d04493b3d363 .qti-question .essay points="1" max-words="200" }

20\. Which of these variables—`Bike`, `Distance`, or `Month`—do you think would help explain the variation we see in `TopSpeed`? Create a word equation and describe the plot you would make. Explain what you would look for in your plot that would show that this variable does indeed explain some of the variation in `TopSpeed`.

::::::
:::
