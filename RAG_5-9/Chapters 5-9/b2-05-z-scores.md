## 6.5 Z-Scores

We have looked at the mean as a model; and we have learned some ways to quantify total error around the mean, as well as some good reasons for doing so. But there is another reason to look at both mean and error together. Sometimes, by putting the two ideas together it can give us a better way of understanding where a particular score falls in a distribution.

A student (let’s call her Zelda) has a thumb length of 65.1 mm. What does this mean? Is that a particularly long thumb? How can we know? By now you may be getting the idea that just knowing the length of one thumb doesn’t tell you very much.

To interpret the meaning of a single score, it helps to know something about the distribution the score came from. Specifically, we need to know something about its shape, center and spread.

::: { .qti-item #Ch6_Z-1 }
:::::: { #45bd9bc3-5325-470e-8dbe-0e579b501eb6 .qti-question .multiple-choice points="1" }

What if, in addition to knowing Zelda's thumb length is 65.1 mm, we know also that the mean of the distribution of thumb lengths is 60.1 mm? What does this tell us that we didn't know before we knew the mean?

::::::::: { .choices }

- We now know how long this thumb is relative to the other thumbs in our sample.
- We now know how long this thumb is relative to other long thumbs.
- We now know that this is one of the longest thumbs in our sample.
- [We now know that this thumb is longer than average and that's about it.]{ .correct }

:::::::::

::::::
:::

We know that this student’s thumb is about 5 mm longer than the average. But because we have no idea about the spread of the distribution, we still don’t have a very clear idea of how to judge 65.1 mm thumb length. Is a 5 mm distance still pretty close to the mean, or is it far away? It’s hard to tell without knowing what the range of thumb lengths looks like.

::: { .qti-item #Ch6_Z_2 }
:::::: { #762df14f-b155-43a1-ae12-0c42dfa3f73d .qti-question .multiple-choice points="1" }

Which of these measures of spread might be most useful in measuring how far 65.1 mm is from the mean?

::::::::: { .choices }

- SS, total squared error: 11880.21
- Variance, average squared error: 76.1552
- [Standard Deviation, average error: 8.726695]{ .correct }

:::::::::

::::::
:::

Although SS will be really useful later, for this purpose it stinks. 65.1 and 11,880 don’t seem like they belong in the same universe! Variance will also be useful, but its units are still somewhat hard to interpret. It’s hard to use squared millimeters as a unit when trying to make sense of unsquared millimeters.

Standard deviation, on the other hand, is really useful. We know that Zelda’s thumb is about 5 mm longer than the average thumb. But now we also know that, on average, thumbs are 8.7 mm away from the mean, both above and below.  Although Zelda’s thumb is above average in length, it is definitely not one of the longest thumbs in the distribution. Check out the histogram below to see if this interpretation is supported.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/NYydpxzz.png" width=80% alt="A density histogram of the distribution of Thumb with a vertical line in blue indicating the mean of 60.2 mm, and another vertical line in red indicating Zelda’s thumb of 65.1 mm." /></p>

The mean of thumb length is shown in blue, and Zelda’s 65.1 mm thumb is shown in red.

### Combining Mean and Standard Deviation

In the `Thumb` situation, we find it valuable to coordinate both mean and standard deviation in order to interpret the meaning of an individual score. **Now, let’s introduce a measure that will combine these two pieces of information into a single score: the ****_z-score_****.**

::: { .qti-item #Ch6_Combining_1 }
:::::: { #34d7a75a-948e-4101-96ae-dc46e23a66d2 .qti-question .essay points="1" max-words="100" }

Say you have a video game called Kargle. A friend of yours says that their high score is 37,000 points. Is that a good score? How do you know?  What else would you want to know to answer this question?

::::::
:::

Let’s say you know that the mean score across all players of the game is 35,000. How would that help you? Clearly it would help. You would know that the score of 37,000 is above the average by 2,000 points. But even though it helps you interpret the meaning of the 37,000, it’s not enough. What it doesn’t tell you is how _far above the average_ 37,000 points is _in relation to the whole distribution_.

::: { .qti-item #Ch6_Combining_2 }
:::::: { #c2968c42-fe05-460f-98df-3007f99f2d0a .qti-question .essay points="1" max-words="100" }

What is similar about 37,000 points in the Kargle situation and 65.1 mm in the `Thumb` situation?

::::::
:::

Let’s say the distribution of scores on Kargle is represented by one of these histograms. Both distributions have an average score of 35,000. But in the distribution on the top (#1), the standard deviation is 1,000 points, while on the bottom (#2) the standard deviation is 5,000 points. The blue line depicts the mean, and the red line depicts our friend’s score of 37,000.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/TR2wrxxM.png" width=80% alt="A histogram of the distribution of score on the top with a vertical line in blue indicating the mean, and another vertical line in red indicating our friend’s score. A histogram of the distribution of score on the bottom with a vertical line in blue indicating the mean, and another vertical line in red indicating our friend’s score. The spread of the bottom distribution is wider than the one above." /></p>

::: { .qti-item #Ch6_Combining_3 }
:::::: { #a834a832-439a-46e1-9102-45c66f7bb856 .qti-question .essay points="1" max-words="100" }

If the true distribution of Kargle scores was the one on the top, above, what would you think of your friend's score of 37,000?

::::::

:::::: { #3ede3f7e-ce3d-412c-96f0-44b25cb7775b .qti-question .essay points="1" max-words="100" }

What if the true distribution of Kargle scores was the one on the bottom? Now what would you think about your friend's score of 37,000?

::::::

:::::: { #e0531859-c87b-4226-a86f-dbfda0e7472f .qti-question .essay points="1" max-words="100" }

In which of these two distributions would you say the score of 37,000 is a better score? Why?

::::::
:::

Clearly your friend would be an outstanding player if Distribution 1 were true. But if Distribution 2 were true, they would be just slightly above average.

We can see this visually just by looking at the two histograms. But is there a way to quantify this intuition? One way to do this is by transforming the score we are trying to interpret into a z-score using this formula:

$$z_i=\frac{Y_i-\bar{Y}}{s}$$

::: { .qti-item #Ch6_Combining_4 }
:::::: { #659c543b-9954-4ad3-ab5e-cdee2355a85c .qti-question .multiple-choice points="1" }

What is the numerator in the formula above?

::::::::: { .choices }

- [Deviation]{ .correct }
- Sum of squares
- Sample mean
- Population mean
- Sample standard deviation

:::::::::

::::::

:::::: { #5f4d94ce-9d51-458b-b9eb-88fb7cad1213 .qti-question .multiple-choice points="1" }

And what is the denominator?

::::::::: { .choices }

- Deviation
- Sum of squares
- Sample mean
- Population mean
- [Sample standard deviation]{ .correct }

:::::::::

::::::

:::::: { #3baaaa18-938c-4493-a238-7e742cd2e3d0 .qti-question .essay points="1" max-words="100" }

See if you can explain what "z" means just by analyzing the formula.

::::::
:::

Let’s apply this formula to our video game score of 37,000 based on each of the two hypothetical distributions (#1 and #2) above.

We show you the R code for calculating the z-score for a score of 37,000 if Distribution 1 is true. Write similar code to calculate z-score if Distribution 2 is true.

```{ data-ckcode=true #B2_Code_Z_01 }
%%% setup
require(coursekata)

%%% prompt
# z-score if distribution 1 were true
(37000 - 35000)/1000

# z-score if distribution 2 were true

%%% solution
# z-score if distribution 1 were true
(37000 - 35000)/1000

# z-score if distribution 2 were true
(37000 - 35000)/5000

%%% test
ex() %>% {
    check_output_expr(., "(37000 - 35000)/1000")
    check_output_expr(., "(37000 - 35000)/5000", missing_msg="Did you divide by the sd of the second distribution?")
}
```

::: { .qti-item #Ch6_Combining_5 }
:::::: { #19ade23c-65af-48c7-888a-1cdf482e9ec7 .qti-question .short-answer points="1" }

What z scores did you get for the two distributions?

::::::
:::

```
2
```

```
0.4
```

In both cases, the numerator is the same: 37,000 (the individual score) minus the mean of the distribution, which equals 2,000. The denominators for the two z-scores are different, though, because the distributions have different standard deviations. In distribution #1, the standard deviation is 1,000. So, the z-score is 2,000 divided by 1,000, or 2. For the other distribution, the standard deviation is 5,000. So, the z-score is 2,000 divided by 5,000, or .40.

::: { .qti-item #Ch6_Combining_6 }
:::::: { #d7045121-c5cd-4fd3-b30f-60198c6c205b .qti-question .essay points="1" max-words="100" }

Why do we put parentheses in the expression (37,000 - 35,000)/1,000?

::::::
:::

If we did this calculation without parentheses, the calculation would be 37,000 - (35,000 / 5,000) because order of operations, our cultural conventions for how we do arithmetic, says that division is done before subtraction.

::: { .qti-item #Ch6_Combining_7 }
:::::: { #b687b073-08bd-46b7-8bb3-08390f69bb83 .qti-question .essay points="1" max-words="100" }

Interpret these z scores. They are measures, but what is the unit of measurement? 2 what? 0.4 what?

::::::
:::

**A z-score represents the number of standard deviations a score is above (if positive) or below (if negative) the mean**. So, the units are standard deviations. A z-score of 2 is two standard deviations above the mean. A z-score of 0.4 is 0.4 standard deviations above the mean.

::: { .qti-item #Ch6_Combining_8 }
:::::: { #230facff-8089-4b3a-93d0-60f9b921527e .qti-question .essay points="1" max-words="100" }

Now compare the two z scores (2 vs. 0.4). Which is more impressive, a player with a z score of 2 or one with a z score of 0.4? Why?

::::::
:::

A z-score of 2 is more impressive—it’s two standard deviations above the mean. It should be harder to score two standard deviations above the mean than to score 0.4 (or less than one half) a standard deviation above the mean.
