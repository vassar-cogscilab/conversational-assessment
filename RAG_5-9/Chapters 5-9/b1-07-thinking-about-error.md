## 5.7 Thinking About Error

We have developed the idea of the mean being the simplest (or empty) model of the distribution of a quantitative variable, represented in this word equation:

<p style="text-align: center;">**DATA = MEAN + ERROR**</p>

If this is true, then we can calculate error in our dataset by just moving components of this equation around to get the formula:

<p style="text-align: center;">**ERROR = DATA - MEAN**</p>

Using this formula, if someone has a thumb length larger than the mean (e.g., 62 versus a mean of 60.1), then their error is a positive number (in this case, nearly +2). If they have a thumb length lower than the mean (e.g., 58) then we can calculate their error as a negative number (e.g. about -2).

We generally call the error calculated this way as the *residual*. Now that you know how to generate predictions, we'll refine our definition of the residual to be the difference between our model's prediction and an actual observed score. The word residual should evoke *the stuff that remains* because the residual is the leftover variation from our data once we take out the model.

To find these errors (or residuals) you can just subtract the mean from each data point. In R we could just run this code to get the residuals:

```
Fingers$Thumb - Fingers$Predict
```

::: { .qti-item #b1_Predictions_2 }
:::::: { #11de9d10-23a1-48b1-818b-5f5f3a03086f .qti-question .multiple-choice points="1" }

If we run this code, what do you think will happen?

::::::::: { .choices }

- R will calculate a residual for a future student.
- [R will generate a list of residuals, one for each student in the `Fingers` data frame.]{ .correct }
- R will make a prediction for each student in the `Fingers` data frame.
- R will generate a list of 157 identical numbers because all of these residuals should be the same.

:::::::::

::::::
:::

If we run the code, R will calculate the 157 residuals, but it won't save them unless we tell it to do so. Modify the code in the window below to save the residuals in a new variable in `Fingers` called `Resid`. (Note that the variable `Predict` already exists in the Fingers data frame).

```{ data-ckcode=true #B1_Code_Thinking_01 }
%%% setup
require(coursekata)

Fingers$TinySet <- c(1,1,1,0,0,0,1,0,0,1, rep(0,147))
Fingers$TinySet[142] <- 1
Fingers <- arrange(arrange(Fingers, Height), desc(TinySet))

empty_model <- lm(Thumb ~ NULL, data = Fingers)
Fingers <- Fingers %>% mutate(
    Predict = predict(empty_model),
    Resid = Thumb - Predict
)

%%% prompt
# modify this to save the residuals from the empty_model
Fingers$Resid <-

# this prints selected variables from Fingers
select(Fingers, Thumb, Predict, Resid)

%%% solution
# modify this to save the residuals from the empty_model
Fingers$Resid <- Fingers$Thumb - Fingers$Predict

# this prints selected variables from Fingers
select(Fingers, Thumb, Predict, Resid)

%%% test
ex() %>% check_object("Fingers") %>%
    check_column("Resid") %>% check_equal()
```

```
 Thumb  Predict     Resid
1    52 60.10366 -8.103662
2    56 60.10366 -4.103662
3    64 60.10366  3.896338
4    70 60.10366  9.896338
5    66 60.10366  5.896338
6    62 60.10366  1.896338
```

These residuals (or "leftovers") are so important in modeling that there is an even easier way to get them in R. The function `resid()`, when given a model (e.g., `empty_model`) will return all the residuals from the predictions of the model.

```
resid(empty_model)
```

Modify the following code to save the residuals that we get using the `resid()` function as a variable in the `Fingers` data frame. Call the new variable `EasyResid`.

```{ data-ckcode=true #Code_Thinking_02 }
%%% setup
require(coursekata)

Fingers$TinySet <- c(1,1,1,0,0,0,1,0,0,1, rep(0,147))
Fingers$TinySet[142] <- 1
Fingers <- arrange(arrange(Fingers, Height), desc(TinySet))

empty_model <- lm(Thumb ~ NULL, data = Fingers)
Fingers <- Fingers %>% mutate(
    Predict = predict(empty_model),
    Resid = Thumb - Predict
)

%%% prompt
# calculate the residuals from empty_model the easy way
# and save them in the Fingers data frame
Fingers$EasyResid <-

# this prints select variables from Fingers
head(select(Fingers, Thumb, Predict, Resid, EasyResid))


%%% solution
# calculate the residuals from empty_model the easy way
# and save them in the Fingers data frame
Fingers$EasyResid <- resid(empty_model)

# this prints select variables from Fingers
head(select(Fingers, Thumb, Predict, Resid, EasyResid))

%%% test
ex() %>% check_object("Fingers") %>%
    check_column("EasyResid") %>% check_equal()

```

```
 Thumb  Predict     Resid EasyResid
1    52 60.10366 -8.103662 -8.103662
2    56 60.10366 -4.103662 -4.103662
3    64 60.10366  3.896338  3.896338
4    70 60.10366  9.896338  9.896338
5    66 60.10366  5.896338  5.896338
6    62 60.10366  1.896338  1.896338
```

Notice that the values for `Resid` and `EasyResid` are the same for each row in the dataset. We will generally use the `resid()` function from now on, just because it's easier, but we want you to know what the `resid()` function is doing behind the scenes.

Below we have plotted a few of the residuals from the `Fingers` dataset on the `Thumb` by `Height` scatter plot. Visually, the residuals can be thought of as *the vertical distance* between the data (the students' actual thumb lengths) and the model's predicted thumb length (60.1).

Note that sometimes the residuals are negative (extending below the empty model) and sometimes positive (above the empty model). Because the empty model is the mean, we know that these residuals are perfectly balanced across the full dataset of 157 students.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/zJypG0qZ.png" width=80% alt="Scatter plot of Thumb predicted by Height from the Fingers data frame, with the empty model overlaid as a horizontal line. A few data points above and below the model are highlighted and connected to the model by vertical lines." /></p>

::: { .qti-item #b1_Predictions_3 }
:::::: { #046e25f6-b46e-40c7-b93f-9a91e4592e32 .qti-question .multiple-choice points="1" }

Because the mean balances the residuals, if we use the code `sum(Fingers$Resid)`, what number should we expect?

::::::::: { .choices }

- [0]{ .correct }
- the mean (60.1)
- 157 (same as the number of students)

:::::::::

::::::
:::

### Distribution of Residuals

Below we’ve plotted histograms of the three variables: `Thumb`, `Predict`, and `Resid`.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/WNrnMzD5.png" width=100% alt="A histogram of the distribution of Thumb on the left. A histogram of the distribution of Predict in the middle. There’s no variation in this distribution. A histogram of the distribution of Resid on the right. The distribution of Thumb and the distribution of Resid have the exact same shape, but different means." /></p>

::: { .qti-item #b1_Predictions_4 }
:::::: { #225e0146-24a3-49ad-b430-665dcd5e9d01 .qti-question .essay points="1" max-words="200" }

Examine the distributions above.

What does the distribution of `Thumb` (data) look like?

What about the distribution of `Predict` (model)?

Finally, what about the distribution of `Resid` (error)?

::::::

:::::: { #095505d6-926b-4a99-b1b2-cbd16678178d .qti-question .essay points="1" max-words="100" }

What is different about the distributions of data and error? What is similar?

::::::
:::

The distributions of the data and the residuals have the same shape. But the numbers on the x-axis differ across the two distributions. The distribution of `Thumb` is centered at the mean (60.1), whereas the distribution of `Resid` is centered at 0. Data that are smaller than the mean (such as a thumb length of 50) have negative residuals (-10) but data that are larger than the mean (such as 70) have positive residuals (10).

Let's see what we would get if we summed all values for the variable `Fingers$Resid`. Try it in the code block below.

```{ data-ckcode=true #Code_Thinking_03 }
%%% setup
require(coursekata)

empty_model <- lm(Thumb ~ NULL, data = Fingers)
Fingers <- Fingers %>% mutate(
    Predict = predict(empty_model),
    Resid = resid(empty_model)
)

%%% prompt
# assume Fingers data frame already has the variable Resid saved in it


%%% solution
# assume Fingers data frame already has the variable Resid saved in it
sum(Fingers$Resid)


%%% test
ex() %>% {

    check_output_expr(., "sum(Fingers$Resid)")
}

```

```
-1.4738210651899e-14
```

R will sometimes give you outputs in scientific notation. The `-1.47e-14` is equivalent to $-1.47*10^{-14}$ which indicates that this is a number very close to zero (the -14 meaning that the decimal point is shifted to the left 14 places)! Whenever you see this scientific notation with a large negative exponent after the "e", you can just read it as “zero,” or pretty close to zero.

The residuals (or error) around the mean always sum to 0. The mean of the errors will also always be 0, because 0 divided by n equals 0. (R will not always report the sum as exactly 0 because of computer hardware limitations but it will be close enough to 0.)
