## 8.2 Fitting and Interpreting the Three-Group Model

We can now create a model that adjusts its predictions based on whether people are short, medium or tall (i.e., `Height3Group`). Let's learn how to fit this model using R, and represent it in GLM notation.

### Fitting the `Height3Group` Model

Now use the code window below to fit the `Height3Group` model to the data, and print out the model estimates.

```{ data-ckcode=true #B4_Extending_05 }
%%% setup
require(coursekata)

Fingers <- Fingers %>% mutate(
    Height2Group = factor(ntile(Height, 2), 1:2, c("short", "tall")),
    Height3Group = factor(ntile(Height, 3), 1:3, c("short", "medium", "tall"))
)
Height2Group_model <- lm(Thumb ~ Height2Group, data = Fingers)

%%% prompt
# modify this code to fit the model
Height3Group_model <- lm(Thumb ~ )

# this prints out the estimates
Height3Group_model

%%% solution
Height3Group_model <- lm(Thumb ~ Height3Group, data = Fingers)
Height3Group_model

%%% test
ex() %>% {
    check_function(., "lm") %>% check_arg("formula") %>% check_equal()
    check_object(., "Height3Group_model") %>% check_equal()
    check_output_expr(., "Height3Group_model")
}
```

```
Call:
lm(formula = Thumb ~ Height3Group, data = Fingers)

Coefficients:
       (Intercept)  Height3Groupmedium    Height3Grouptall
            56.071               4.153               8.023
```

The three-group model is written like this using General Linear Model notation:

$$Y_i=b_0+b_1X_{1i}+b_2X_{2i}+e_i$$

Whereas fitting the two-group model involved constructing two parameter estimates ($b_0$ and $b_1$), the three-group model adds a third parameter estimate ($b_2$).

  ::::::::: { .qti-item #Ch7_Extending_6 }
  :::::: { #98fb69ce-4c59-4053-b2d6-f61baa8ca234 .qti-question .association
  points="1" }
  Which numbers from `Height3Group.model` goes with these parameters?
  ::: associations

- [$b_0$]{match="3"}
- [$b_1$]{match="1"}
- [$b_2$]{match="2"}
  :::
  ::: choices

  1. 4.15
  2. 8.02
  3. 56.07
  :::
  ::::::
  :::::: { #7a1db089-b7d7-4153-8573-c5605996397c .qti-question .association
  points="1" }
  What do the variables represent?
  ::: associations

- [$Y_i$]{match="3"}
- [$X_{1i}$]{match="1"}
- [$X_{2i}$]{match="2"}
  :::
  ::: choices

  1. Whether the individual is in the medium group
  2. Whether the individual is in the tall group
  3. The individual's thumb length
  :::
  ::::::
  :::::::::

### Interpreting the `Height3Group` Model

$b_0$ is the mean of the short group. $b_1$ is the increment you have to add to the short group to get the mean of the medium group. And $b_2$ is the increment you have to add to the short group to get the mean of the tall group.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/2jmXHvzH.png" width=80%  alt="Jitter plot of Thumb predicted by Height3Group (short, medium, tall). A red horizontal line is overlaid on each group at the group mean. The mean of the short group is labeled as b-sub-zero; the vertical distance between the mean of the short group and the mean of the medium group is labeled as b-sub-one, and the vertical distance between the mean of the short group and the mean of the tall group is labeled as b-sub-two." /></p>

We can substitute in the parameter estimates into the model, like this:

$$Y_i=56.07+4.15X_{1i}+8.02X_{2i}+e_i$$

Or, more specifically, like this:

$$\text{Thumb}_i=56.07+4.15\text{Height3Groupmedium}_i+8.02\text{Height3Grouptall}_i+e_i$$

Just as before, it is useful to think through exactly how the X variables are coded. Notice, first, that we now have two of these in the model: $X_{1i}$ and $X_{2i}$. The new subscripts (1 and 2) just distinguish between the two variables; instead of giving them different names, we call them X-sub-1 and X-sub-2.

The sub-i indicates these are not parameters, but variables, which means that each individual in the dataset will have their own scores on the two variables. As before, it’s a little tricky to figure out what all the possible scores are on these two variables, and also how scores are assigned for each individual.

::: { .qti-item #Ch7_Extending_7 }
:::::: { #bfc9f0f8-0bf0-47bd-a736-73faf36dd435 .qti-question .multiple-choice points="1" scoring="partial" }

What is the difference between a parameter estimate and a variable? (Check all that apply.)

::::::::: { .choices }

- Parameter estimates are represented with regular letters, and variables are represented with Greek letters.
- [Parameter estimates are the same for each person in a sample, whereas values on a variable will differ according to which group someone is in.]{ .correct }
- [Each person's thumb length is composed of the same parameter estimates, and different values for the variables.]{ .correct }
- [The variables have a sub-*i* to indicate that this value varies for each person. Parameter estimates do not have a sub-*i* because they are the same for each person.]{ .correct }

:::::::::

::::::
:::

R doesn’t necessarily use the same numbers you do to code a variable. For the `Height3Group` model we put in a single categorical explanatory variable (`Height3Group`, with level 1 representing short, 2 representing medium, and 3 representing tall). But R turns this one variable into two new variables, $X_1$ and $X_2$, both of which are *dummy coded*, which means they can either have a value of 0 or 1 for each person in the dataset.

Here's how dummy coding works: For someone in the short group, the model needs to assign them a score of 56.07, the mean for the short group. You can think of $X_1$ as a variable asking, "Is this person medium?" and 0 means no and 1 means yes. By the same reasoning, $X_2$ represents whether someone is tall or not. For short people, $X_1$ and $X_2$ are both 0 because they are *not* medium and *not* tall.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/zD8JY0wK.png" width=80%  alt="Jitter plot of Thumb predicted by Height3Group (short, medium, tall). The short group is labeled as X1 equals zero and X2 equals zero. The medium group is labeled as X1 equals one, and the tall group is labeled as X2 equals one." /></p>

::: { .qti-item #Ch7_Extending_8 }
:::::: { #bb8ec042-e73f-42be-8f2a-bd88b596cbbe .qti-question .multiple-choice points="1" }

Let's work out the equation for someone in the short group.

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_1.png" width="350" height="31" />

::::::::: { .choices }

- [<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_2.png" width="300" height="34" />]{ .correct }
- <img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_3.png" width="275" height="35" />
- <img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_4.png" width="275" height="33" />
- <img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_5.png" width="250" height="33" />

:::::::::

::::::

:::::: { #2e0d366e-7e49-4148-99d1-245ee6cf0eda .qti-question .multiple-choice points="1" }

Let's work out the equation for someone in the medium group.

<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_1.png" width="350" height="31" />

::::::::: { .choices }

- <img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_2.png" width="300" height="34" />
- <img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_3.png" width="275" height="35" />
- [<img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_4.png" width="275" height="33" />]{ .correct }
- <img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Ch7_Extending_8_5.png" width="250" height="33" />

:::::::::

::::::
:::

For the people in the medium group, $X_1$ should be 1 (because they are in the medium group), and $X_2$ should be 0 (because they are *not* in the tall group). So the model will give them a predicted thumb length of $b_0 + b_1$ (56.07 + 4.15) which is equal to 60.22 mm.

And notice from favstats that the average thumb length of the medium group is 60.22!

<pre><code>  Height3Group   min    Q1 median    Q3   max     <mark>mean</mark>      sd  n  missing
1        short 39.00 51.00     55 58.42 79.00 <mark>56.07113</mark> 7.499937 53       0
2       medium 45.00 55.00     60 64.00 86.36 <mark>60.22375</mark> 8.490406 52       0
3         tall 44.45 59.75     64 68.25 90.00 <mark>64.09365</mark> 8.388113 52       0
</code></pre>

Dummy coding takes categorical variables and turns them into a series of binary codes. As you can see from the table below, just giving each person a 0 or 1 on $X_1$ and $X_2$ can uniquely categorize them as short, medium, or tall.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th>Category (Group)</th>
            <th>$X_1$ Code</th>
            <th>$X_2$ Code</th>
    </thead>
    <tbody>
        <tr>
            <td>Short</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Medium</td>
            <td>1</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Tall</td>
            <td>0</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

You may wonder why you need to go through all the details of how R assigns dummy codes for the categorical explanatory variable. The reason is that it gives you a concrete understanding of how to interpret the model parameters. For example, it helps us understand how the model generates the third group's prediction, by adding $b_2$ to $b_0$ (and not to $b_1$). In this course, we don’t often ask you to calculate these numbers on your own. Instead, we want you to focus on thinking about what, exactly, a number means.
