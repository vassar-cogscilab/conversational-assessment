## 7.3 GLM Notation for the Group Model

For most of us humans, we are content to describe the `Gender` model simply as two means. But as with the empty model, it will be helpful to learn how a two-group model is represented in the notation of the General Linear Model, especially as we develop more complicated models.

### The `Gender` Model Using GLM Notation

The full GLM equation for the `Gender` model incorporates both $b_0$ and $b_1$. There are actually a few ways you could write this model but we will write the model like this:

$$Y_i=b_0+b_1X_i+e_i$$

We can also write it in a way more specific to the `Gender` model of `Thumb` like this:

$$\text{Thumb}_i=b_0+b_1\text{Gendermale}_i+e_i$$

Using the output from `lm()`, we can substitute the estimates into the model.

```
Call:
lm(formula = Thumb ~ Gender, data = Fingers)

Coefficients:
(Intercept)   Gendermale
     58.256        6.447
```

::::::::: { .qti-item #b3_GLM_01_r5.8 }
:::::: { #a71d0203-e293-48f1-8633-2047f1ca1457 .qti-question .multiple-choice
points="1" }
Using the output from `lm()`, we can fill in the model estimates.

Call:
lm(formula = Thumb ~ Gender, data = Fingers)

```
Coefficients:
     (Intercept)    Gendermale
          58.256         6.447
```

Which of the following shows us the best-fitting `Gender` model? (Check all
that apply.)
::: choices

- $\text{Thumb}_i=6.4+58.3\text{Gendermale}_i+e_i$
- $\text{Thumb}_i=6.4+6.4\text{Gendermale}_i+e_i$
- [$\text{Thumb}_i=58.3+6.4\text{Gendermale}_i+e_i$]{.correct}
- $\text{Gender}_i=58.3+6.4\text{Thumb}_i+e_i$
- [$Y_i=58.3+6.4X_i+e_i$]{.correct}
:::
::::::
:::::: { #78c22c90-ecc7-4527-8972-0d7e94b2a468 .qti-question .association
points="1" }
Match the interpretation of each element to the GLM notation.

$$Y_i = b_0 + b_1 X_i + e_i$$

::: associations

- [$Y_i$]{match="1"}
- [$b_0+b_1X_i$]{match="2"}
- [$e_i$]{match="3"}
:::
::: choices

1. the thumb length of each student
2. the model's predicted thumb length
3. error, how different the prediction is from the actual thumb length
:::
::::::
:::::::::

It's important to notice, first, that both the empty model and the two-group `Gender` model start with $Y_i$ to the left of the equals sign and end with $e_i$. In both models, $Y_i$ represents the thumb length for student *i*, and $e_i$ represents the error or residual between the predicted thumb length and the actual thumb length for student *i*.

For the two-group model, the **MODEL** part of **DATA = MODEL + ERROR** is now more complicated: $b_0+b_1X_i$ instead of simply $b_0$ (for the empty model). In both cases, though, the model can be thought of as **a function that produces a predicted value on the outcome variable for each observation** (in this case, student).

Note that the $b_0$ parameter estimate has a different meaning than it does in the empty model. It is the first parameter in both models. But for the empty model, which only has one parameter, it represents the mean of `Thumb` for the whole sample of data, whereas for the two-group model (with two parameters), it represents the mean of the first group (in this case, `female`).

You might find it confusing to use the same symbol to represent two different ideas. But this flexibility is what makes the General Linear Model so powerful and so... *general*.

Unlike the empty model, this more complicated model ($b_0 + b_1X_i$) is able to generate two different predictions depending on whether a student is female or male.

::: { .qti-item #b3_GLM_02 }
:::::: { #1bb080d7-4862-434e-b9b1-00234f24da9e .qti-question .multiple-choice points="1" }

Based on what you know about $b_0$ and $b_1$ so far, what does the model use to predict the thumb length of a female student?

::::::::: { .choices }

- [$b_0$]{ .correct }
- $b_1$
- $b_0 + b_1$
- $b_0 * b_1$

:::::::::

::::::

:::::: { #5d0aea9c-0c77-4a2b-a9fe-ceacfc5450db .qti-question .multiple-choice points="1" }

Based on what you know about $b_0$ and $b_1$ so far, what does the model use to predict the thumb length of a male student?

::::::::: { .choices }

- $b_0$
- $b_1$
- [$b_0 + b_1$]{ .correct }
- $b_0 * b_1$

:::::::::

::::::
:::

### Interpreting $X_i$

We have developed the idea that $b_0$ is the mean of the first group, and $b_0 + b_1$ is the mean of the second group. But the function that results in a predicted value for each observation under the two-group model is this: $b_0 + b_1 X_i$. In this model, what does the $X_i$ do?

It turns out we need the $X_i$ in order for the model to actually compute two predicted scores. Here's how it works. $X_i$ represents the grouping variable – our explanatory variable, `Gender` – but in a special way. It is called a *dummy variable*, which means that R creates it specifically to make the model work.

R takes the variable `Gender` and recodes it into a new variable ($X_i$) that can only be assigned one of two values: 0 or 1. In the two-group model, $X_i$ is coded 1 if the student is in the second group (`male`), and it is coded 0 if the student is **not** in the second group (i.e., **not** `male`).

::: { .qti-item #b3_GLM_03 }
:::::: { #d2ef12a2-eb0d-4c10-989c-79effe189659 .qti-question .multiple-choice points="1" }

If a student is **not** in `male` in this data set, what group is the student in?

::::::::: { .choices }

- [The student is female.]{ .correct }
- The student does not have a thumb.
- It's not possible to know.

:::::::::

::::::
:::

Although in this data, saying a student is **not** male is the same as saying the student **is** female, it's important to think of $X_i = 0$ as meaning the student is **not** male. Keeping this subtle distinction in mind will help us understand how dummy variables work when we have models with more than 2 groups.

The reason the $b_0$ estimate is called `Intercept` in the `lm()` output is because it is the predicted thumb length when $X_i$ is equal to 0 – in other words, when the Gender is *not* male. The estimate that R called `Gendermale` ($b_1$), by this line of reasoning, is kind of like the slope of a line. It is the adjustment in predicted thumb length for a 1 unit increase in `Gender`.

::: { .qti-item #b3_GLM_04 }
:::::: { #3feafa2b-33b0-449c-8f32-08f79f0c2010 .qti-question .multiple-choice points="1" }

In the `Gender` model, $b_0+b_1X_i$, which of these describes $b_0$ (or `Intercept` in the R output)?

::::::::: { .choices }

- [what the model should predict when $X_i=0$]{ .correct }
- what the model should predict when $X_i=1$
- what the model should predict no matter what $X_i$ is
- the adjustment to add on for a 1 unit increase in $X_i$

:::::::::

::::::

:::::: { #43d14657-9f16-4c81-8e81-f5c41bdfa4cf .qti-question .multiple-choice points="1" }

Which of these is the definition of $b_1$ (or `Gendermale` in the R output) for the `Gender` model?

::::::::: { .choices }

- what the model should predict when $X_i=0$
- what the model should predict when $X_i=1$
- what the model should predict no matter what $X_i$ is
- [the adjustment to add onto $b_0$ for a 1 unit increase in $X_i$]{ .correct }

:::::::::

::::::
:::
