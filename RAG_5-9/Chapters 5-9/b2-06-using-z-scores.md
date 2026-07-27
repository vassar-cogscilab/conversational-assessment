## 6.6 Interpreting and Using Z-Scores

### How Z-Scores Are Different From Standard Deviation

::: { .qti-item #Ch6_Combining_9 }
:::::: { #f1e2d4bc-15bf-4d52-89d3-c91313205c0e .qti-question .essay points="1" max-words="100" }

What is the difference between a z score and a standard deviation?

::::::
:::

Standard deviation (SD) is roughly the average deviation of all scores from the mean. It can be seen as an indicator of the spread of the distribution. A z-score uses SD as a sort of ruler for measuring how far an individual score is above or below the mean.

A z-score tells you *how many* standard deviations a score is from the mean of its distribution, but doesn’t tell you what the standard deviation is (or what the mean is). Another way to think about it is that a z-score is a way of comparing a deviation of a score (the numerator) to the standard deviation of the distribution (the denominator).

Let’s use z-scores to help us make sense of our `Thumb` data. Calculate the z-score for a 65.1 mm thumb.

```{ data-ckcode=true #B2_Code_Using_01 }
%%% setup
require(coursekata)

%%% prompt
# this saves the mean and standard deviation of Thumb
mean <- mean(Fingers$Thumb)
sd <- sd(Fingers$Thumb)

# write code to calculate the z-score for a 65.1 mm Thumb

%%% solution
# this saves the mean and standard deviation of Thumb
mean <- mean(Fingers$Thumb)
sd <- sd(Fingers$Thumb)

# write code to calculate the z-score for a 65.1 mm Thumb
(65.1 - mean) / sd

%%% test
ex() %>% {
    check_output_expr(., "(65.1 - mean) / sd")
}
```

```
0.572534942855165
```

::: { .qti-item #Ch6_Combining_10 }
:::::: { #e90748a0-030f-4e45-8f1e-4aca0b62e464 .qti-question .multiple-choice points="1" }

Which is the correct interpretation of this z score?

::::::::: { .choices }

- This thumb is bigger than .57 of all thumbs in the population.
- This thumb is .57 m long.
- There is a .57 chance of picking a thumb that is bigger than this thumb.
- This thumb is .57 mm longer than the mean.
- [This thumb is .57 standard deviations (less than 1 standard deviation) above the mean.]{ .correct }

:::::::::

::::::
:::

A single z-score tells us how many standard deviations away this particular 65.1 mm thumb is from the mean. Because the standard deviation is roughly the average distance of all scores from the mean, it is likely that most scores are clustered between one standard deviation above and one standard deviation below the mean. It is less likely to find scores that are two or three standard deviations away from the mean. Z-scores give us a way to characterize scores in a bit finer way than just bigger or smaller than the mean.

### Using Z-Scores to Compare Scores From Different Distributions

One more use for the z-score is to compare scores that come from different distributions, even if the variables are measured on different scales.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/dq788GwK.png" width=80% alt="A histogram of the distribution of score with a vertical line in blue indicating the mean, and another vertical line in red indicating our friend’s score. " /></p>

Here's the distribution of scores for all players of the video game Kargle again. We know that the distribution is roughly normal, the mean score is 35,000, and the standard deviation is 5,000.

::: { .qti-item #Ch6_Using_2 }
:::::: { #1d58fd68-1633-48f5-a41d-4565b56d13e7 .qti-question .short-answer points="1" }

Your friend just scored 45,000 on Kargle. What is her z score? (Note: Provide only the result of your calculation.)

::::::
:::

Her z-score is +2. Wow, two standard deviations from the mean! Not a lot of scores are way up there.

Now let’s say you have another friend who doesn’t play Kargle at all. She plays a similar game, though—Spargle! Spargle may be similar, but it has a completely different scoring system. Although the scores on Spargle are roughly normally distributed, their mean is 50, and the standard deviation is 5. This other friend has a high score of 65 on Spargle.

Now: what if we want to know which friend, in general, is a better gamer? The one who plays Kargle, or the one who plays Spargle? This is a hard question, and there are lots of ways to answer it. The z-score provides one way.

We’ve summarized the z-scores for your two friends in the table below.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <tbody>
        <tr>
            <td>Player</td>
            <td>Player Score</td>
            <td>Game Mean</td>
            <td>Game SD</td>
            <td><b>Player Z-Score</b></td>
        </tr>
        <tr>
            <td>Kargle Player</td>
            <td>45,000</td>
            <td>35,000</td>
            <td>5,000</td>
            <td><b>+2.0</b></td>
        </tr>
        <tr>
            <td>Spargle Player</td>
            <td>65</td>
            <td>50</td>
            <td>5</td>
            <td><b>+3.0</b></td>
        </tr>
    </tbody>
</table>
<br>
Looking at the z-scores helps us to compare the abilities of these two players, even though they play games with different scoring systems. Based on the z-scores, we could say that the Spargle player is a better gamer, because she scored three standard deviations above the mean, compared with only two standard deviations above the mean for the Kargle player.

::: { .qti-item #Ch6_Using_1 }
:::::: { #9b94a651-fd4d-422f-baad-68eac7dd3098 .qti-question .essay points="1" max-words="100" }

In what sense is the Spargle player a better gamer? How is this represented by the z score?

::::::

:::::: { #a9811e49-f7bf-459d-84fc-7621dca82e98 .qti-question .essay points="1" max-words="100" }

Can you think of a reason why, despite the z score advantage, the Spargle player might nevertheless NOT be the better gamer?

::::::
:::

Of course, nothing is really definite with such comparisons. Someone might argue that Spargle is a much easier game, and so the people who play it tend to be novices. Maybe the Kargle player is better, because even though her z-score is lower, she is being compared to a more awesome group of gamers!
