## 7.4 How the Model Makes Predictions

Here's the best-fitting model of thumb length using gender as an explanatory variable:

$$\text{Thumb}_i=b_0+b_1\text{Gendermale}_i+e_i$$

$$\text{Thumb}_i=58.3+6.4\text{Gendermale}_i+e_i$$

Armed with this understanding of how $\text{Gendermale}_i$ (a.k.a. $X_i$) works, you can now use the model to make predictions. If $X_i=1$, then the student is male. In this case, the predicted thumb length would be $b_0+b_1*1$. (A reminder: The asterisk represents multiplication in R so we're using it as a way of notating multiplication in GLM.)

::: { .qti-item #b3_Predictions_01 }
:::::: { #29d4df49-3e0d-41dd-b02c-09a4d8c2c86a .qti-question .multiple-choice points="1" }

If a student is male, then $X_i$ would be coded by R as 1. Which of the following represents how the model would generate a prediction for a male student's thumb length?

::::::::: { .choices }

- [$58.3+(6.4*1)$]{ .correct }
- $58.3+(6.4*0)$
- $58.3*(6.4*58.3)$
- $58.3*0$
- $58.3$

:::::::::

::::::

:::::: { #fae86161-98fc-4422-a920-284fc88b12b5 .qti-question .multiple-choice points="1" scoring="partial" }

If a student is *not* male, then $X_i$ would be coded by R as 0. Which of the following represents the model's prediction for a female student's thumb length? (Check all that apply.)

::::::::: { .choices }

- $58.3+(6.4*1)$
- [$58.3+(6.4*0)$]{ .correct }
- $58.3*(6.4*58.3)$
- $58.3*0$
- [$58.3$]{ .correct }

:::::::::

::::::
:::

If $X_i = 0$, meaning the student is *not* male, then the second parameter estimate won't get added in, because $b_1$ times 0 is equal to 0. And if the second parameter drops out, the prediction would simply be the $b_0$, which is the mean of female thumb lengths.

$X_i$ is a variable, meaning it can take a different value for different students in the data frame. We show that this is a variable by putting a subscript $i$ after the $X$. Each student can either have the value of 0 or 1 for $X_i$ because each student in this dataset is or is not male.

::: { .qti-item #b3_Predictions_02 }
:::::: { #1412c445-bafa-4f95-9573-81896144a409 .qti-question .multiple-choice points="1" }

Consider $b_0$. It does not have the subscript $i$. Can it vary across individual students?

::::::::: { .choices }

- [No, $b_0$ is the mean thumb length of females. It cannot vary across individual students.]{ .correct }
- Yes, $b_0$ can vary across across individual students.

:::::::::

::::::
:::

### How Does R Know Which Gender to Represent with $X_i$?

The answer to this question is: R doesn’t know; it’s just taking whatever group comes first alphabetically (in this case, `female`) and making it the *reference group*. The mean of the reference group is the first parameter estimate ($b_0$ or the *Intercept* in the `lm()` output).

R then takes the second group (in this case, `male`) and represents it with the dummy variable $X_i$. If $X_i$ is coded 1 then the student is `male`. If it is coded 0, then the student is *not* `male`.

Let’s say, just for fun, that you changed the label for `male` to `man` and the label for `female` to `woman` in the data frame. Because `man` comes before `woman` alphabetically, `man` becomes the reference group, and its mean is now the estimate for the intercept ($b_0$).

::: { .qti-item #b3_Predictions_03 }
:::::: { #d0c7579d-d4eb-480d-82ff-ef268750448e .qti-question .multiple-choice points="1" }

In this new hypothetical case where `man` is now the reference group, would the value of $b_1$ be negative or positive?

::::::::: { .choices }

- [Negative, because to go from the `man` group mean to the `woman` mean, we need to adjust it in the negative direction]{ .correct }
- Negative, because $b_1$ changes across individual students
- Positive, because $b_1$ would not change even if the ordering of categories changed

:::::::::

::::::
:::

As long as R knows that a variable is categorical (e.g., a factor), it doesn’t really care how you code it. You can code the categories under `Gender` with any characters you choose (e.g., `female` or `woman`), or with any numbers you choose (e.g, 1 and 2, 0 and 1, or 1 and 500). However you code it, R will take the category that comes first as the intercept ($b_0$) and then the next one as the dummy explanatory variable, which R will code 0 or 1.
