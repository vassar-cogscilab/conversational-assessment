## 7.9 Partitioning Sums of Squares into Model and Error

### DATA = MODEL + ERROR

Statistical modeling is all about explaining variation. SS Total tells us how much total variation there is to be explained. When we fit a model (as we have done with the `Gender` model), that model explains some of the total variation, and leaves some of that variation still unexplained. The part we explain is called SS Model; the part left unexplained, SS Error.

These relationships are visualized in the diagram below: SS Total can be seen as the sum of SS Model (the amount of variation explained by a more complex model) and SS Error, which is the amount left unexplained after fitting the model. Just as **DATA = MODEL + ERROR**, **SS Total = SS Model + SS Error**.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_09_DATA_1.jpg" width=80%  alt="On the left, a single circle represents SS Total from the Empty Model of Thumb. An arrow from that circle points to a Venn diagram of two partially overlapping circles to the right. One circle is labeled as SS Error from the Gender Model of Thumb, and the other circle is labeled as Gender. The intersection where the two circles overlap is labeled as Error Reduced by Gender." /></p>

### Partitioning Sums of Squares

Let's see how this concept works in the ANOVA table for the gender model (reprinted below). Look just at the column labeled SS (highlighted). The two rows associated with the gender model (Model and Error) add up to the row labeled Total (SS Total for the empty model): 1,334 + 10,546 = 11,880.

<pre><code>Analysis of Variance Table (Type III SS)
Model: Thumb ~ Gender

                               SS  df       MS      F    PRE     p
----- --------------- | --------- --- -------- ------ ------ -----
Model (error reduced) |  <mark>1334.203</mark>   1 1334.203 19.609 0.1123 .0000
Error (from model)    | <mark>10546.008</mark> 155   68.039
----- --------------- | --------- --- -------- ------ ------ -----
Total (empty model)   | <mark>11880.211</mark> 156   76.155
</code></pre>

Let's put these numbers back into the Venn diagram of the gender model. SS Total, represented by the whole circle, can be partitioned into two parts: SS Model and SS Error.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_09_DATA_2.jpg" width=80% alt="Venn diagram of the Gender Model of Thumb, represented as a single teal circle labeled as SS Error equals 10,546. A portion of the circle is shaded in white with teal lines and labeled as SS Model equals 1,334." /></p>

The striped part (SS Model, which is 1,334 for the gender model) represents the part of SS Total that is explained by the gender model. Another way to think of it is as the *reduction in error* (measured in sums of squares) achieved by the gender model as compared to the empty model.

### Calculating SS Model

There are two ways to calculate SS Model. One is to simply subtract SS Error (error from the `Gender` model predictions) from SS Total (error around the mean, or the empty model):

$$\text{SS}_\text{Model} = \text{SS}_\text{Total} - \text{SS}_\text{Error}$$

Another way is to calculate the reduction in error from the empty model to the gender model separately for each data point, then square and sum these to get SS Model. As illustrated below for a female student, we take the distance from her predicted score under the gender model to her predicted score under the empty model, then square it. If we do this for each student and then total up the squares we will get SS Model.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_09_Calcuating_SS_Model_01.jpg" width=80%  alt="Jitter plot of Thumb predicted by Gender (female and male), with the empty model overlaid as a blue horizontal line at the mean of thumb, and the Gender model overlaid as red horizontal lines at the mean of each group. A few predictions from each model are highlighted as points along the lines." /></p>

::: { .qti-item #b3_Partitioning_01 }
:::::: { #9ee22ac1-e9d6-4b66-a680-8ffa00f52231 .qti-question .multiple-choice points="1" scoring="partial" }

Which of these statements are true about the distance from each person's predicted score under the gender model to their predicted score under the empty model? (Check all the apply)

::::::::: { .choices }

- [These distances will be the same for all females, and the same for all males.]{ .correct }
- [These distances are represented by the gap between the predictions of the two models (blue and red dots).]{ .correct }
- [These distances are neither the residuals from the empty model nor are they residuals from the gender model.]{ .correct }
- [We can calculate these distances even if we don't know the lengths of the individual students' thumbs.]{ .correct }

:::::::::

::::::

:::::: { #edc57999-c039-4698-a5ab-0ee00debf3ce .qti-question .multiple-choice points="1" }

Which of these lines of R code would return the distances that make up SS Model?

::::::::: { .choices }

- [`predict(Gender_model) - predict(empty_model)`]{ .correct }
- `resid(Gender_model) - resid(empty_model)`
- `supernova(Gender_model) - supernova(empty_model)`
- `predict(Gender_model) - Fingers$Thumb`

:::::::::

::::::
:::

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_09_DATA_4.jpg" width=80%  alt="Jitter plot of Thumb predicted by Gender (female and male), with the empty model overlaid as a blue horizontal line at the mean of thumb, and the Gender model overlaid as red horizontal lines at the mean of each group. A few predictions from each model are highlighted as points along the lines. The distance between the predictions from the empty model to the Gender model are drawn as vertical lines and labeled as error reduced by the gender model compared to the empty model." /></p>

The `supernova()` function tells you that SS Model for the gender model in the `Fingers` dataset is 1,334. But let's use R to calculate it in this more direct way to see if we get the same result, and further your understanding of what's going on in the `supernova()` calculation.

In the code window below, assume the objects `empty_model` and `Gender_model` have been created already. The line of code provided generates all the differences between the two model predictions and saves it as a new variable called `error_reduced`. Run it to see what this variable is like. Then modify that code to square and sum the error reduced to print out SS Model.

```{ data-ckcode=true #B3_Code_Partitioning_01 }
%%% setup
require(coursekata)

empty_model <- lm(Thumb ~ NULL, data=Fingers)
Gender_model <- lm(Thumb ~ Gender, data=Fingers)

%%% prompt
# creates the differences between the two predictions
error_reduced <-  predict(Gender_model) - predict(empty_model)

# modify this line of code to square and sum these differences
error_reduced

%%% solution
# creates the differences between the two predictions
error_reduced <-  predict(Gender_model) - predict(empty_model)

# modify this line of code to square and sum these differences
sum(error_reduced ^ 2)

%%% test
ex() %>% check_output(1334.2)
```

```
1334.20254468864
```
