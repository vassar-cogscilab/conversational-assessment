## 6.3 Variance

Sum of squares is a good measure of *total* variation in an outcome variable if we are using the mean as a model. But, it does have one important disadvantage.

Consider these distributions.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/DFW6CDLV.png" width=80% alt="A faceted histogram, with a histogram of the distribution of outcome within group 1 with the mean on the top, and a histogram of the distribution of outcome within group 2 with the mean at the bottom." /></p>

```
SS from Mean for distribution 1:  14
SS from Mean for distribution 2:  28
```

::: { .qti-item #b2_Variance_1 }
:::::: { #01022ebc-74e1-44e4-95d9-42524c412863 .qti-question .multiple-choice points="1" }

Which looks more spread out?

::::::::: { .choices }

- Distribution 1
- Distribution 2
- [They're the same.]{ .correct }

:::::::::

::::::

:::::: { #70fed6e2-16b3-498d-a03e-b029a8128dd8 .qti-question .multiple-choice points="1" }

Of the distributions above, which has the larger SS?

::::::::: { .choices }

- Distribution 1
- [Distribution 2]{ .correct }
- They're the same.

:::::::::

::::::
:::

Although you can see that the spread of the data points does not look different between the two distributions, the one on the bottom (#2) has a much larger SS.

Even worse, take a look at this pair of distributions.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/W2crnNgz.png" width=80% alt="A faceted histogram, with a histogram of the distribution of outcome within group 3 with the mean on the top, and a histogram of the distribution of outcome within group 4 with the mean at the bottom." /></p>

```
SS from Mean for distribution 3:  72
SS from Mean for distribution 4:  58
```

::: { .qti-item #b2_Variance_2 }
:::::: { #5c3687e1-4f73-4cfc-8081-9d880d18c574 .qti-question .multiple-choice points="1" }

Which looks more spread out?

::::::::: { .choices }

- Distribution 3
- [Distribution 4]{ .correct }
- They're the same.

:::::::::

::::::

:::::: { #0b582286-eeea-4b0d-aeee-dfe3e0f50398 .qti-question .multiple-choice points="1" }

Of the distributions above, for which do you think the mean would be a better model?

::::::::: { .choices }

- [Distribution 3]{ .correct }
- Distribution 4
- They're the same.

:::::::::

::::::

:::::: { #4476459d-d1fe-4420-8678-138be82102f2 .qti-question .essay points="1" max-words="100" }

Why is the SS so large for distribution 3, relative to distribution 4?

::::::
:::

Sum of squares works fine as a way to quantify error around the mean, and compare error across two distributions, but only when both distributions have the same sample size.

The reason for this is that each time you add another data point to the sample distribution, you are adding another squared deviation from the mean to the total SS. So even if two distributions appear to be equally well modeled by their respective means, they may have very different SS. SS always grows as the number of data points in the distribution gets larger, irrespective of the degree of spread.

::: { .qti-item #Ch6_Sum_7 }
:::::: { #1b392301-5ace-4837-a903-25b483138dec .qti-question .essay points="1" max-words="100" }

Can you think of a way to measure error that would not be influenced by sample size? Hint: What could you do to keep SS from growing each time you add another data point?

::::::
:::

This problem is solved by adding two new statistics to our toolbox: *variance* and *standard deviation*. To calculate variance, we start with SS, or total error, but then divide by the sample size to end up with a measure of *average error* around the mean—the average of the squared deviations.

**Because it is an average, variance is not impacted by sample size, and thus, can be used to compare the amount of error across two samples of different sizes**. You can think of it as a measure of average variation per sampled unit (e.g., students) in the dataset.

The formula for variance, usually represented as $s^2$, is this:

$$\frac{\sum_{i=1}^n (Y_i-\bar{Y})^2}{n-1}$$

::: { .qti-item #Ch6_Sum_8 }
:::::: { #0ba4fddc-1f72-4890-8f8a-a41aff834d77 .qti-question .essay points="1" max-words="100" }

Where is SS in the formula above?

::::::

:::::: { #a30699cf-12f3-484c-a7c8-b7cf4496da83 .qti-question .multiple-choice points="1" }

Is this a sample statistic or a population parameter?

::::::::: { .choices }

- [Sample statistic]{ .correct }
- Population parameter

:::::::::

::::::
:::

You can see that the numerator is the sum of squares. Although to get an actual average of squared deviations you would divide by n, we instead divide by n-1. We do this because dividing by n-1 gives us a better estimate of the true population variance, a fact that can be demonstrated by simulating multiple random samples from a population of known variance and then seeing which estimates are better – those obtained by dividing by n, or those obtained dividing by n-1.

There is, of course, a mathematical proof for this (for reference, here you can <a href="https://github.com/UCLATALL/czi-stats-course-files/raw/master/Book-1979.pdf" target="_blank">download mathematical proof for n-1 correction (PDF, 347KB)</a>). But we find it helpful to think about this way: when you take a small sample, the most extreme values in a population are unlikely to show up. So, if we divided by n it would, especially in smaller samples, slightly underestimate the true population variance. Dividing by n-1 corrects this bias, making the variance estimate a bit larger. And, as the sample gets larger, the difference between n and n-1 makes less and less difference.

The main thing to know is that taking the SS and dividing by n-1 results in something that approximates an *average squared deviation*.  (Also note: the n-1 you see in the denominator is sometimes called the degrees of freedom, or df. This will be more important later.)

::::::::: { .qti-item #Ch6_Sum_9 }
:::::: { #7ec0f77a-8bdf-4b2f-87b4-46107f9763ec .qti-question .association
points="1" }
In the image below, which is the visual definition of SS? Which is the visual
definition of variance?

::: {style="text-align: center;"}
![A scatterplot with Height on the x-axis and Thumb on the y-axis. A horizontal line runs through the mean of the data. A few of the data points are connected to the mean line with vertical lines and form a square for each of those data points.](https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch6_Sum_9_image.png){width=90%}
:::

::: associations

- [SS]{match="1"}
- [Variance]{match="5"}
:::
::: choices

1. The sum of the area of all the squares
2. The number of squares
3. The sum of the sides of the squares
4. The sum of the perimeters of the squares
5. The average area of the squares
:::
::::::
:::::::::

To calculate variance in R we can use the `var()` function. Here is how to calculate the variance of our `Thumb` data from `Fingers`.

```
var(Fingers$Thumb)
```

You can also find variance by running the `supernova()` function on the empty model. In the code window below, try using both the `var()` function and the `supernova()` function to calculate the variance of `Thumb` in the `Fingers` data frame.

```{ data-ckcode=true #B2_Code_Variance_01 }

%%% setup
require(coursekata)
empty_model <- lm(Thumb ~ NULL, data = Fingers)

%%% prompt
# this creates the empty_model
empty_model <- lm(Thumb ~ NULL, data = Fingers)

# calculate the variance of Thumb from the Fingers data frame
var()

# use supernova() on the empty_model to calculate variance
supernova()

%%% solution
# this creates the empty_model
empty_model <- lm(Thumb ~ NULL, data = Fingers)

# calculate the variance of Thumb from the Fingers data frame
var(Fingers$Thumb)

# use supernova() on the empty_model to calculate variance
supernova(empty_model)

%%% test
ex() %>% check_function("var") %>% check_result() %>% check_equal()
ex() %>% check_function("supernova") %>% check_result() %>% check_equal()
```

```
76.1551981994121
```

<pre><code>Analysis of Variance Table (Type III SS)
Model: Thumb ~ NULL

                               SS  df     MS   F PRE   p
----- ----------------- --------- --- ------ --- --- ---
Model (error reduced) |       --- ---    --- --- --- ---
Error (from model)    |       --- ---    --- --- --- ---
----- ----------------- --------- --- ------ --- --- ---
Total (empty model)   | 11880.211 156 <mark>76.155</mark>
</code></pre>

You can see that the variance of `Thumb` is the same, whether produced by the `var()` function or the `supernova()` function. In the ANOVA table, however, variance goes by a different name: MS. MS stands for Mean Square, as in the "mean of the sum of squares." If you divide the sum of squares (11880.211) by n-1 (156), you will also get the MS, or variance, of 76.155.

::: { .qti-item #Ch6_Sum_10 }
:::::: { #d4d336fd-82f3-41b3-8d8e-9575193f62be .qti-question .multiple-choice points="1" }

What is the correct interpretation of the value 76.1552?

::::::::: { .choices }

- There are about 76 thumbs that are larger than the mean.
- There are about 76 thumbs that are different from the mean.
- [The average squared deviation in this distribution is about 76 squared mm.]{ .correct }
- The average deviation in this distribution is about 76 mm.
- The average thumb in this distribution is about 76.

:::::::::

::::::
:::
