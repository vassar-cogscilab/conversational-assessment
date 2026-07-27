## 6.12 Chapter 6 Review Questions

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B2_Review1_01 }
:::::: { #bb6d0587-cfdf-42d7-939b-6453e0dd2f26 .qti-question .multiple-choice points="1" }

1\. What is represented by the numbers on the y-axis of this histogram?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/MWNCM71s.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of hwy in mpg." />

::::::::: { .choices }

- Engine types
- Car brands
- Years that cars were made
- [Specific cars]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_02 }
:::::: { #64d4cbc9-6fba-48ae-8a99-360df4873387 .qti-question .multiple-choice points="1" }

The histogram below was created with this code: `gf_histogram(~ hwy, data = mpg, fill = "pink", bins = 10)` <img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/F95bY17y.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of hwy in mpg with 10 bins." />

2\. Why does this histogram look different than the one in the previous question?

::::::::: { .choices }

- Because there are fewer cars included in this histogram (i.e., only 10)
- Because the shape of the original distribution was not symmetrical
- [Because the values of `hwy` (i.e., highway miles per gallon) were put into fewer bins]{ .correct }
- Because the variables in this data frame were put into 10 bins

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_03 }
:::::: { #25ccfc4f-8409-4450-8a21-745e57a3d3c9 .qti-question .multiple-choice points="1" }

3\. Here we have depicted the mean as a vertical blue line. Why is the mean a good model for `hwy`?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/dvP3kXmK.png" class="lrn-image-center" width="500" height="333" alt="A density histogram of the distribution of hwy in mpg with a vertical line in blue showing the mean. " />

::::::::: { .choices }

- Because the mean is the only true statistical model that can represent a population parameter
- Because the mean is the best model whenever you make a visualization of data
- Because the mean is the best model for all categorical variables
- [Because the mean is a model that balances the residuals and minimizes the sum of squared residuals]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_04 }
:::::: { #a467fe59-f992-4036-8607-cd535314eedb .qti-question .multiple-choice points="1" }

4\. If a data point is very far away from the mean, what would you expect for the residual?

::::::::: { .choices }

- When farther away, the more positive the residual
- [When farther away, the larger the absolute value of the residual]{ .correct }
- When farther away, the more variable the residual
- When a data point is very far away from the mean, the residual should be 0, because the mean balances the residuals.

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_05 }
:::::: { #fd44c2b3-23bb-4508-9f4d-e1241e88e2ce .qti-question .multiple-choice points="1" }

5\. What's true of the distribution of any variable, if your model is the mean of that variable?

::::::::: { .choices }

- The distribution of the variable is more narrow than the distribution of its residual.
- The distribution of the variable is always centered on a number lower than the distribution of the residual is centered on.
- The distribution of the variable is always centered on 0, whereas the center of the distribution of its residual is unpredictable.
- [The distribution of the variable is the same shape as the distribution of its residual.]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_06 }
:::::: { #fb8507f7-348a-4a37-9122-c3e5d6b85a27 .qti-question .multiple-choice points="1" }

6\. If you ran the R code below, what would you be able to tell from the output?

```
empty_model <- lm(hwy ~ NULL, data = mpg)
empty_model
```

::::::::: { .choices }

- How much error there is around the empty model
- [The mean]{ .correct }
- $\beta_0$
- All of the above

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_07 }
:::::: { #99ebd560-7812-4d37-baa2-e05f170a2fdd .qti-question .multiple-choice points="1" }

7\. If you ran the R code below, what would you be able to tell from the output?

```
empty_model <- lm(hwy ~ NULL, data = mpg)
supernova(empty_model)
```

::::::::: { .choices }

- How much error there is around the empty model
- The sum of the squared residuals
- The sum of squares
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_08 }
:::::: { #26da3f95-9a31-45b3-a612-ea99b89b29b5 .qti-question .multiple-choice points="1" }

8\. The sum of squares gets larger as:

::::::::: { .choices }

- The variation increases
- The sample size increases
- The spread of the distribution increases
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_09 }
:::::: { #e3dce6f3-55c2-48a2-aa44-4ce2d12a7f1c .qti-question .multiple-choice points="1" }

9\. Let's say you've calculated the sum of squares for `hwy`. What would the advantage be of dividing that number by $n-1$ (i.e., dividing it by the $df$)?

::::::::: { .choices }

- It turns the sum of squares into a measure of spread.
- [You can use it to compare error across samples of different sizes.]{ .correct }
- You would have calculated the population variance.
- None of the above. There's no advantage of dividing $\mathit{SS}$ by the $\mathit{df}$.

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_10 }
:::::: { #625a3164-aa63-43b0-9880-d2d760400fb7 .qti-question .multiple-choice points="1" }

10\. Which of these lines of code will calculate the variance of `hwy`?

::::::::: { .choices }

- [`var(mpg$hwy)`]{ .correct }
- `lm(hwy ~ var, data = mpg)`
- `anova(mpg, data = hwy)`
- `favstats(~ hwy, data = hwy)`

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_11 }
:::::: { #5735f1e2-e010-4a40-89b0-5201538164e3 .qti-question .multiple-choice points="1" }

11\. What R code will output the standard deviation for `hwy`?

::::::::: { .choices }

- `sd(mpg$hwy)`
- `sqrt(var(mpg$hwy))`
- `favstats(~ hwy, data = mpg)`
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_12 }
:::::: { #8cff8ef3-233d-4662-b5f0-547cee9b4383 .qti-question .multiple-choice points="1" }

12\. If you've calculated the standard deviation for `hwy`, what have you found?

::::::::: { .choices }

- Roughly the total squared deviations from the mean, in squared highway miles per gallon
- Roughly the average squared deviation from the mean, in squared highway miles per gallon
- [Roughly the average deviation from the mean, in highway miles per gallon]{ .correct }
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_13 }
:::::: { #761baef3-89c4-4198-91c9-f336b4adf92b .qti-question .multiple-choice points="1" }

13\. Below is the histogram for `hwy`. What would you get if you were to total up the height (the "count") of all the bars?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/MWNCM71s.png" class="lrn-image-center" width="500" height="333" alt="A histogram of the distribution of hwy in mpg." />

::::::::: { .choices }

- [The total number of cars in the `mpg` data frame]{ .correct }
- The sum of squares
- The number of highway miles
- None of the above

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_14 }
:::::: { #ffc6cbe5-82d0-4ba5-92d7-6b808a2bfe32 .qti-question .multiple-choice points="1" }

14\. The mean of `hwy` is 23.44. If you wanted to calculate a z score for a `hwy` of 27, how would it be affected by the standard deviation for `hwy`?

::::::::: { .choices }

- If the standard deviation is large, the z score should also be very large and positive.
- If the standard deviation is large, the absolute z score should also be large but we won't be able to tell if it is positive or negative.
- [If the standard deviation is large, the z score should be small and positive.]{ .correct }
- Standard deviation and z are unrelated because they measure different things about the distribution.

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_15 }
:::::: { #95ec0b5e-2344-4070-b001-29173a79bf46 .qti-question .multiple-choice points="1" }

15\. If the z score for your friend's car's highway miles per gallon is found to be .6, what does that mean?

::::::::: { .choices }

- The car's highway miles per gallon is 60% better than the other cars in the distribution.
- [The car's highway miles per gallon is .6 standard deviations larger than the mean for `hwy`.]{ .correct }
- The car's highway miles per gallon is now smaller because .6 is smaller than 27.
- The car's highway miles per gallon should be a whole number (like in the Empirical Rule), which clearly suggests an error in the calculation.

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_16 }
:::::: { #68d8c10b-480a-4c7a-8b00-f3f73a8a211e .qti-question .multiple-choice points="1" }

16\. If we fit a normal curve on the distribution of `hwy` (see visualization below), what is it that we're modeling with it?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Vmw3C9V6.png" class="lrn-image-center" width="500" height="333" alt="A density histogram of the distribution of hwy in mpg with a vertical line in blue showing the mean and overlaid with a best-fitting normal curve." />

::::::::: { .choices }

- [Error around the model for `hwy`]{ .correct }
- The median
- The empty model for `hwy`
- Sample statistics

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_17 }
:::::: { #26c421b9-310b-426e-8872-7e35f9f11174 .qti-question .multiple-choice points="1" }

17\. In the figure below, which part represents the probability that a car would have a `hwy` above 29.4 (depicted in red)? Which part represents the z score for 29.4?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/NsZq2Wr2.png" class="lrn-image-center" width="500" height="333" alt="A density histogram of the distribution of hwy in mpg with a vertical line in blue showing the mean of 23.4, overlaid with a best-fitting normal curve, and with a vertical line in red showing hwy of 29.4. A is the area under the normal curve to the left of the mean. B is the area under the normal curve to the right of the mean and to the left of hwy of 29.4. C is the deviation from hwy of 29.4 to the mean. D is the area under the normal curve to the right of hwy of 29.4. " />

::::::::: { .choices }

- A; B
- D; B
- [D; C]{ .correct }
- C; A

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_18 }
:::::: { #51712f1c-0cff-4c9a-8a0b-75f5e11eb3ad .qti-question .multiple-choice points="1" }

18\. Below we have depicted the favstats and histogram for `hwy`. Using the Empirical Rule, estimate the probability that a car would have a `hwy` above 29.4 (depicted as a red dashed line).

```
min Q1 median Q3 max     mean       sd   n missing
 12 18     24 27  44 23.44017 5.954643 234       0
```

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Mw3jrdSc.png" class="lrn-image-center" width="500" height="333" alt="A density histogram of the distribution of hwy in mpg with a vertical line in blue showing the mean of 23.4, overlaid with a best-fitting normal curve, and with a vertical line in red showing hwy of 29.4. According to the favstats for hwy, Min is 12. Q1 is 18. Median is 24. Q3 is 27. Max is 44. Mean is 23.44017. Sd is 5.954643. N is 234. " />

Note: Although we have depicted the original data distribution in the histogram, you don't need to use the data. Just estimate the probability of a value greater than 29.4 based on a normal model of the distribution.

::::::::: { .choices }

- 5.95%
- [16%]{ .correct }
- 32%
- 68%

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_19 }
:::::: { #b36c3efa-3e31-435e-91e1-a682e064f83d .qti-question .multiple-choice points="1" }

19\. Below is a normal model of a population. There are more or less likely values of this variable. What part of the population would be considered "unlikely" to be randomly selected (according to the definition of "unlikely" agreed upon by the statistics community)?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/NgdZWbRM.png" class="lrn-image-center" width="500" height="333" alt="In a normal curve, A is the area within zone 1 (within 1 standard deviation from the mean). B is the area outside of zone 2 (outside 2 standard deviations from the mean). C is the extent on the x-axis between -3 and -4 standard deviations from the mean. D is a point at 2 standard deviations from the mean." />

::::::::: { .choices }

- A (shaded area below the normal model)
- [B (shaded areas below the normal model)]{ .correct }
- C (the length)
- D (the point)

:::::::::

::::::
:::

::: { .qti-item #B2_Review1_20 }
:::::: { #dc36d627-de4e-4de7-b4ae-056879258521 .qti-question .essay points="1" max-words="200" }

20\. What is the difference between a residual and the standard deviation?

::::::
:::
