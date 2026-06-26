## 9.7 Assessing Model Fit with PRE and F

### Comparing PRE for the Two Models

Let’s go back to the ANOVA tables for the `Height2Group` and `Height` models.

::: { .alert .alert-info }
**Height2Group Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height2Group

                               SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   830.880   1 830.880 11.656 0.0699 .0008
Error (from model)    | 11049.331 155  71.286
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11880.211 156  76.155
```

::: { .alert .alert-info }
**Height Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height

                               SS  df       MS      F    PRE     p
----- --------------- | --------- --- -------- ------ ------ -----
Model (error reduced) |  1816.862   1 1816.862 27.984 0.1529 .0000
Error (from model)    | 10063.349 155   64.925
----- --------------- | --------- --- -------- ------ ------ -----
Total (empty model)   | 11880.211 156   76.155
```

::: { .qti-item #Ch8_Assessing_4 }
:::::: { #b93d4a0d-04c9-4b7f-a7ce-c29957c2fe44 .qti-question .multiple-choice points="1" }

Compare PRE (Proportional Reduction in Error) for the two models (the two-group model vs. the regression model). Which model has a higher PRE?

::::::::: { .choices }

- `Height2Group`
- [`Height`]{ .correct }

:::::::::

::::::

:::::: { #697dd30d-0e57-4a43-8ec0-73d64584f459 .qti-question .multiple-choice points="1" scoring="partial" }

What does this number (e.g., PRE = .15) mean? (Check all that apply.)

::::::::: { .choices }

- Proportion of error reduced from the `Height` model compared to the `Height2Group` model
- [Proportion of error reduced from the empty model by adopting the `Height` model]{ .correct }
- [Proportion of error explained by the `Height` model compared to the empty model]{ .correct }
- Proportion of error left unexplained from the `Height` model

:::::::::

::::::

:::::: { #dd401406-d35f-47a7-a22c-d7fbaf55881d .qti-question .multiple-choice points="1" scoring="partial" }

How is PRE calculated for the regression model? (Check all that apply.)

::::::::: { .choices }

- [(SS Total - SS Error) / SS Total]{ .correct }
- [SS Model / SS Total]{ .correct }
- SS Error / SS Total

:::::::::

::::::

:::::: { #b8e55530-5f9a-4ec2-b767-6871af63fb01 .qti-question .multiple-choice points="1" }

What is common in the calculation of PRE across the two models?

::::::::: { .choices }

- [SS Total is the same, but SS Error and SS Model differ.]{ .correct }
- SS Total and SS Error are the same, but SS Model differs.
- SS Model and SS Error are the same, but SS Total differs.

:::::::::

::::::

:::::: { #0e64dc5f-a508-48d3-b5b5-f5667c68e8a6 .qti-question .essay points="1" max-words="100" }

Why is the PRE larger in the `Height` model compared to the `Height2Group` model?

::::::
:::

**PRE has the same interpretation in the context of regression models as it does for the group models. As we have pointed out, the total sum of squares is the same for both models. And the PRE is obtained in both cases by dividing SS Model by SS Total**.

Many statistics textbooks emphasize the difference between ANOVA models (such as our two- and three-group models) and regression models (such as our height model). But in fact, the two types of models are fundamentally the same and easily incorporated into the General Linear Model framework. In the context of regression, PRE is sometimes referred to as $R^2$ (R-squared).

**For the models we are considering, no matter what you call it, the interpretation of PRE is identical: it is the proportion of error reduced by the complex model compared with the empty model. Or, put another way, the proportion of variation explained by the model.**

::: { .qti-item #Ch8_Assessing_5 }
:::::: { #0a5147e8-b36a-4314-822e-b0afa0044f94 .qti-question .multiple-choice points="1" scoring="partial" }

What does it mean that PRE is larger for the `Height` model than for the `Height2Group` model? (Check all that apply.)

::::::::: { .choices }

- [The `Height` model has less residual error than the `Height2Group` model.]{ .correct }
- [The `Height` model explains more variation than the `Height2Group` model.]{ .correct }
- [The `Height` model results in predictions that are closer to the data than the `Height2Group` model.]{ .correct }
- [About 15% of the variation in `Thumb` length is explained by variation in height, compared to 7% being explained by which which height group someone falls into (short vs. tall).]{ .correct }
- The `Height` model leaves more error unexplained than the `Height2Group` model.
- The data used to fit the `Height` model has more proportional variation than the data used to fit the `Height2Group` model.

:::::::::

::::::
:::

### Using the F Ratio for Comparing Models

Finally, we can also assess model fit by looking at the F ratio, which we introduced in a previous chapter. Whereas PRE is a proportion based on sums of squares, the F statistic is a ratio of two variances (also called mean squares or MS), obtained by dividing SS by df. The numerator is the MS Model, which indicates the amount of variation explained by the model per degree of freedom spent; and the denominator is MS Error, which indicates the amount of variation left unexplained by the model per degree of freedom remaining.

#### More on F Versus PRE

To get a more concrete idea of why this matters, let’s compare yet another group model to the `Height` model: the `Height10Group` model. The following R code creates a new grouping variable called `Height10Group` (inside the `Fingers` data frame), which divides the sample into 10 equally-sized groups based on `Height`, and then makes it a factor.

```
Fingers$Height10Group <- ntile(Fingers$Height, 10)
Fingers$Height10Group <- factor(Fingers$Height10Group)
```

::: { .qti-item #Ch8_Assessing_6 }
:::::: { #afc64f11-efdc-44d5-afa3-aa712fef955d .qti-question .multiple-choice points="1" }

Why did we need to turn the variable `Height10Group` into a factor?

::::::::: { .choices }

- So it would come out even
- [So lm() would not treat it as a quantitative variable]{ .correct }
- So we could plot `Thumb` as a function of it

:::::::::

::::::
:::

We fit a group model of `Thumb` using `Height10Group`, and placed it on the jitter plot of the 10 groups. The model's predictions are shown as 10 horizontal line segments, each representing the mean of each group.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/bpk5t5SP.png" width=80% alt="A scatter plot of the distribution of Thumb by Height10Group with horizontal line segments showing the group means for the 10 groups." /></p>

Here's the code used to fit a model of `Thumb` using `Height10Group`, and produce the ANOVA table.

```
Height10Group_model <- lm(Thumb ~ Height10Group, data = Fingers)
supernova(Height10Group_model)
```

Below are the `supernova()` tables for three models: `Height2Group`, `Height10Group`, and `Height`. The outcome variable for all three models, again, is `Thumb`.

::: { .alert .alert-info }
**Height2Group Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height2Group

                               SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   830.880   1 830.880 11.656 0.0699 .0008
Error (from model)    | 11049.331 155  71.286
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11880.211 156  76.155
```

::: { .alert .alert-info }
**Height10Group Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height10Group

                               SS  df      MS     F    PRE     p
----- --------------- | --------- --- ------- ----- ------ -----
Model (error reduced) |  1920.474   9 213.386 3.149 0.1617 .0017
Error (from model)    |  9959.737 147  67.753
----- --------------- | --------- --- ------- ----- ------ -----
Total (empty model)   | 11880.211 156  76.155
```

::: { .alert .alert-info }
**Height Model**
:::

```
Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height

                               SS  df       MS      F    PRE     p
----- --------------- | --------- --- -------- ------ ------ -----
Model (error reduced) |  1816.862   1 1816.862 27.984 0.1529 .0000
Error (from model)    | 10063.349 155   64.925
----- --------------- | --------- --- -------- ------ ------ -----
Total (empty model)   | 11880.211 156   76.155
```

::: { .qti-item #Ch8_Assessing_7 }
:::::: { #a045fcd6-4104-4e56-8829-b2fe4fc222c0 .qti-question .multiple-choice points="1" }

If we just compare PREs between these three models, which model explains more of the variation in thumb length?

::::::::: { .choices }

- `Height2Group` model
- [`Height10Group` model]{ .correct }
- `Height` model

:::::::::

::::::

:::::: { #6a6e729a-e919-4ac9-85e5-dde048c8ba41 .qti-question .multiple-choice points="1" }

Compare the degrees of freedom (df) for these models. Which model uses the most df?

::::::::: { .choices }

- `Height2Group` model
- [`Height10Group` model]{ .correct }
- `Height` model

:::::::::

::::::
:::

To see how many degrees of freedom are used by a model, look at the **df** column in the row that says "Model (error reduced)." Notice that the `Height10Group` model costs us nine degrees of freedom, eight more than either the `Height2Group` model or the `Height` model (they each just spend one).

What do we get for these extra degrees of freedom? When we go from the `Height2Group` model to the `Height` model, PRE goes up from .07 to .15 without spending any additional degrees of freedom. That seems like a no brainer!

The `Height10Group` model produces the highest PRE of all the models (.16), but it costs us eight additional degrees of freedom. A model that predicts 10 different group means is not very elegant compared to one with just a y-intercept and slope. Here’s what the `Height10Group` model would look like in GLM notation:

$$Y_i=b_0+b_1X_{1i}+b_2X_{2i}+b_3X_{3i}+b_4X_{4i}+b_5X_{5i}+b_6X_{6i}+b_7X_{7i}+b_8X_{8i}+b_9X_{9i}+e_i$$

::: { .qti-item #Ch8_Assessing_8 }
:::::: { #71a7a812-dbe2-4241-8c44-e459a37da95e .qti-question .multiple-choice points="1" }

Which part of the equation above is the model?

::::::::: { .choices }

- $Y_i = b_0 + b_1X_{1i}$
- $b_0 + b_1X_{1i}$
- [$b_0 + b_1X_{1i} + b_2X_{2i} + b_3X_{3i} + b_4X_{4i} + b_5X_{5i} + b_6X_{6i} + b_7X_{7i} + b_8X_{8i} + b_9X_{9i}$]{ .correct }

:::::::::

::::::
:::

Compare that jumble of symbols with the `Height` model:

$$b_0+b_1X_i$$

That’s a truly elegant model! True, it doesn’t reduce error quite as much as the `Height10Group` model. But the regression model has a PRE of .15 with just two parameters ($b_0$ and $b_1$) while the 10 group model estimates 8 more parameters ($b_2$ to $b_9$) to get to a PRE of just .16. Elegant models add a lot of explanatory power without estimating a lot of parameters unnecessarily.

#### Comparing F Ratios for the Three Models

The `supernova()` function also calculated the F ratio for each of the three models. As we can see from the table below, the F ratio paints a different picture of the three models than we get by looking only at PRE.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th align="left">Model (Group)</th>
            <th align="left" style="width:25%">PRE</th>
            <th align="left" style="width:25%">F Ratio</th>
    </thead>
    <tbody>
        <tr>
            <td><b>Height2Group</b> Model</td>
            <td align="right">.0699</td>
            <td align="right">11.656</td>
        </tr>
        <tr>
            <td><b>Height10Group</b> Model</td>
            <td align="right">.1617</td>
            <td align="right">3.149</td>
        </tr>
        <tr>
            <td><b>Height</b> Model</td>
            <td align="right">.1529</td>
            <td align="right">27.984</td>
        </tr>
    </tbody>
</table>

Going by PRE alone, the `Height10Group` model would appear to be the best one. But when we use F, which incorporates degrees of freedom into our model comparison, the `Height` model is the clear winner, with an F of 27.984. The `Height10Group` model is by far the worst, with an F of 3.149.

::::::::: { .qti-item #Ch8_Assessing_9 }
:::::: { #003ad32f-505d-44b8-82da-77e240f7a2c5 .qti-question .association
points="1" }
Let's review the calculations that go into the F ratio. As discussed in
Chapter 7, the F ratio is based on mean squares (or MS), which is, in essence,
 a variance (a SS divided by degrees of freedom). Just like SS, there are
three different mean squares. Match the appropriate mean squares with their
formulas based on SS and df.
::: associations

- [MS Model]{match="1"}
- [MS Error]{match="3"}
- [MS Total]{match="2"}
:::
::: choices

1. SS Model / df Model
2. SS Total / df Total
3. SS Error / df Error
:::
::::::
:::::: { #e95888a1-c4b8-438f-9642-ad205f639350 .qti-question .multiple-choice
points="1" }
The F ratio is which proportion?
::: choices

- [MS Model / MS Error]{.correct}
- MS Model / MS Total
- MS Error / MS Total
:::
::::::
:::::: { #adc487bd-2f87-496e-9e5f-496c3313cc7c .qti-question .multiple-choice
points="1" }
Why is the F ratio for the `Height` model about 28? (Check all that apply.)
::: choices
- [The SS explained by the model per df is 28 times larger compared to the SS
left unexplained per df.]{.correct}
- [The variance explained by the model is 28 times larger compared to the
variance left unexplained.]{.correct}
- The SS explained by the model is 28 times larger compared to the SS left
unexplained.
- There are 28 more data points predicted by the complex model compared to the
 empty model.
:::
::::::
:::::: { #620ab5d7-95b4-4817-b4b9-61c4ca7460e2 .qti-question .multiple-choice
points="1" }
Why is the F ratio for the `Height` model bigger than for the `Height10Group`
model?
::: choices
- Because the data used for the `Height` model were easier to explain than the
 data used by the `Height10Group` model.
- [Because the `Height` model explains more variation per df used than the
`Height10Group` model.]{.correct}
- Because the `Height` model makes more predictions than the `Height10Group`
model.
- Because the `Height` model exactly predicts 28 more thumb lengths than the
`Height10Group` model.
:::
::::::
:::::::::
