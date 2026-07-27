## 9.12 Chapter 9 Review Questions

::: {.alert .alert-warning}
**NOTE:** Depending on your internet connection, this page may take a moment to load. In order to avoid automatic scrolling of the page, please wait until all of the questions have fully loaded before submitting responses.
:::

::: { .qti-item #B4_Review1_01 }
:::::: { #9d37ff92-cbf7-466e-9936-1ff87ca3537d .qti-question .multiple-choice points="1" }

1\. Why do some players get more playing time and some players see less game time? Let's take a look at a histogram of number of minutes played to start exploring this variation. What does the black curve drawn on this histogram represent?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/pxp2C5Kx.png" class="lrn-image-center" width="500" height="333" />

::::::::: { .choices }

- This represents the population from which these data were drawn randomly.
- [This represents a normal distribution that was fit to the mean and standard deviation of this data.]{ .correct }
- This represents a normal curve that shows the 95% of data points that lie within two standard deviations of the mean.
- This is another way of representing the sample distribution.

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_02 }
:::::: { #261125d7-e7a4-41e5-92e6-c4a74c5dda0a .qti-question .multiple-choice points="1" }

2\. One student suggests that players who make a lot of free throws (`FTMade`) are better and they would see more game time. Another student argues that making free throws doesn't make you a better player—having a higher free throw percentage (`FTPct`) is the sign of a better player, and suggests that would explain the variation in minutes played (`Mins`). Which of these plots would depict the relationship between `Mins` and one of these explanatory variables?

::::::::: { .choices }

- Box plots (i.e., `gf_boxplot`)
- [Scatter plots (i.e., `gf_point`)]{ .correct }
- Faceted histograms (i.e., `gf_histogram` with `gf_facet_grid`)
- All of the above would be able to depict these relationships equally clearly.

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_03 }
:::::: { #fbe070bd-0f83-4574-b5f5-f0d93234e414 .qti-question .multiple-choice points="1" }

3\. We made this plot to explore the idea that free throw percentage (`FTPct`) would predict how many minutes a player gets to play.

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/DnxPTD81.png" class="lrn-image-center" width="500" height="333" />

If we fit an empty model of `Mins` to this data, how would we depict it on this plot?

::::::::: { .choices }

- [A horizontal line that shows the mean for minutes played.]{ .correct }
- A vertical line that shows the mean free throw percentage.
- A diagonal line that bisects the cloud of points.
- You would not be able to represent the empty model visually because it is a single number.

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_04 }
:::::: { #b5ca8eda-8fb1-46e9-aa20-4cf68d282ab0 .qti-question .essay points="1" max-words="200" }

4\. On the left (in firebrick) is a plot depicting this model: `Min` = `FTMade` + other stuff. On the right (in black) is a plot depicting: `Min` = `FTPct` + other stuff. Which explanatory variable explains variation better: `FTMade` or `FTPct`? How do you know?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/RCNKVC3f.png" class="lrn-image-center" width="700" height="233" alt="A scatter plot of the distribution of Mins by FTMade in NBAPlayers2011 on the left. A scatter plot of the distribution of Mins by FTPct in NBAPlayers2011 on the right. The dots in the left distribution are clustered more closely to a noticeable shape compared with the dots in the right distribution." />

::::::
:::

::: { .qti-item #B4_Review1_05 }
:::::: { #0da525ac-ddb3-4450-ab64-47c69ac8e0b1 .qti-question .multiple-choice points="1" }

5\. If you fit a model that predicts `Mins` by including `FTMade` as an explanatory variable, how many parameters would the model have?

::::::::: { .choices }

- 2: `Mins` and `FTMade`
- [2: the y-intercept and the slope of the regression line]{ .correct }
- 2: the mean of `Mins` and the increment added for each free throw made that exceeds the mean number of free throws made
- 4: $Y_i,\ b_0,\ b_1,\ X_i$

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_06 }
:::::: { #1b9b5913-846f-435d-b37e-ea1eba365966 .qti-question .multiple-choice points="1" }

6\. We fit a model of `Mins` predicted by `FTMade` and called it `FTMade_model` (the output is below). If you know a player had 0 free throws, how many minutes would you predict he played?

```
Call:
lm(formula = Mins ~ FTMade, data = NBAPlayers2011)

Coefficients:
(Intercept)       FTMade
   1662.309        2.834
```

::::::::: { .choices }

- 0
- 2.83
- [1662.31]{ .correct }
- 1662.31 + 2.83

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_07 }
:::::: { #d077030f-de39-4885-b69a-221bcfed193b .qti-question .multiple-choice points="1" }

7\. We fit a model of `Mins` predicted by `FTMade` and called it `FTMade_model` (the output is below). We also fit a model of `Mins` predicted by `Points` (points scored) and called it `Points_model` (output below). From these best-fitting parameters, can we tell which model explains more variation: `FTMade_model` or `Points_model`?

```
Call:
lm(formula = Mins ~ FTMade, data = NBAPlayers2011)

Coefficients:
(Intercept)       FTMade
   1662.309        2.834

Call:
lm(formula = Mins ~ Points, data = NBAPlayers2011)

Coefficients:
(Intercept)       Points
   1156.680        1.062
```

::::::::: { .choices }

- Yes, `FTMade_model` is a better model, because the increment of time added on per free throw made is larger than the increment of time added on per point scored.
- Yes, `FTMade_model` is a better model because the intercept is larger than the intercept for `Points_model`.
- No, we should never compare models that have different explanatory variables because they are in different units.
- [No, we cannot tell from the best-fitting estimates how much variability has been explained by a model.]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_08 }
:::::: { #7d701e0f-5cff-4757-bc7a-26a4581df867 .qti-question .multiple-choice points="1" }

You run the following R code:

```
Points_model <- lm(Mins ~ Points, data = NBAPlayers2011)
Points_model
```

When you do so, you get the following output:

```
Call:
lm(formula = Mins ~ Points, data = NBAPlayers2011)

Coefficients:
(Intercept)       Points
   1156.680        1.062
```

8\. Which of the following equations represents the fitted model?

::::::::: { .choices }

- $Y_i=1156.68\ +\ 1.06\ +\ e_i$
- [$Y_i=\ 1156.68+1.06X_i+e_i$]{ .correct }
- $Y_i=1.06\ +\ 1156.68\ +\ e_i$
- $Y_i=1.06+1156.68X_i+e_i$

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_09 }
:::::: { #8acb5cbf-6f3a-429c-bd9a-fe418b4219c6 .qti-question .multiple-choice points="1" }

Our `Points_model` of the outcome variable `Mins` can be represented as:

$Y_i=b_0+b_1X_i+e_i$

9\. LeBron James scored 2,111 points in the 2011 season. In this equation, what part represents the prediction the `Points_model` would make for minutes played by LeBron James?

::::::::: { .choices }

- $b_0$
- $b_1$
- $b_1X_i$
- [$b_0+b_1X_i$]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_10 }
:::::: { #768d4c5f-ff82-4ee3-a63f-51c227d54326 .qti-question .multiple-choice points="1" }

We found the best-fitting estimates and put them into the `FTMade_model` of the outcome variable `Mins`:

$Y_i=1662.31+2.83X_i+e_i$

10\. LeBron James played 3,063 minutes, scored 2,111 points, and made 758 free throws in the 2011 season. What is the `FTMade_model`'s prediction for minutes played by LeBron James?

::::::::: { .choices }

- 3063
- 1662.31
- [1662.31 + 2.83\*758]{ .correct }
- 1662.31 + 2.83\*758 + 2111

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_11 }
:::::: { #fe13301f-5b75-477e-9211-b071d9d2386b .qti-question .multiple-choice points="1" }

11\. We have quantified error from the `FTMade_model` of `Mins` and the `Points_model` of `Mins` by using the `supernova()` function. Which of the following are reasons to think that the `Points_model` is better than the `FTMade_model`?

```
Analysis of Variance Table (Type III SS)
Model: Mins ~ FTMade

                                   SS  df           MS       F    PRE     p
----- --------------- | ------------ --- ------------ ------- ------ -----
Model (error reduced) | 21174725.960   1 21174725.960 119.466 0.4071 .0000
Error (from model)    | 30840525.949 174   177244.402
----- --------------- | ------------ --- ------------ ------- ------ -----
Total (empty model)   | 52015251.909 175   297230.011

Analysis of Variance Table (Type III SS)
Model: Mins ~ Points

                                   SS  df           MS       F    PRE     p
----- --------------- | ------------ --- ------------ ------- ------ -----
Model (error reduced) | 33777630.163   1 33777630.163 322.263 0.6494 .0000
Error (from model)    | 18237621.747 174   104813.918
----- --------------- | ------------ --- ------------ ------- ------ -----
Total (empty model)   | 52015251.909 175   297230.011
```

::::::::: { .choices }

- The `FTMade_model`'s PRE is less than the `Points_model`'s PRE.
- The `FTMade_model`'s SS model is less than the `Points_model`'s SS model.
- The `Points_model`'s SS error is less than the `FTMade_model`'s SS error.
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_12 }
:::::: { #b88a2c89-2d19-4c6c-9881-97bc53b46457 .qti-question .multiple-choice points="1" }

12\. Why is the SS Total the same value for the `FTMade_model` and the `Points_model`?

::::::::: { .choices }

- Both are based on the residuals from the mean of the same explanatory variable.
- [Both are based on residuals from the mean of the same outcome variable.]{ .correct }
- All models that use the same data frame will have the same SS total.
- Both models are based on the same number of values (n = 176).

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_13 }
:::::: { #f15eb277-6032-4acb-ad1c-3cafea92294a .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: Mins ~ Points

                                   SS  df           MS       F    PRE     p
----- --------------- | ------------ --- ------------ ------- ------ -----
Model (error reduced) | 33777630.163   1 33777630.163 322.263 0.6494 .0000
Error (from model)    | 18237621.747 174   104813.918
----- --------------- | ------------ --- ------------ ------- ------ -----
Total (empty model)   | 52015251.909 175   297230.011
```

13\. Which of the following is the correct interpretation of MS Total (297,230) in the supernova table above?

::::::::: { .choices }

- This is, roughly, the total number of points in the data frame.
- This is, roughly, the total number of squared means based on the empty model.
- [This is, roughly, the average squared residual from the mean.]{ .correct }
- This is, roughly, the standard deviation from the mean.

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_14 }
:::::: { #05ae49f2-1193-4015-a51a-5e463e9b2989 .qti-question .multiple-choice points="1" }

```
Analysis of Variance Table (Type III SS)
Model: Mins ~ Points

                                   SS  df           MS       F    PRE     p
----- --------------- | ------------ --- ------------ ------- ------ -----
Model (error reduced) | 33777630.163   1 33777630.163 322.263 0.6494 .0000
Error (from model)    | 18237621.747 174   104813.918
----- --------------- | ------------ --- ------------ ------- ------ -----
Total (empty model)   | 52015251.909 175   297230.011
```

14\. Which of the following is the correct interpretation of PRE (0.65) in the supernova table above?

::::::::: { .choices }

- 65% of the players' minutes in the data frame can be predicted with their `Points.`
- [65% of the SS from the empty model can be explained by adding `Points` to the complex model.]{ .correct }
- 65% of the `Points` model can be proportionally reduced by the empty model.
- The `Points` model's SS total will be 65% of the SS total from the empty model.

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_15 }
:::::: { #cde245d4-c7a8-4819-b1a8-77d65aff6a27 .qti-question .essay points="1" max-words="200" }

```
Analysis of Variance Table (Type III SS)
Model: Mins ~ Points

                                   SS  df           MS       F    PRE     p
----- --------------- | ------------ --- ------------ ------- ------ -----
Model (error reduced) | 33777630.163   1 33777630.163 322.263 0.6494 .0000
Error (from model)    | 18237621.747 174   104813.918
----- --------------- | ------------ --- ------------ ------- ------ -----
Total (empty model)   | 52015251.909 175   297230.011
```

15\. Do these data demonstrate that when a player amasses more points, this causes the coaches and other decision makers to give them more time to play? Why or why not?

::::::
:::

::: { .qti-item #B4_Review1_16 }
:::::: { #4ab89b48-68a3-4b84-a8a1-ddbeebacc50a .qti-question .multiple-choice points="1" }

We use this code to calculate the correlation coefficient (Pearson's *r*) for `Mins` and `Points:`

```
cor(Mins ~ Points, data = NBAPlayer2011)
```

16\. What have we found?

::::::::: { .choices }

- A measure of how tight the data points are around the regression line
- The slope of the regression line between the standardized `Mins` and `Points`
- The strength of a bivariate relationship
- [All of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_17 }
:::::: { #a4d91bf8-ad21-416a-b74f-e71eeaa0e3b6 .qti-question .multiple-choice points="1" }

17\. If you were to calculate the sum of the residuals from the empty model of `Mins`, what would it be?

::::::::: { .choices }

- Less than the sum of the residuals from the `Points_model` of Mins
- More than the sum of the residuals from the `Points_model` of Mins
- [0]{ .correct }
- It's impossible to tell

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_18 }
:::::: { #b861e338-0913-4340-a90b-c3d0cb52dd80 .qti-question .multiple-choice points="1" }

18\. Which of these values will be the same if we create two models with these lines of R code:

```
Points11_model <- lm(Min ~ Points, data = NBAPlayers2011)
Points15_model <- lm(Min ~ Points, data = NBAPlayers2015)
```

::::::::: { .choices }

- The SS total for both these models will be the same, because they have the same outcome variable.
- The SS model for both these models will be the same because they have the same explanatory variable.
- The best-fitting estimate of the empty model will be the same because it will be the mean number of minutes played.
- [None of these values (SS total, SS model, mean) will be the same.]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_19 }
:::::: { #7ea62855-7e85-47eb-90a4-46466e305d2d .qti-question .multiple-choice points="1" }

19\. Based on these scatter plots, which season had a higher correlation between minutes played and points scored?

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/dJ7bSbVH.png" class="lrn-image-center" width="700" height="233" alt="A scatter plot of the distribution of Mins by Points in NBAPlayers2011 on the left. A scatter plot of the distribution of Mins by Points in NBAPlayers2015 on the right." />

::::::::: { .choices }

- [2011]{ .correct }
- 2015
- Impossible to tell without calculations
- The correlation looks perfectly equal because they both have a positive slope.

:::::::::

::::::
:::

::: { .qti-item #B4_Review1_20 }
:::::: { #e69e732e-60f7-4d2d-8e58-f29a2c681e2e .qti-question .multiple-choice points="1" }

20\. Let's compare two models. The first model uses `Points` as a quantitative variable to predict `Mins`. We will call this the `Points` model. To create the second model, we use `Points` to create 24 groups (`Points24Group`). So the second model uses `Points24Group` to predict `Mins`.

The supernova tables below show that the PRE for `Points24Group` reduces the total variation in `Mins` by 77%, but the `Points` model reduces it by 65%. Why isn't the `Points24Group` model better than the `Points` model of `Mins`?

```
Analysis of Variance Table (Type III SS)
Model: Mins ~ Points

                                   SS  df           MS       F    PRE     p
----- --------------- | ------------ --- ------------ ------- ------ -----
Model (error reduced) | 33777630.163   1 33777630.163 322.263 0.6494 .0000
Error (from model)    | 18237621.747 174   104813.918
----- --------------- | ------------ --- ------------ ------- ------ -----
Total (empty model)   | 52015251.909 175   297230.011

Analysis of Variance Table (Type III SS)
Model: Mins ~ Points24Group

                                   SS  df          MS      F    PRE     p
----- --------------- | ------------ --- ----------- ------ ------ -----
Model (error reduced) | 39738347.891  23 1727754.256 21.391 0.7640 .0000
Error (from model)    | 12276904.018 152   80769.105
----- --------------- | ------------ --- ----------- ------ ------ -----
Total (empty model)   | 52015251.909 175  297230.011
```

::::::::: { .choices }

- [The F ratio shows that the `Points` model explains more variation per degree of freedom than the `Points24Group`.]{ .correct }
- The SS error is bigger for the `Points` model, which demonstrates its advantage over the `Points24Group` model.
- The `Points` model is far more elegant because the name is shorter and less clunky.
- Trick question! The `Points24Group` model *is* better than the `Points` model because the PRE is bigger, the SS model is bigger, and the SS error is smaller. There are no measures that suggest that the `Points` model is better.

:::::::::

::::::
:::
