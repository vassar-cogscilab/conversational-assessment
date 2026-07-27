## 8.4 The F Ratio

On the prior page we discussed the limits of PRE as a measure of model fit. We can “overfit” a model by adding a lot of parameters to it. PRE alone, therefore, is not a sufficient guide in our quest to document a reduction in error. Yes, it tells us whether we are reducing error. But it does not take into account the *cost* of that reduction. The F ratio provides a solution to this problem, giving us an indicator of the amount of error reduced by a model that **adjusts for the number of parameters it takes to realize the reduction in error**.

To see how the F ratio is calculated, let’s go back to the analysis of variance table for the `Height2Group` model (reprinted below). We have already discussed how we interpret the SS column. Let's now look at the next three columns in the table: df, MS, and F. Just a note: df stands for degrees of freedom, MS stands for Mean Square, and F, well, that stands for the F ratio.

<pre><code>Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height2Group

                               SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   830.880   1 830.880 11.656 0.0699 .0008
Error (from model)    | 11049.331 155  71.286
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | <mark>11880.211 156  76.155</mark>                    </code></pre>

### Degrees of Freedom ($\text{df}$)

Technically, the degrees of freedom is the number of independent pieces of information that went into calculating a parameter estimate (e.g., $b_0$ or $b_1$). But we find it helpful to think about degrees of freedom (also called $df$) as a budget. The more data (represented by $n$) you have, the more degrees of freedom you have, which you can use to estimate more parameters (i.e., build more complex models).

In the `Fingers` data, there are 157 students. When we estimated the single parameter for the empty model (to estimate $b_0$), we used 1 $\text{df}$, leaving a balance of 156 $\text{df}$ left to spend (called $\text{df}_\text{total}$). The `Height2Group` model required us to estimate one additional parameter (to estimate $b_1$), which cost us one additional $\text{df}$. This is why, in the ANOVA table $\text{df}_\text{model}$ is 1. After fitting the `Height2Group` model we are left with 155 $\text{df}$ (also called $\text{df}_{error}$).

::: { .qti-item #b4_FRatio_01 }
:::::: { #90e2beca-2b0b-422c-91bf-d6153137f3f3 .qti-question .multiple-choice points="1" }

Each additional parameter in a model costs:

::::::::: { .choices }

- an additional data set
- [an additional degree of freedom]{ .correct }
- a variable

:::::::::

::::::
:::

### Mean Square ($MS$)

The column labeled MS stands for mean square (also referred to as *variance*).

<pre><code>Analysis of Variance Table (Type III SS)
Model: Thumb ~ Height2Group

                               SS  df      MS      F    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   830.880   1 830.880 11.656 0.0699 .0008
Error (from model)    | 11049.331 155  71.286
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | <mark>11880.211 156  76.155</mark>     </code></pre>

MS is calculated by dividing SS by degrees of freedom for each row of the table.

$$\text{MS}_\text{Model} = \text{SS}_\text{Model}/\text{df}_\text{Model}$$

$$\text{MS}_\text{Error} = \text{SS}_\text{Error}/\text{df}_\text{Error}$$

$$\text{MS}_\text{Total} = \text{SS}_\text{Total}/\text{df}_\text{Total}$$

Starting again with the bottom row, MS Total tells us how much error there is in the outcome variable, per degree of freedom, after fitting the empty model. MS Error tells us how much error still remains, per degree of freedom, after fitting the `Height2Group` model. MS Model represents the reduction in error by the `Height2Group` model per degree of freedom spent beyond the empty model.

::: { .qti-item #b4_FRatio_02 }
:::::: { #d63198d9-e6e7-4f04-9fca-985532d4320f .qti-question .multiple-choice points="1" }

Which of these mean squares (MS) represents the total error from the empty model per degree of freedom left?

::::::::: { .choices }

- MS Model
- MS Error
- [MS Total]{ .correct }

:::::::::

::::::

:::::: { #3ef7509a-ca4b-4930-afdc-2788678c99a3 .qti-question .multiple-choice points="1" }

Which of these mean squares (MS) represents the error from the complex model per degree of freedom left?

::::::::: { .choices }

- MS Model
- [MS Error]{ .correct }
- MS Total

:::::::::

::::::

:::::: { #9569c6f7-83a5-40fe-9b5d-afbc40cb1bfe .qti-question .multiple-choice points="1" }

Which of these mean squares (MS) represents the error reduced by the complex model per degree of freedom spent?

::::::::: { .choices }

- [MS Model]{ .correct }
- MS Error
- MS Total

:::::::::

::::::
:::

### The F Ratio

Now let’s get to the F ratio. In our table, we have produced two different estimates of variance under the `Height2Group` model: MS Model and MS Error.

<pre><code>                               SS  df <mark>     MS      F</mark>    PRE     p
----- --------------- | --------- --- ------- ------ ------ -----
Model (error reduced) |   830.880   1 <mark>830.880 11.656</mark> 0.0699 .0008
Error (from model)    | 11049.331 155 <mark> 71.286       </mark>
----- --------------- | --------- --- ------- ------ ------ -----
Total (empty model)   | 11880.211 156  76.155                    </code></pre>

MS Model tells us the variance of the predictions generated by the `Height2Group` model; MS Error tells us the variance of the residuals after subtracting out the model. The F ratio is calculated as MS Model divided by MS Error:

$$F = \frac{\text{MS}_\text{Model}}{\text{MS}_\text{Error}} = \frac{\text{SS}_\text{Model}/\text{df}_\text{Model}}{\text{SS}_\text{Error}/\text{df}_\text{Error}}$$

This ratio turns out to be a very useful statistic. If there were little effect of `Height2Group` on thumb length we would expect the variance among the model predictions to be approximately the same as the variance of the residuals, resulting in an F ratio of approximately 1. A larger F ratio means a better model.

Another way that we can think about F is as the variance between groups (because the group means are in fact the model predictions) divided by the variance within groups (the variation around the group means). But if the variation across groups is more than the variation within groups, the F ratio would rise above 1.

::: { .qti-item #Ch7_TheF_4 }
:::::: { #a14940d3-d861-4633-9ce1-5d3c9686804e .qti-question .multiple-choice points="1" }

The F ratio for the `Height2Group` model is 11.66. Which is the correct interpretation?

::::::::: { .choices }

- There are at least 11 people whose `Thumb` lengths are better predicted by knowing which `Height` group they are in.
- `Height2Group` has an effect size of 11.66 standard deviations.
- [The variance explained by the model is 11.66 times larger than the leftover variance unexplained by the model.]{ .correct }
- The sum of squared deviations accounted for by the model is 11.66 times larger than the sum of squared deviations leftover after fitting the model.

:::::::::

::::::
:::

Just as variance provides a way to adjust the sum of squares based on degrees of freedom, the F ratio provides a way to take degrees of freedom into account when judging the fit of a model. The F ratio gives us a sense of whether the degrees of freedom that we spent in order to make our model more complicated were "worth it".

::: { .qti-item #Ch7_TheF_5 }
:::::: { #73c62392-7b56-4de2-b38e-43a369b17384 .qti-question .multiple-choice points="1" }

If we took another sample of 157 students and asked them for measurements of thumb and height, would we get the same F ratio?

::::::::: { .choices }

- Yes, certainly.
- [No, this is unlikely.]{ .correct }

:::::::::

::::::

:::::: { #bb7de4aa-6bb7-407d-bf1b-ea74f40b0f85 .qti-question .multiple-choice points="1" }

What is the F ratio?

::::::::: { .choices }

- [A sample statistic]{ .correct }
- A population parameter
- A model

:::::::::

::::::

:::::: { #0e3c78ae-522a-40dd-a3e7-7e68522f4499 .qti-question .multiple-choice points="1" }

Why would we be unlikely to get the same F ratio?

::::::::: { .choices }

- [Because the F ratio is a statistic, just like the mean or PRE. A different sample will likely result in a different statistic.]{ .correct }
- Because with so many data points, calculation errors are likely.
- Because the F ratio is different for each person in your study. We would get a set of 157 new F ratios.
- Because the F ratio is different for each group in our study.  We would get an F ratio for the short group and a different one for the tall group.
- Because the df Total would be different because it is a new sample.

:::::::::

::::::

:::::: { #57d97942-19ed-4b48-bb9e-b1f72832f608 .qti-question .multiple-choice points="1" }

What is the formula for the F ratio?

::::::::: { .choices }

- $F=\frac{MS_{Error}}{MS_{Total}}$
- $F=\frac{MS_{Total}}{MS_{Error}}$
- [$F=\frac{MS_{Model}}{MS_{Error}}$]{ .correct }
- $F=\frac{MS_{Model}}{MS_{Total}}$

:::::::::

::::::
:::

### Another Way of Thinking About the F Ratio

There is another way of thinking about F that makes clearer the relationship between F and PRE. It is represented by this alternative formula for F:

$$F = \frac{\text{PRE}/\text{df}_\text{model}}{(1-\text{PRE})/\text{df}_\text{error}}$$

This formula produces the same result as the formula for F presented in the previous section, but makes it easier to think about the relation between PRE and F.

The numerator of this formula gives us an indicator of how much PRE we have achieved in our model *per degree of freedom* spent (i.e., number of parameters estimated beyond the empty model). In the case of the `Height2Group` model, it would simply be PRE divided by 1 because the model used only one additional degree of freedom ($b_1$) beyond the empty model.

The denominator of the formula tells us how much error could still be reduced (i.e., the remaining unexplained error, $1-\text{PRE}$) *per degree of freedom* if we were to put all still-unused degrees of freedom ($\text{df}_\text{error}$) into the model. In other words, it tells us what the PRE would be, on average, if we just randomly picked a parameter to estimate instead of the one that we picked for our model.

The F ratio, thought of this way, compares the amount of PRE achieved by the particular parameters we included in our model (per parameter) to the average amount of remaining unexplained variation that could have been explained by adding all the possible remaining parameters into the model.

Put another way, the F ratio answers this question: How many times bigger is the PRE obtained by our best fitting model (per degree of freedom spent) than the PRE that could have been obtained (again, per degree of freedom) by spending all of the possible remaining degrees of freedom?

::: { .qti-item #Ch7_TheF_6 }
:::::: { #2872970a-6bab-410c-9d80-fe978728268e .qti-question .multiple-choice points="1" }

$$
F = \frac{MS_{Model}}{MS_{Error}}
$$

$$
F = \frac{PRE/df_{model}}{(1-PRE)/df_{error}}
$$

Which of the following statements is FALSE?

::::::::: { .choices }

- [We need both of these formulas because they give us different values for the F statistic.]{ .correct }
- We need both of these formulas because they express different ways of thinking about the F statistic.
- We need both of these formulas because one shows us the relationship between the F and variance and the other shows us the relationship between F and PRE.
- Both of these formulas show us how the F statistic takes degrees of freedom into account.

:::::::::

::::::

:::::: { #ae504294-9484-4ed9-8bfa-b15d88ea026f .qti-question .multiple-choice points="1" }

Consider this equation:

$$
F = \frac{PRE/df_{model}}{(1-PRE)/df_{error}}
$$

If the F ratio is 1, what does it mean?

::::::::: { .choices }

- The PRE explained by our additional parameter is very special, because 100% of the PRE has been explained by our additional parameter.
- The PRE explained by our additional parameter is somewhat special because the numerator is the same as the denominator, by coincidence.
- [The PRE explained by our additional parameter is not very special because it's about the same as the average amount of PRE that could have been explained by any other parameter.]{ .correct }

:::::::::

::::::
:::
