# Chapter 8 - Digging Deeper into Group Models

## 8.1 Extending to a Three-Group Model

You have now learned how to specify a model with a single categorical explanatory variable consisting of two groups. It’s actually pretty simple to extend this idea to a categorical variable with three groups.

### First, a New Two-Group Model

Let’s use a new explanatory variable to explain variation in thumb length: `Height`. `Height`, in our dataset, is a quantitative variable measured in inches. But we can make a new variable that turns `Height` into a categorical variable with two categories: `short` and `tall`.

We can do this using the `ntile()` function in R. The code below will cut the sample up into two equal-sized groups based on `Height` and save the result into a new variable called `Height2Group`.

```
Fingers$Height2Group <- ntile(Fingers$Height, 2)
head(select(Fingers, Thumb, Height, Height2Group), 10)
```

We used `head()` and `select()` to look at the first 10 rows of the relevant variables – `Thumb`, `Height`, and `Height2Group`:

```
   Thumb Height Height2Group
1  66.00   70.5            2
2  64.00   64.8            1
3  56.00   64.0            1
4  58.42   70.0            2
5  74.00   68.0            2
6  60.00   68.0            2
7  70.00   69.0            2
8  55.00   65.7            2
9  60.00   62.5            1
10 52.00   63.4            1
```

In the code window below, use the `factor()` function to add labels to `Height2Group` so that the 1s are labeled as `short` and the 2s are labeled as `tall`.

 ```{ data-ckcode=true #B4_Code_Extending_01 }
%%% setup
require(coursekata)

Fingers <- Fingers %>% mutate(
    Height2Group = ntile(Height, 2)
)

%%% prompt
# this creates Height2Group, a numeric variable
Fingers$Height2Group <- ntile(Fingers$Height, 2)

# this is how we used factor() before:
Fingers$Gender <- factor(Fingers$Gender, levels = c(1,2), labels = c("female", "male"))

# modify this line so that 1s are labeled as "short" and 2s are labeled as "tall"
Fingers$Height2Group <- factor()

# this prints out 10 rows of Fingers for the selected columns
head(select(Fingers, Thumb, Height, Height2Group), 10)

%%% solution
Fingers$Height2Group <- factor(Fingers$Height2Group, levels = 1:2, labels = c("short", "tall"))

head(select(Fingers, Thumb, Height, Height2Group), 10)

%%% test
ex() %>% {
    check_object(., "Fingers") %>% check_column("Height2Group") %>% check_equal()
    check_output_expr(., "head(select(Fingers, Thumb, Height, Height2Group), 10)")
}
```

```
   Thumb Height Height2Group
1  66.00   70.5         tall
2  64.00   64.8        short
3  56.00   64.0        short
4  58.42   70.0         tall
5  74.00   68.0         tall
6  60.00   68.0         tall
7  70.00   69.0         tall
8  55.00   65.7         tall
9  60.00   62.5        short
10 52.00   63.4        short
```

Using the same approach we used for gender, we can write the model for `Height2Group` like this:

$$\text{Thumb}_i=b_0+b_1\text{Height2Group}_i+e_i$$

  ::::::::: { .qti-item #Ch7_Extending_1_r5.8 }
  :::::: { #e1b915e0-ca47-4945-b6c3-4a35b28216e8 .qti-question .association
  points="1" }
  What do the different symbols mean in the equation above?
  ::: associations

- [$Y_i$]{match="1"}
- [$X_i$]{match="3"}
  :::
  ::: choices

  1. Thumb
  2. Height
  3. Height2Group
  4. Gender
  5. Short
  6. Tall
  :::
  ::::::
  :::::::::

Go ahead and fit the `Height2Group` model, and print out the parameter estimates and ANOVA table for the model.

```{ data-ckcode=true #B4_Code_Extending_02 }
%%% setup
require(coursekata)

Fingers <- Fingers %>% mutate(
    Height2Group = factor(ntile(Height, 2), 1:2, c("short", "tall"))
)

%%% prompt
# fit a model for Thumb ~ Height2Group
Height2Group_model <-

# this prints out the estimates
Height2Group_model

%%% solution
# fit a model for Thumb ~ Height2Group
Height2Group_model <- lm(formula = Thumb ~ Height2Group, data = Fingers)

# this prints out the estimates
Height2Group_model

%%% test
ex() %>% {
    check_function(., "lm") %>% check_arg("formula") %>% check_equal()
    check_object(., "Height2Group_model") %>% check_equal()
    check_output_expr(., "Height2Group_model")
}
```

```
Call:
lm(formula = Thumb ~ Height2Group, data = Fingers)

Coefficients:
     (Intercept)  Height2Grouptall
          57.818             4.601
```

  ::::::::: { .qti-item #Ch7_Extending_2 }
  :::::: { #8c48e0e2-9db0-4aa3-b989-b7fa088d7800 .qti-question .association
  points="1" }
  What are your estimates for $b_0$ and $b_1$?
  ::: associations

- [$b_0$]{match="1"}
- [$b_1$]{match="2"}
  :::
  ::: choices

  1. 57.818
  2. 4.601
  :::
  ::::::
  :::::: { #aa4da9cb-6c40-4c1a-b4fd-ababa50512ee .qti-question .multiple-choice
  points="1" }
  Why does it say `Height2Grouptall` in the output (rather than just
  `Height2Group`)?
  ::: choices

- [This is the adjustment you add on for the thumb length of someone in the
  tall group.]{.correct}
- This is the average height of someone in the tall group.
- This is the average thumb length of someone in the tall group.
- This is the adjustment you add on for the height of someone in the tall
  group.
  :::
  ::::::
  :::::: { #8d9d2327-6818-4b4a-b6e2-382e26db013b .qti-question .multiple-choice
  points="1" }
  How would $X_i$ be coded in order for this model to make sense?
  ::: choices
- -1 for short and 1 for tall
- 1 for short and 2 for tall
- -1 for short and 1 for tall
- [0 for short and 1 for tall]{.correct}
  :::
  ::::::
  :::::::::

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

::::::::: { .qti-item #Ch7_Extending_3_r3.0 }

:::::: { #Ch7_Extending_3_r3.0a .qti-question .multiple-choice points="1" scoring="exactMatch" multiple-responses="true" }

What is the $\text{SS}_\text{Total}$? (Check all that apply.)

::: choices

- [The total squared error of `Thumb` lengths from the grand mean]{.correct}
- [The remaining SS from the `empty_model` of `Thumb` length]{.correct}
- All the SS explained by `Height2Group_model` of `Thumb` length
- [All of the SS left over from the `empty_model` of `Thumb` length]{.correct}
- [The SS Error from the `empty_model` of `Thumb` length]{.correct}

:::

::::::

:::::: { #Ch7_Extending_3_r3.0b .qti-question .short-answer points="1" }

What is PRE for the `Height2Group` model? [0.0699]{.correct number tolerance=.001}

::::::

:::::: { #Ch7_Extending_3_r3.0c .qti-question .multiple-choice points="1" }

What does PRE mean?

::: choices

- The proportion of variation explained by the `empty_model`.
- The number of square mm explained by the `Height2Group_model`.
- [The proportion of variation explained by the `Height2Group_model`.]{.correct}
- The proportion of variation unexplained by the `Height2Group_model`.
- The sum of squared error explained by the `Height2Group_model`.

:::

::::::

:::::::::

### A Three-Group Model

Now let’s try this same approach with three height groups: short, medium, and tall.

Revise the code below to make a new variable called `Height3Group` that divides the sample into three categories based on `Height`, each with an equal number of students. Label the levels (1,2,3) as `short`, `medium`, and `tall`.

```{ data-ckcode=true #B4_Code_Extending_03 }
%%% setup
require(coursekata)

Fingers <- Fingers %>% mutate(
    Height2Group = factor(ntile(Height, 2), 1:2, c("short", "tall"))
)
Height2Group.model <- lm(Thumb ~ Height2Group, data = Fingers)

%%% prompt
# modify these two lines of code to create 3 Height groups with the labels "short", "medium", and "tall"
# make sure you save to a new variable in Fingers called Height3Group
Fingers$Height2Group <- ntile(Fingers$Height, 2)
Fingers$Height2Group <- factor(Fingers$Height2Group, levels = c(1,2), labels = c("short", "tall"))

# this prints out 10 rows of Fingers for selected columns
head(select(Fingers, Thumb, Height, Height3Group), 10)

%%% solution
# modify these two lines of code to create 3 Height groups with the labels "short", "medium", and "tall"
# make sure you save to a new variable in Fingers called Height3Group
Fingers$Height3Group <- ntile(Fingers$Height, 3)
Fingers$Height3Group <- factor(Fingers$Height3Group, levels = c(1,2,3), labels = c("short", "medium", "tall"))

# this prints out 10 rows of Fingers for selected columns
head(select(Fingers, Thumb, Height, Height3Group), 10)

%%% test
ex() %>% {
    check_object(., "Fingers") %>% check_column("Height3Group") %>% check_equal()
    check_output_expr(., "head(select(Fingers, Thumb, Height, Height3Group),10)")
}
```

```
   Thumb Height Height3Group
1  66.00   70.5         tall
2  64.00   64.8       medium
3  56.00   64.0        short
4  58.42   70.0         tall
5  74.00   68.0         tall
6  60.00   68.0         tall
7  70.00   69.0         tall
8  55.00   65.7       medium
9  60.00   62.5        short
10 52.00   63.4        short
```

Calculate and print out the group means of `Thumb` for the three height groups.

```{ data-ckcode=true #B4_Code_Extending_04 }
%%% setup
require(coursekata)

Fingers <- Fingers %>% mutate(
    Height2Group = factor(ntile(Height, 2), 1:2, c("short", "tall")),
    Height3Group = factor(ntile(Height, 3), 1:3, c("short", "medium", "tall"))
)

%%% prompt
# use favstats() to print the group means of Thumb length for the three height groups you created earlier
favstats()

%%% solution
# use favstats() to print the group means of Thumb length for the three height groups you created earlier
favstats(Thumb ~ Height3Group, data = Fingers)

%%% test
ex() %>% check_function("favstats") %>% check_result() %>% check_equal()
```

```
  Height3Group   min    Q1 median    Q3   max     mean       sd  n missing
1        short 39.00 51.00     55 58.42 79.00 56.07113 7.499937 53       0
2       medium 45.00 55.00     60 64.00 86.36 60.22375 8.490406 52       0
3         tall 44.45 59.75     64 68.25 90.00 64.09365 8.388113 52       0
```

::: { .qti-item #Ch7_Extending_5 }
:::::: { #e912af6b-894e-4ca0-a699-0802e3eaaf42 .qti-question .multiple-choice points="1" }

What is the pattern of *means* from `favstats()` across the three groups of `Height3Group`?

::::::::: { .choices }

- There are more people as the groups get larger.
- There are taller people in the tall group.
- [The taller groups tend to have longer thumbs.]{ .correct }
- The medium group has slightly longer thumbs than the tall group.

:::::::::

::::::
:::

Here is a jitter plot that shows the distribution of thumb lengths for each of the three height groups and the mean of each group. On the next page, we'll learn how to create a model of thumb length based on the three height groups.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/KmTPgTmF.png" width=80%  alt="Jitter plot of Thumb predicted by Height3Group (short, medium, tall). A red horizontal line is overlaid on each group at the group mean and labeled with the value of the mean: short equals 56.1, medium equals 60.2, and tall equals 64.1." /></p>
