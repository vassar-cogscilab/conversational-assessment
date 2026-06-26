### 9.2 Specifying the Height Model with GLM Notation

Here is how we specify a regression model in which we have a single quantitative explanatory variable (such as `Height`):

$$Y_i=b_0+b_1X_i+e_i$$

It might be useful to compare this notation to that used in the previous chapter to specify the two-group model (such as `Height2Group`):

$$Y_i=b_0+b_1X_i+e_i$$

::: { .qti-item #b5_Notation_01 }
:::::: { #8bf45ba6-03b9-4cf8-ac0f-484d7ea4f3e9 .qti-question .essay points="1" max-words="100" }

What is different in the GLM notation for these two models? What is similar?

::::::::: { .feedback }

The GLM notation is identical for the two models! Both the regression model (e.g., `Height_model`) and two-group model (e.g., `Height2Group_model`) are two-parameter models, meaning that we will be estimating two parameters: $b_0$ and $b_1$.

:::::::::

::::::
:::

The fact that the same notation represents both models is what is so beautiful about the General Linear Model. It is simple and elegant and can be applied across a wide variety of situations, including situations with categorical or quantitative explanatory variables. Although both models are specified using the same notation, the interpretation of the notation varies from situation to situation.

::: { .qti-item #b5_Notation_02 }
:::::: { #2d9a03c0-7063-4996-bca5-cc9c6c71d06c .qti-question .multiple-choice points="1" }

Both the `Height2Group` and the `Height` models of `Thumb` can be represented with the same GLM notation: $Y_{i}=b_{0}+b_{1}X_{i}+e_{i}$.

Which part of the GLM notation represents the outcome variable (<span style="font-size: 12.6px; white-space: nowrap; background-color: rgb(249, 242, 244);">Thumb</span>) in both models?

::::::::: { .choices }

- [$Y_i$]{ .correct }
- $X_i$
- $e_i$

:::::::::

::::::

:::::: { #fc05afdb-86f2-4b7d-8b22-2ddf1fd7ff07 .qti-question .multiple-choice points="1" }

Which part of the GLM notation represents error (also called residuals) in both models?

::::::::: { .choices }

- $Y_i$
- $X_i$
- [$e_i$]{ .correct }

:::::::::

::::::

:::::: { #1bc8bc8a-b4d1-49ef-9850-cece0ccad569 .qti-question .multiple-choice points="1" }

Which part of the GLM notation represents the explanatory variable (either `Height` or `Height2Group`)?

::::::::: { .choices }

- $Y_i$
- [$X_i$]{ .correct }
- $e_i$

:::::::::

::::::
:::

In the `Height2Group` model, $X_i$ was dummy coded as either 0 or 1. The 1 did not represent a quantity, just whether the student was tall or not. In the `Height` model, the $X_i$ literally is coded as the measured height in inches of the student.

Coding $X_i$ in these different ways leads to different, but related, interpretations of the $b_1$ coefficient.

::: { .qti-item #b5_Notation_03 }
:::::: { #49ae9ab2-777e-48c7-a15f-d97eac60cd17 .qti-question .multiple-choice points="1" }

In the group model (e.g. `Height2Group` model), the $b_1$ coefficient represents:

::::::::: { .choices }

- the mean difference between the two groups
- the adjustment that gets added to $b_0$ in order to get the mean thumb length of tall students.
- the adjustment added to $b_0$ when $X_{i}$ is equal to 1
- [all of the above]{ .correct }

:::::::::

::::::
:::

::: { .qti-item #b5_Notation_04 }
:::::: { #ce1ca05b-953f-4c1c-b617-59c46409215c .qti-question .multiple-choice points="1" }

In the group model (e.g., `Height2Group` model), $b_1$ was the amount by which the predicted thumb length should be adjusted when `Height2Grouptall` increased by 1 (i.e., went from 0 to 1). Reasoning by analogy, what does $b_1$ mean in the `Height` model?

::::::::: { .choices }

- The predicted thumb length when height = 1
- [The adjustment that should be made to predicted thumb length when height increases by 1]{ .correct }
- The adjustment that should be made to predicted thumb length when height group increases by 1

:::::::::

::::::
:::

In the regression model, $b_1$ still represents an adjustment to $b_0$, but this time it is the amount of adjustment to make for every 1-unit change in `Height`. This is the definition of the slope of a line: the amount of "rise" for each one unit of “run”, i.e., how much $Y_i$ changes for each one unit change in $X_i$. $b_1$ is, in fact, the slope of the best-fitting regression line.

In both models, the $b_0$ coefficient represents an intercept, i.e., the value of $Y_i$ when $X_i = 0$. But in the `Height2Group` model, when $X_i = 0$ it simply means that the student is short, which is the reference category for `Height2Group`. In the `Height` model, if $X_i$ were equal to 0 it would literally mean that the student has a height of 0 inches! Zero is not a common sense value for $X_i$ when $X_i$ is representing `Height`, but the model can still make a prediction for such a nonsensical student.

::: { .qti-item #b5_Notation_05 }
:::::: { #89f6c132-3b75-4db8-96b9-7993aac28b20 .qti-question .multiple-choice points="1" }

What would this model predict for a student who had a height of 0?

::::::::: { .choices }

- [$b_0$]{ .correct }
- $b_1$
- $b_0 + b_1$

:::::::::

::::::
:::

  ::::::::: { .qti-item #Ch8_Regression_6 }
  :::::: { #e15e4ab4-4196-4e8f-98ab-9f021b2b4524 .qti-question .association
  points="1" }
  Let's interpret this equation in the context of `Thumb` and `Height`.

  $$Y_i=b_0+b_1X_i+e_i$$

  ::: associations

- [$Y_i$]{match="6"}
- [$b_0$]{match="8"}
- [$b_1$]{match="2"}
- [$X_i$]{match="3"}
- [$e_i$]{match="7"}
  :::
  ::: choices

  1. The increment to add on for the other group
  2. The increment to add on for each unit of $X_i$
  3. Height (in inches)
  4. Which height group someone is in
  5. Mean thumb length for one of the groups
  6. Thumb length (in mm)
  7. How "off" the model's prediction is (also called the residual)
  8. Thumb length when $X_i$ is 0
  :::
  ::::::
  :::::::::

### Connection to Algebra

In algebra, a straight line is often represented by the equation $y = mx+ b$, where the $m$ is called the slope and the $b$ is called the y-intercept.

In statistics, we use that same linear equation, but we switch it around so the intercept comes first ($y = b+mx$), and we use different letters to represent the intercept and slope ($b_0$ and $b_1$, respectively).

  ::::::::: { .qti-item #b5_Notation_06 }
  :::::: { #f2771b1a-eed9-4960-b524-7c21df628512 .qti-question .association
  points="1" }
  Note that there is a similarity between the GLM notation and the equation of a
   line.

  $$Y_i=b_0+b_1X_i+e_i$$

  $$y=mx+b$$

  Which parts of the GLM notation go with the parts in the equation for a line?
  ::: associations

- [$Y_i$]{match="2"}
- [$b_0$]{match="1"}
- [$b_1$]{match="4"}
- [$X_i$]{match="3"}
  :::
  ::: choices

  1. *b*
  2. *y*
  3. *x*
  4. *m*
  :::
  ::::::
  :::::::::

Fitting a regression model is a matter of finding the particular line (i.e., slope and intercept) that best fits the data (i.e., that minimizes the sum of squared errors).
