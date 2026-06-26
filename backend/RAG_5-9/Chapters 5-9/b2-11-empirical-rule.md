## 6.11 The Empirical Rule

The cool thing about normal distributions is that they all basically follow this pattern. In the smooth perfect version of the normal distribution (i.e., the theoretical probability distribution), Zone 1 covers about .68, Zone 2 covers .95, and Zone 3 covers .997. This .68-.95-.997 pattern is called the *empirical rule*.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/xdg5fz97.png" width=80% alt="A normal distribution curve representing the empirical rule, with vertical lines marking the mean and each standard deviation above and below the mean. Horizontal arrows indicate each portion under the curve that corresponds to 68, 95, and 99 percent of the middle areas under the curve." /></p>

The empirical rule tells us:

* Approximately 68 percent of the scores in a normal distribution are within one standard deviation, plus or minus, of the mean.

* Approximately 95 percent of the scores are within two standard deviations.

* Approximately 99.7 percent of scores are within three standard deviations of the mean (in other words, almost all of them).

The smooth normal distribution is something that is so perfect that it doesn’t really exist. It’s a mathematical object, kind of like how there are straight lines in the world, but a mathematical straight line is this perfect thing that has no mass, no jitter, and goes on forever. In the same way, a mathematical normal distribution is perfect with no mass, no jitter, and it goes on forever.

The tails of the normal distribution never quite hit 0, they just go on forever and ever. This is why the normal distribution is sometimes called *asymptotic*. This feature is important because it allows us to predict the very tiny probabilities of very unlikely events such as a person with a thumb length of 1,000 mm.

You probably have never even heard of a thumb so long. But, if we assume the normal probability distribution, we could quantify *exactly how low the probability would be* of finding such a rare event.

You can try making up a standard deviation for your own game (we’ll call it Zargle) and simply run the code. It will show you the histograms and proportions for the three zones. Try some different standard deviations to try and break the empirical rule.

```{ data-ckcode=true #B2_Code_Empirical_01 }
%%% setup
require(coursekata)

simulate_scores <- function(game, n, mean, sd) {
  scores <- rnorm(n, mean, sd)
  z <- (scores - mean) / sd
  interval <- ifelse(z > 0, trunc(1 + z), trunc(z - 1))
  data.frame(game = game, scores = scores, z = z, interval = interval, zone = abs(interval))
}

compare_score_distributions <- function(sd = 3500, mean = 35000, n = 1000, ..., .seed = 5) {
  set.seed(.seed)
  kargle <- simulate_scores("Kargle", 1000, 35000, 5000)
  bargle <- simulate_scores("Bargle", 1000, 35000, 1000)
  zargle <- simulate_scores("Zargle", n, mean, sd)
  games <- vctrs::vec_c(kargle, bargle, zargle)

  # combine all zones > 3 into a single "outside 3" zone
  games$zone <- ifelse(games$zone > 3, "outside 3", games$zone)
  # convert the proportions to cumulative proportions for all except "outside 3"
  props <- data.frame(tally(zone ~ game, data = games, format = "proportion"))
  props <- purrr::map_dfr(split(props, props$game), function(x) {
    x$Freq <- c(cumsum(x$Freq[1:3]), x$Freq[4])
    x
  })
  # re-format the table to be wide (one column per game)
  zone_table <- tidyr::pivot_wider(props, names_from = game, values_from = Freq)

  gf_histogram(~scores, fill = ~zone, data = games, bins = 160, alpha = .8) %>%
    gf_facet_grid(game ~ .) %>%
    print()

  data.frame(zone_table)
}

%%% prompt
# change the standard deviation to whatever you'd like it to be
# try to break the empirical rule!
compare_score_distributions(sd = 3500, mean = 35000, n = 1000)

%%% test
ex() %>% check_error()
```

This is what we would get for the Zargle distribution if the standard deviation was set for 3,500.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/z5bS78yr.png" width=80% alt="A histogram of the distribution of score in Bargle on the top. A histogram of the distribution of score in Kargle in the middle. A histogram of the distribution of score in Zargle at the bottom. The distributions have the same mean but different spreads." /></p>

```
       zone Bargle Kargle  Zargle
1         1  0.686  0.690   0.675
2         2  0.950  0.948   0.944
3         3  0.998  0.996   0.997
4 outside 3  0.002  0.004   0.003
```

The empirical rule can be very useful when trying to make a quick interpretation of a specific score. If a friend has a baby and tells you it was 54 cm long, how would you interpret that measurement? As an experienced statistician, you should ask: what is the mean, and what is the standard deviation, of the distribution of baby length at birth?

As it turns out, the mean baby length is roughly 50 cm, and the standard deviation is 2 cm. Using the empirical rule, you would say, "Wow! Your baby is like two standard deviations above the mean! That’s a huge baby! Only .05 of babies are longer than 54 cm (the mean plus two standard deviations). You’ve got yourself a big one!"

Actually, you’d be slightly wrong. (Sorry, I know we set you up!) According to the empirical rule, .95 scores in a normal distribution are within plus or minus two standard deviations from the mean. It follows from this that .05 of the scores are more extreme than this, or outside plus or minus two standard deviations.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/xdg5fz97.png" width=80% alt="Normal curve showing empirical rule" /></p>

**But note, in the figure, that if .05 of the scores are outside plus or minus two standard deviations, half of those would be expected to be more than two standard deviations above the mean, and half less than two standard deviations below the mean.**

So, only .025 of scores would be higher than two standard deviations above the mean. That baby is even more impressive than we thought! He or she is longer than 97.5% of all babies!

### What Counts as Unlikely?

We have seen how modeling the error distribution (in the case of the empty model, the distribution of scores around the mean) can help us to calculate probabilities and make predictions. The problem with a probability, though, is that it’s just a number. It doesn’t tell us what to do. We still have to think about it even after all our fancy R code calculations.

For example, if we wanted to use a model of finger lengths to design stretchy one-size-fits-all gloves, how big should we make the gloves? After all, even though very long thumbs are unlikely, they are still possible. But if we make these gloves too big, then we’ll alienate short-fingered folks.

What would be the right glove size? To answer questions like this, we have to figure out what are the most *likely* lengths of people’s fingers, and that means we need to make a judgment call about what "likely" and “unlikely” mean. We might be able to agree on the best way to estimate a probability, but people will differ on what counts as “unlikely.”

For example, someone who is very risky might look at a .01 probability and say, "Hey! At least it is still possible." But someone who likes being very certain might say, “Even .40 is unlikely because it’s less likely than a coin toss!” So in being part of a statistics community, it’s helpful to have an agreement about what counts as *unlikely.*

Statisticians, as a community, have decided to count .05 and lower probabilities as *unlikely*. So in the case of a DGP that produces a fairly normal population, we would count scores that are outside of Zone 2 (+/- two standard deviations from the mean) as unlikely scores, and the scores within Zone 2 as likely. Note that this decision doesn’t result from a calculation. Human statisticians just sort of agree—*yeah*, *.05 is a pretty low likelihood*.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Z49Zy0zk.png" width=80% alt="A density histogram of the distribution of Thumb overlaid with the best-fitting normal model, with a vertical line in blue showing the mean of 65.1 mm, and with light gray lines showing the lower boundary of Zone 2 of 43 mm and the upper boundary of Zone 2 of 78 mm." /></p>

::::::::: { .qti-item #Ch6_WhatCounts_1 }
:::::: { #79d59d40-6cdd-4389-a963-3ffb0d126181 .qti-question .multiple-choice
points="1" }
In the distribution above, we've drawn some light gray lines to illustrate the boundaries of Zone 2 (the data within 2 standard deviations from the mean).
Let's apply the statistical community's idea of "unlikely." Choose all of the
"unlikely" thumb lengths.
::: choices

* 53
* 48
* [38]{.correct}
* 75
* [80]{.correct}
* 64
* [82]{.correct}
* [90]{.correct}
* 71
:::
::::::
:::::: { #7c79690b-ce5b-4978-88ff-2e8a1319d13c .qti-question .association
points="1" match-mode="reuse" }
The "unlikely" part is the .05 part that is farthest away from the mean (in both left and right directions). Label the regions below with the appropriate proportions. (You're free to use a value more than once.)

::: {style="text-align: center;"}
![A bell-shaped normal distribution. The shaded regions at the far left (A) and far right (B) are labeled as tails, representing extreme and relatively rare values. An arrow labeled C points to the body of the curve between the tails, where most observations fall.](https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch6_WhatCounts_1_image.png){width=80%}
:::

::: associations

* [A]{match="1"}
* [B]{match="7"}
* [C]{match="1"}
:::
::: choices

1. .025
2. .05
3. .25
4. .5
5. .68
6. .9
7. .95
:::
::::::
:::::::::
