## 6.10 Getting Familiar With the Normal Distribution

By now you see why normal distributions are often good models of error (aggregation of forces!) and also how you might use them to make predictions. But why is it that distributions that look very different from one another are all called "normal"? The shape of the normal distribution is intuitively like “a bell”, but let’s consider what that really means.

To be more concrete, let’s go back to Kargle, our favorite video game.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/CYC0YbNK.png" width=80% alt="A histogram of the distribution of score in Bargle with a vertical line in blue showing the mean of 35,000 points and another vertical line in red showing a score of 37,000 points on the top. A histogram of the distribution of score in Kargle with a vertical line in blue showing the mean of 35,000 points and another vertical line in red showing a score of 37,000 points at the bottom. They are both normal but the Kargle distribution is much flatter and more spread out than the Bargle distribution." /></p>

Remember we had that friend who scored 37,000 points in Kargle (shown in red) and we were trying to evaluate how skilled a player she was? When we discovered that the bottom distribution (where the standard deviation is about 5,000) was the actual distribution of Kargle scores, we were less impressed than when we thought it was the top distribution. As it turns out, the top distribution (with a standard deviation of about 1,000) is from a game called Bargle.

::: { .qti-item #Ch6_Getting_1 }
:::::: { #cdc3e019-add7-477d-b8e6-3923aa91a212 .qti-question .essay points="1" max-words="100" }

These two distributions look pretty different from one another. But both would be called "normal distributions." What is it that makes them *the same shape*?

::::::
:::

Normal distributions are roughly "bell-shaped" in that there are way more scores in the middle than there are out in the tails. They are also symmetrical from left to right. But it turns out that normal distributions are even more regular, and thus quantifiable, than that description.

To illustrate the regularity of this normal shape, let’s just think about the players of both Kargle and Bargle that are within plus or minus (+/-) one standard deviation from the mean. We’ll call this area of the distribution Zone 1 for now. These are the players with the less extreme scores.

::: { .qti-item #Ch6_Getting_2 }
:::::: { #7fdf7daa-bf51-41fd-9db9-bdf1a0aa669c .qti-question .short-answer points="1" }

If the mean of Bargle scores is 35,000 and the standard deviation is 1,000, what is the range of scores for Zone 1 in Bargle? Hint: It might help to sketch a picture of a normal distribution and shade the region you're looking for.

::::::::: { .feedback }

About 34,000 to 36,000

:::::::::

::::::

:::::: { #1e707ebe-43f7-45cc-91d2-a1a4d85ee64d .qti-question .short-answer points="1" }

If the mean of Kargle scores is 35,000 and the standard deviation is 5,000, what is the range of scores for Zone 1 in Kargle?

::::::
:::

### Dividing Scores into Zones Based on Standard Deviation

We constructed a new variable called `zone` that simply indicates whether each person’s score is within Zone 1 (coded "1") or outside of it (coded “outside”).

To do this we first transformed each person’s raw score into a z-score (which, you may recall, indicates how many standard deviations a score is from the mean). We then coded "1" in the variable `zone` for every player whose z-score was > -1 and < 1. (Don’t worry about doing this in R; you can learn later if you want.)

In the histograms below, we have shaded Zone 1 in red, and anything outside of Zone 1 in purple.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/x9D1g9tk.png" width=80% alt="A histogram of the distribution of score in Bargle with a vertical line in blue showing the mean of 35,000 points and another vertical line in red showing a score of 37,000 points on the top. Zone 1 is shaded in teal, and the area outside of zone 1 is shaded in purple. The vertical line in red passes through the purple area. A histogram of the distribution of score in Kargle with a vertical line in blue showing the mean of 35,000 points and another vertical line in red showing a score of 37,000 points at the bottom. Zone 1 is shaded in teal, and the area outside of zone 1 is shaded in purple. The vertical line in red passes through the teal area." /></p>

Notice that our friend who scored 37,000 falls into Zone 1 for Kargle, but if that was her score in Bargle, she would be outside Zone 1. Putting aside our friend for a moment, what’s the proportion of players that fall inside Zone 1 in Bargle and Kargle? Let’s run a tally to find out.

```
tally(zone ~ game, data=VideoGame, format="proportion")
```

```
           game
zone        Bargle Kargle
  1         0.6844 0.6822
  outside 1 0.3156 0.3178
```

Wow, Zone 1—within one standard deviation from the mean—is very similar (about .68) for both Bargle and Kargle! Interestingly, more than half the distribution is within one standard deviation of the mean.

::: { .qti-item #Ch6_Dividing_1 }
:::::: { #c9619731-da2c-489e-b4f7-f89da0df227b .qti-question .multiple-choice points="1" }

What is the range of z**scores for the data points in Zone 1?

::::::::: { .choices }

- [Greater than -1 but less than 1]{ .correct }
- Greater than 0 but less than 1
- Greater than -1 but less than 0
- Greater than -0.5 but less than 0.5
- Greater than -2 but less than 2

:::::::::

::::::
:::

If we are one standard deviation in the positive direction, the z-score would be 1. If we are one standard deviation in the negative direction, the z-score would be -1. So Zone 1, +/- one standard deviation, would contain all the data for which z-scores fall between -1 and 1.

Let’s loosen our idea of "close to" average and consider the players of both Kargle and Bargle who are +/- two standard deviations from the mean. We’ll call this area Zone 2 for now.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/mLkGSn9p.png" width=80% alt="A histogram of the distribution of score in Bargle on the top. Zone 2 is shaded in green, and the area outside of zone 2 is shaded in purple. A histogram of the distribution of score in Kargle at the bottom. Zone 2 is shaded in green, and the area outside of zone 2 is shaded in purple. The proportion of Zone 2 is around 0.95 in both distributions." /></p>

::: { .qti-item #Ch6_Dividing_2 }
:::::: { #64efaf11-a456-4074-ab5b-66351e01f5d2 .qti-question .multiple-choice points="1" }

Notice that Zone 2 constitutes most of Bargle and Kargle's distributions. What do you think the proportion of scores in Zone 2 might be?

::::::::: { .choices }

- .70
- .80
- [.95]{ .correct }
- .99

:::::::::

::::::
:::

```
           game
zone        Bargle Kargle
  2         0.9518 0.9487
  outside 2 0.0482 0.0513
```

Basically, .95 of the scores fall within two standard deviations of the mean. In a normal distribution, scores are *so* clustered in the center that if you go out just two standard deviations from the center, you have captured a whole lot of your distribution!

::: { .qti-item #Ch6_Dividing_3 }
:::::: { #30e33d42-4a6d-4277-99ea-4137725e2026 .qti-question .essay points="1" max-words="100" }

What do you think might happen at +/- three standard deviations from the mean?

::::::
:::

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/nHMdSfdm.png" width=80% alt="A histogram of the distribution of score in Bargle on the top. Zone 3 is shaded in blue, and the area outside of zone 3 is shaded in purple. A histogram of the distribution of score in Kargle at the bottom. Zone 3 is shaded in blue, and the area outside of zone 3 is shaded in purple. We can barely see purple areas in both distributions." /></p>

```
       zone Bargle Kargle
1         1 0.6844 0.6822
2         2 0.9518 0.9487
3         3 0.9982 0.9972
4 outside 3 0.0018 0.0028
```

Zone 3, which is within three standard deviations from the mean, seems to cover almost all of the distribution. If you look at the tally (or look very, very carefully at the histograms), you can see that there is a tiny proportion of scores outside Zone 3.
