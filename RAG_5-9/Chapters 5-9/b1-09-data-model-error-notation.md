## 5.9 DATA = MODEL + ERROR: Notation

Now let’s see how mathematical notation is used to represent the simple (empty) model we introduced before.

<p style="text-align: center;">**Thumb = Mean + Error**</p>

There are some real advantages to rewriting this statement in mathematical notation. Here’s one form this notation might take:

$$Y_i=\bar{Y}+e_i$$

This equation literally represents what we showed above in our word equation. It tells us that each value of **Thumb** in our dataset ($Y_i$) can be seen as the sum of two parts: the mean of all values of $Y$ ($\bar{Y}$, which is the empty model prediction), and its residual from that mean ($e_i$, or error). If we add these two numbers together (**Mean + Error**) for a specific score, we will get the original score. Very simple, very concrete.

### Notation for the General Linear Model

This notation for the mean ($\bar{Y}$) works well enough for the empty model. But it's not going to help us build more complex models later. To prepare for that eventuality, we will introduce a more general notation, referred to as the General Linear Model (GLM). In GLM notation, the empty model is represented like this:

$$Y_i=b_0+e_i$$

::: { .qti-item #Ch5_Notation_1 }
:::::: { #df567ea3-3c90-4bd7-b606-9b6cdb3703b8 .qti-question .essay points="1" max-words="100" }

Based on what you have learned about notation so far, what do you think the $b_0$ might represent in the equation above?

::::::
:::

This is a more *general* version of the equation above, in which we have substituted $b_0$ (we read this as "b sub 0") for the mean, $\bar{Y}$. This won't make much sense right now, but later it will help us add complexity to our model (with $b_1$, $b_2$, and so forth). The main thing to know for now is that $b_0$ can represent the mean, as it does in the empty model, but it won't always represent the mean.

$$\underbrace{Y_i}_\text{Thumb}=\underbrace{b_0}_\text{Predict}+\underbrace{e_i}_\text{Resid}$$

Indeed, this flexibility is what makes the General Linear Model *general*. Whenever you see a GLM model statement, you should think carefully about what, in the particular situation, each symbol represents.

::::::::: { .qti-item #Ch5_Notation_2 }
:::::: { #ec6de1e5-7326-4273-8b3c-8a74711ae7df .qti-question .association
points="1" }
Using our `Thumb` example, try to interpret this GLM notation by mapping on
the contextual interpretations:

$$Y_i=b_0+e_i$$

::: associations

- [$Y_i$]{match="1"}
- [$b_0$]{match="3"}
- [$e_i$]{match="2"}
:::
::: choices

1. $\text{Thumb}_i$
2. $\text{Residual}_i$
3. Mean
:::
::::::
:::::: { #edd45253-c569-4590-af36-3ce1a11fd685 .qti-question .association
points="1" }
Now try interpreting this GLM Notation by mapping on elements of our DATA =
MODEL + ERROR statement.

$$Y_i=b_0+e_i$$

::: associations

- [$Y_i$]{match="1"}
- [$b_0$]{match="2"}
- [$e_i$]{match="3"}
:::
::: choices

1. DATA
2. MODEL (or PREDICTION)
3. ERROR
:::
::::::
:::::::::

<iframe title="What is 'DATA = MODEL + ERROR'?" data-type="vimeo" id="379150092" width="640" height="360" src="https://player.vimeo.com/video/379150092" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

<a href="https://docs.google.com/document/d/10DmrpTcTyh0vqy8RnV7i1bc_JEraGHJpx9RizoofOwc/edit?usp=sharing">Video Transcript</a>

### Statistics and Parameters

Now is a good time to remember that our goal in exploring distributions of data is to find out about the DGP. Our goal in constructing statistical models is the same: we estimate models based on data in order to make inferences about the population and the DGP.

With our data, we can calculate the exact mean of the distribution, and the exact size of the errors. When we do this, we are calculating a *statistic*. A statistic is anything you can compute to summarize something about your data; the mean is our first example of a statistic.

But we can’t calculate the mean of the population; the population distribution is unknown. Instead we use the mean we calculate from our data as an *estimate* of the mean of the population—the distribution from which our data were sampled.

The mean of the population is an example of a *parameter*. A parameter is a number that summarizes something about a population. **Whereas statistics are computed, parameters are estimated.** We use statistics as estimates because we don’t generally know what the true parameter is.

::: { .qti-item #Ch5_Notation_3 }
:::::: { #21d5f186-d54d-4cbf-83c0-002864d1a5b9 .qti-question .multiple-choice points="1" }

When we use the mean as a model, why do we call it a "parameter estimate"?

::::::::: { .choices }

- Because we can't calculate the mean of a sample, we must estimate it.
- [Because we can't calculate the mean of the DGP, we must estimate it.]{ .correct }
- Because whenever we use R to calculate something, we call it an estimate.
- Because the formula for the mean is very complicated, we call it an estimate.

:::::::::

::::::

:::::: { #1cf104f1-567c-4aff-961d-ead0b8d53690 .qti-question .multiple-choice points="1" }

What is the difference between a model of data and a model of the DGP?

::::::::: { .choices }

- What we want is a good model of the DGP. Because we can't develop one directly, we must instead develop a model based on sample data.
- Our certainty about each model's accuracy is different.  We can be certain about our sample model statistics, but never truly know the parameters in the model of the DGP.
- [Both of the above are differences.]{ .correct }
- Neither of the above are differences.

:::::::::

::::::
:::

Sometimes students think that the main goal of statistics is to calculate a correct answer. But statistics isn’t mostly about calculation. It is mostly a way of thinking about how to interpret those calculations. In statistics, understanding *what you are trying to calculate* can be just as important as the calculations themselves.

Notation is one way we keep our thinking straight about *what we are trying to calculate*, and what the results of our calculations mean. Because the distinction between statistics (or *estimators*) and parameters is so critical, we use different notation to distinguish them.

If we want to represent the mean calculated from data, we typically use the notation $\bar{Y}$ (or, sometimes, $\bar{X}$). To represent the mean of the population, we typically use the Greek letter $\mu$ (pronounced "mew").

The same distinction shows up in the notation of the General Linear Model. The empty model we have discussed so far, which is calculated from data, is written like this (as you know):

$$Y_i=b_0+e_i$$

The model of the DGP that we are **trying to estimate** when we fit the empty model is represented like this:

$$Y_i=\beta_{0}+\epsilon_i$$

Note that in this model of the population we have replaced the estimators $b_0$ and $e_i$ with the Greek letters $\beta_{0}$ (pronounced "beta sub 0") and $\epsilon_i$ (pronounced “epsilon sub i”). $b_0$ is the estimator for $\beta_{0}$, which is used to represent the mean of the population; and $e_i$ is the estimator for $\epsilon_i$.

Whenever you see Greek letters you can be pretty sure we are talking about parameters of the population. Roman letters are generally used to represent estimators calculated from data. Models are often referred to by the number of parameters that are estimated. The empty model can be referred to as a "one-parameter model" because only one parameter ($/beta_{0}$) is estimated.

::: { .qti-item #Ch5_Statistics_1_r3.0 }
:::::: { #a65df333-335a-4a97-a155-f0449ef1398d .qti-question .multiple-choice points="1" scoring="partial" }

```
empty_model <- lm(Thumb ~ NULL, data = Fingers)
empty_model

Call:
lm(formula = Thumb ~ NULL, data = Fingers)

Coefficients:
(Intercept)
       60.1
```

When we ran this R code to fit the empty model to our data for the thumb lengths from the full `Fingers` data set, what was the number 60.1? (Check all that apply.)

::::::::: { .choices }

- [A statistic]{ .correct }
- A parameter
- [A parameter estimate]{ .correct }

:::::::::

::::::

:::::: { #f932e6c1-9f0f-4320-9105-102748005687 .qti-question .multiple-choice points="1" }

Should 60.1 be represented in the GLM notation as $b_0$ or $\beta_0$?

::::::::: { .choices }

- [$b_0$]{ .correct }
- $\beta_0$

:::::::::

::::::
:::

As it turns out, in the absence of other information about the objects being studied, the mean of our sample is the best estimate we have of the actual mean of the population. It is equally likely to be too high as it is too low, making it an unbiased estimator of the parameter.

Because it is our best guess of what the population parameter is, it is the best predictor we have of the value of a subsequent observation. While it will certainly be wrong, the mean will do a better job than any other number.

<iframe title="Why do we need those Greek letters?" data-type="vimeo" id="379319558" width="640" height="360" src="https://player.vimeo.com/video/379319558" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

<a href="https://docs.google.com/document/d/16WjW406fr8RPfdSqpJGY4jgulQdbd1IdLWSPgZdm74w/edit?usp=sharing">Video Transcript</a>

::: { .qti-item #Ch5_Statistics_4 }
:::::: { #033d709f-4df1-44b3-a07d-33881ec050cb .qti-question .multiple-choice points="1" }

Let's say we run a study and calculate a parameter estimate, $b_0$ = 25. We decide to run the study again, and this time get the same parameter estimate of $b_0$ = 25. Based on these two studies, what do we know about the population parameter $\beta_0$?

::::::::: { .choices }

- We know the true population parameter $\beta_0$ = 25, because both samples confirmed this.
- We know the true population parameter is probably 25, but we'd have to do the study more than twice to be sure.
- [We know that 25 is our best estimate of $\beta_0$, but we can never be sure of the true population parameter.]{ .correct }

:::::::::

::::::
:::

::::::::: { .qti-item #Ch5_Statistics_3 }
:::::: { #f87cee6a-75ad-48d2-8027-ce9dfd58683a .qti-question .association
points="1" }
Match each concept to its notation.
::: associations

- [Mean of a population]{match="3"}
- [Error around a population model]{match="2"}
- [Mean of a sample]{match="4"}
- [Error around a sample model]{match="1"}
:::
::: choices

1. $e_i$
2. $\epsilon_i$
3. $\mu$
4. $\overline{Y}$
:::
::::::
:::::: { #abe69fb7-c547-4271-a003-3528caaa64ab .qti-question .association
points="1" }
Which is which?
::: associations

- [Describes a sample]{match="2"}
- [Describes a population]{match="1"}
:::
::: choices

1. Parameter
2. Statistic
:::
::::::
:::::: { #05fe11d6-4135-427e-ad6c-022f51a7830d .qti-question .essay points="1" }
What is the difference between $b_0$ and $\overline{Y}$?
::::::
:::::: { #74e143a2-7f7c-4a0c-b878-e3b1619070ae .qti-question .essay points="1" }
What is the difference between $b_0$ and $\beta_0$?
::::::
:::::::::
