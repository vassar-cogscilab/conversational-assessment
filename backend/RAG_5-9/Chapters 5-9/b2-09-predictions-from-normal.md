## 6.9 Using the Normal Model to Make Predictions

Let’s go back now to the question we asked earlier: Given the distribution of thumb length, what is the probability that the next randomly sampled student would have a thumb length at least 65.1 mm long? (The "at least" phrase indicates a thumb length 65.1 mm *or even longer*!) How could we use the smoothed out normal model to answer this question?

### Fitting the Normal Model to a Distribution of Data

We first need to fit the normal model to the distribution of thumb length in our data (much like how we fit simple shapes over the irregularly shaped state of California). Below is the jagged distribution of `Thumb`. We have represented the empty model (the mean of the distribution, 60.1) as a blue line to serve as a reference point.

```
empty_model <- lm(Thumb ~ NULL, data = Fingers)

gf_dhistogram(~ Thumb, data = Fingers) %>%
  gf_model(empty_model)
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/DvHHkmVK.png" width=80% alt="A density histogram of the distribution of Thumb in Fingers with a vertical line in blue showing the mean." /></p>

The normal distribution is actually a family of theoretical distributions, each having a different mean and a different standard deviation. To find the particular normal distribution that best fits our data, we need to find the two parameters (mean and standard deviation) that define the best-fitting curve, i.e. the curve that minimizes the squared residuals of our data from the model.

The figure below can give you a sense of how normal distributions can vary from each other, depending on their means and standard deviations. Note that three of the four distributions pictured have the same mean, which is 0, but quite different shapes. The fourth distribution has a mean that is below the other three.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/R0TsWYLg.png" width=80% alt="Normal distributions with different means and standard deviations." /></p>

Finding the normal curve that best fits our distribution of data is fairly straightforward. First we use our sample mean and standard deviation ($\bar{Y}$ and $s$) as estimates of the population mean and standard deviation ($\mu$ and $\sigma$). Then, using these estimates we can use the `gf_fitdistr()` function to graphically overlay the best-fitting normal model on the distribution of data.

The `gf_fitdistr()` function can overlay a number of different mathematical probability distributions. The default distribution is a normal distribution (this function automatically calculates the mean and standard deviation to draw the normal curve).

```
gf_dhistogram(~ Thumb, data = Fingers) %>%
  gf_model(empty_model) %>%
  gf_fitdistr()
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/WsyM7Z0j.png" width=80% alt="A density histogram of the distribution of Thumb in Fingers with a vertical line in blue showing the mean and overlaid with the best-fitting normal model in black." /></p>

You might be thinking—hmm, the normal curve doesn’t fit *that* well over the data. You are correct! But remember, our goal is not just to model our data, but to model the long-term results of the DGP. Even when our data look jagged, the population distribution may not be.

And, the goal of a model is not to fit perfectly, but to balance the fit of the model with the simplicity and elegance of the model. By modeling error with the normal curve, we can trade in the complexity of 157 jagged values for an elegant, two-parameter model—the normal curve.

Finally, remember our original question? We wanted to know the exact probability that the next randomly sampled student would have thumb length of more than 65.1 mm. To help visualize this question, let’s add one more thing to the graph: a red line to locate 65.1 mm in reference to the distribution.

```
gf_dhistogram(~ Thumb, data = Fingers) %>%
  gf_model(empty_model) %>%
  gf_fitdistr() %>%
  gf_vline(xintercept = 65.1, color = "red")
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/bYdyLZxc.png" width=80% alt="A density histogram of the distribution of Thumb in Fingers with a vertical line in blue showing the mean, overlaid with the best-fitting normal model, and with another vertical line in red showing a thumb length of 65.1 mm." /></p>

With the help of this picture, we can restate our question as: What proportion of the area under the black normal curve falls to the right of the red vertical line? This proportion, which we will calculate below, would tell us the probability that the next randomly sampled student would have a thumb length longer than 65.1 mm.

### Using the Normal Distribution to Calculate Probabilities

Once you have fit a smooth normal curve over a data distribution, you can use mathematical properties of the curve (don’t worry, we’ll let R handle that!) to find the probability of scores falling into specific regions. This is exactly like what we did when we used rectangles to model the area of California. Once we fit a rectangle, we could simply use the formula for the area of a rectangle ($l \times w$) to calculate the area.

In the graph below, we have removed the distribution of data, and left only the best-fitting normal curve. The answer to the question, "What is the probability that the next student will have a thumb length more than 65.1 mm?," is represented by the region colored green under the curve. If we can find the proportion of total area that is colored green, we can use that proportion as our probability estimate for the next observation being greater than 65.1.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/gc9pyg2R.png" width=80% alt="A best-fitting normal curve of Thumb with a vertical line in black showing a thumb length of 65.1 mm whose z-score is 0.57." /></p>

::: { .qti-item #Ch6_UsingNormal_1 }
:::::: { #a60ae680-a842-4078-ae65-40bb326f574e .qti-question .multiple-choice points="1" }

What value of `Thumb` is represented by the blue, vertical line in the picture above?

::::::::: { .choices }

- [65.1]{ .correct }
- The mean of the distribution
- The proportion of thumbs larger than 65.1
- The proportion of thumbs smaller than 65.1

:::::::::

::::::

:::::: { #2a2ddb3d-6323-4c0d-bb90-04832253d325 .qti-question .multiple-choice points="1" }

Based on this picture, eyeball the proportion of thumbs that might be at least 65.1.

::::::::: { .choices }

- .10
- [.30]{ .correct }
- .50
- .75
- .85

:::::::::

::::::
:::

Because the normal distribution has a smooth shape easily defined by two parameters, R can tell us the exact probability by using the mathematical function for a normal distribution. There is a function called `xpnorm()` that can do this with just three pieces of information: the border you are interested in, and the mean and standard deviation of the normal distribution.

```
xpnorm(65.1, mean(Fingers$Thumb), sd(Fingers$Thumb))
```

Note that you can also include argument labels, `mean =` and `sd =`, which would give you the flexibility to put the values in a different order like this: `xpnorm(65.1, sd =  sd(Fingers$Thumb), mean = mean(Fingers$Thumb))`.

Try running the function in the code window below. It will generate both this picture as well as some output where you can read off the exact probability that you are looking for.

```{ data-ckcode=true #B2_Code_UsingNormal_01 }
%%% setup
require(coursekata)


%%% prompt
# try running this code
xpnorm(65.1, mean(Fingers$Thumb), sd(Fingers$Thumb))

%%% solution
# try running this code
xpnorm(65.1, mean(Fingers$Thumb), sd(Fingers$Thumb))

%%% test
ex() %>% check_error()

```

::: { .qti-item #Ch6_UsingNormal_2 }
:::::: { #4820f3dd-1da4-4c67-ad23-ab855456e221 .qti-question .multiple-choice points="1" }

When we model error with a normal distribution, we think about our data in a smooth way rather than a jagged way. If we are interested in the probability of a student having a thumb longer than 65.1 mm, what part of the picture above should we look at?

::::::::: { .choices }

- The purple part
- [The green part]{ .correct }
- The border
- The y-axis
- The x-axis

:::::::::

::::::

:::::: { #4622c6f0-c2d1-4f00-bcbb-49735ec78b60 .qti-question .multiple-choice points="1" }

According to the normal model, what is the probability of a student having a thumb longer than 65.1?

::::::::: { .choices }

- .72
- [.28]{ .correct }
- .57
- .65

:::::::::

::::::

:::::: { #65717c6b-b5b1-44b1-be7b-47369715bb1e .qti-question .multiple-choice points="1" }

You probably noticed that the border (the black line representing 65.1 mm) is not labeled 65.1. Instead, it is labeled "z = 0.57."  What does this z score mean?

::::::::: { .choices }

- The probability of someone having a thumb length of exactly 65.1 mm
- The likelihood of having a thumb of at least 65.1 mm
- [The number of standard deviations that fit between the mean and 65.1 mm]{ .correct }

:::::::::

::::::
:::
