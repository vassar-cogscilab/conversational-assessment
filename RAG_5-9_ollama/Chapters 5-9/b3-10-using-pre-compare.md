## 7.10 Using Proportional Reduction in Error (PRE) to Compare Two Models

We have now quantified how much variation has been explained by our model: 1,334 square millimeters. But is that a lot of explained variation, or just a little? It would be easier to understand if we knew the *proportion* of total error that has been reduced rather than the raw amount of error reduced measured in $mm^2$.

If you take another look at the `supernova()` table (reproduced below) for the `Gender_model`, you will see a column labeled PRE. PRE stands for *Proportional Reduction in Error*.

<pre><code>Analysis of Variance Table (Type III SS)
Model: Thumb ~ Gender

                               SS  df       MS      F    <mark>PRE</mark>     p
----- --------------- | --------- --- -------- ------ ------ -----
Model (error reduced) |  1334.203   1 1334.203 19.609 <mark>0.1123</mark> .0000
Error (from model)    | 10546.008 155   68.039
----- --------------- | --------- --- -------- ------ ------ -----
Total (empty model)   | 11880.211 156   76.155
</code></pre>

PRE is calculated using the sums of squares. It is simply SS Model (i.e., the sum of squares reduced by the model) divided by SS Total (or, the total sum of squares in the outcome variable under the empty model). We can represent this in a formula:

$$\text{PRE}=\frac{\text{SS}_\text{Model}}{\text{SS}_\text{Total}}$$

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_10_UsingProp_1.jpg" width=80% alt="Venn diagram of the Gender Model of Thumb represented as a single teal circle, with a portion of the circle filled in white with teal lines labeled as PRE equals SS Model divided by SS Total." /></p>

When we calculate PRE this way we are comparing a complex model (e.g., the gender model) to the empty model. Based on this formula, PRE can be interpreted as **the proportion of total variation in the outcome variable that is explained by the explanatory variable**. It tells us something about the overall strength of our statistical model. For example, in the `Fingers` dataset , the effect of `Gender` on `Thumb` accounts for .11 (11%) of the variation in thumb length. Not too shabby.

It is important to remember that SS Model in the numerator of the formula above represents the *reduction* in error when going from the empty model to the more complex model, which includes an explanatory variable. To make this clearer we can rewrite the above formula like this:

$$\text{PRE}=\frac{(\text{SS}_\text{Total} - \text{SS}_\text{Error})}{\text{SS}_\text{Total}}$$

The numerator of this formula starts with the error from the *simple* (empty) model (SS Total), and then subtracts the error from the *complex* model (SS Error) to get the error reduced by the complex model. Dividing this reduction in error by the SS Total yields the *proportion* of total error in the empty model that has been reduced by the complex model.

::: { .qti-item #Ch7_PRE_4 }
:::::: { #d9b0465c-ae85-4b8b-8d98-3532c35083a4 .qti-question .multiple-choice points="1" }

If you have two models for the same outcome variable, one more complex than the other, which will usually have the larger Sum of Squares Error?

::::::::: { .choices }

- The complex model
- [The simple model]{ .correct }
- Their errors would be the same
- It's impossible to tell

:::::::::

::::::
:::

The PRE in the ANOVA table above (.11) represents a comparison of the gender model to the empty model, but PRE more generally can represent a comparison of *any* complex model to one that is simpler. Toward this end, we will add a version of the same formula that is more general:

$$\text{PRE}=\frac{(\text{SS}_\text{Error from Simple Model} - \text{SS}_\text{Error from Complex Model})}{\text{SS}_\text{Error from Simple Model}}$$

Just as a note: PRE goes by other names in other traditions. In the ANOVA tradition (Analysis of Variance) it is referred to as $\eta^2$, or *eta squared*. In an upcoming chapter, we will introduce the same concept in the context of regression, where it is called $R^2$. For now all you need to know is: these are different terms used to refer to the same thing, in case anyone asks you.

::: { .qti-item #Ch7_PRE_1 }
:::::: { #dea04179-1336-48eb-95a3-91c6eef38d9a .qti-question .multiple-choice points="1" scoring="partial" }

Which is true about PRE? (Check all that apply.)

::::::::: { .choices }

- PRE is in the units of the outcome variable (e.g., mm) rather than squared units (squared mm).
- [PRE ranges from 0 to 1. A proportion of the total cannot go beyond the total (i.e., over 1).]{ .correct }
- [PRE can be thought of as the proportion of explained variation.]{ .correct }
- PRE can be thought of as the proportion of leftover or unexplained variation.
- PRE can be thought of as $SS_{Total}-SS_{Error}$

:::::::::

::::::
:::

::: { .qti-item #b3_UsingPRE_01 }
:::::: { #78b8f10d-87db-4939-bab3-2be45178d9be .qti-question .multiple-choice points="1" }

What does PRE mean?

::::::::: { .choices }

- The number of square mm explained by the model
- [The proportion of variation explained by the model]{ .correct }
- The proportion of variation unexplained by the model
- The sum of squared error explained by the model

:::::::::

::::::
:::
