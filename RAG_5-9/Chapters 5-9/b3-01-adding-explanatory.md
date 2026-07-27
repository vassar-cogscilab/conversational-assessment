# Chapter 7 - Adding an Explanatory Variable to the Model

## 7.1 Explaining Variation

Having now spent some time with the empty model, you may be wondering, “What is the point of that model?” Statistics is supposed to help us *explain variation* and make better predictions of the outcome based on other variables. But the empty model doesn’t seem to make very good predictions. Yes, the mean is the point in the distribution that reduces the sum of squares to its lowest point. But surely that doesn’t count as an explanation of variation!

Indeed it does not. We started with the empty model but that’s not where we want to end up. We will use the empty model as a reference point to help us see if more complex models that include explanatory variables are *better*. Note that even though we will refer to models in this chapter as “complex” – they are still relatively simple. We just mean that these models are *more* complex than the empty model.

### Explaining Variation in Thumb Lengths

Let’s start by reviewing what we mean by *explaining* variation. Earlier in the course, we developed an intuitive idea of what it means to *explain* variation by comparing the distribution of an outcome variable across two different groups.

For example, we looked at the distribution of thumb length broken down by gender, which we can see in the two density histograms below. We’ve added the empty model prediction (the grand mean of thumb length) for reference. The empty model prediction would be the one we would use if we didn't know someone's gender.

```
empty_model <- lm(Thumb ~ NULL, data = Fingers)

gf_dhistogram(~ Thumb, data = Fingers) %>%
 gf_facet_grid(Gender ~ .) %>%
 gf_model(empty_model)
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/G32XGppR.png" width=80%  alt="Faceted histogram of Thumb grouped by Gender (female and male), with the empty model overlaid as a vertical line through the mean of Thumb." /></p>

We can look at the same relationship (and empty model) in a jitter plot.

```
empty_model <- lm(Thumb ~ NULL, data = Fingers)

gf_jitter(Thumb ~ Gender, data = Fingers, width = .1) %>%
  gf_model(empty_model)
```

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b1_05_Fitting_1.jpg" width=80%  alt="A jitter plot of the distribution of Thumb by Gender in the Fingers data frame, overlaid with a horizontal line in blue showing the empty model for Thumb." /></p>

Graphing the data by gender helps us  see that there appears to be a relationship in the data between gender and thumb length. Applying our informal definition of *explain variation*, it appears from the graph that if we know the gender of a student, we can make a slightly better guess about their thumb length.

::: { .qti-item #b3_Explaining_01 }
:::::: { #32492e38-0faf-41f2-a9fd-bed9abd8adec .qti-question .essay points="1" max-words="100" }

Under the empty model, we would predict the thumb length of a future student to be 60.1 mm (i.e., the overall average of `Thumb`). How might knowing the gender of a student change our prediction of their thumb length?

::::::::: { .feedback }

Although there is a lot of variation within both females and males, it still looks like males, on average, have slightly longer thumbs than females. If we know someone is male, therefore, we would probably predict their thumb to be a little longer than if they are female.

:::::::::

::::::
:::

We can express this relationship between `Gender` and `Thumb` informally with a word equation:

**Thumb = Gender + Error**

We will refer to this as the `Gender` model of `Thumb`. Gender doesn't explain all of the variation in thumb lengths (there still is error), but it does appear to explain some.

### Quantifying the `Gender` Model

In the previous chapter we developed our first real *statistical model*, the empty model. As it turned out, the best prediction of a future thumb length if we know nothing about the student is just the mean of the outcome variable `Thumb`. We called this empty model a *one-parameter model* because our prediction was based on a single estimate: the mean.

Let's see if we can follow a similar approach to go from our informal `Gender` model expressed as a word equation to a true statistical model that we can use to make specific quantitative predictions of the thumb lengths of other students not in our sample.

::: { .qti-item #b3_Explaining_02 }
:::::: { #e46dc33e-d12f-4c41-8f71-f9ef65f310f4 .qti-question .multiple-choice points="1" }

If we wanted to generate different predictions for thumb lengths of females and males, which of the following strategies sounds reasonable?

::::::::: { .choices }

- Use the mean length of the longer thumbs versus the mean length of the shorter thumbs to generate different predictions.
- [Use the mean thumb length of females versus the mean thumb length of males to generate different predictions.]{ .correct }
- Use the highest thumb length (maximum) to predict male thumb lengths and the lowest price (minimum) to predict female thumb lengths.

:::::::::

::::::
:::

We can turn the `Gender` model into a statistical model in much the same way we did for the empty model. This time, instead of predicting a student's thumb length to be the mean of `Thumb` we will predict it to be the mean thumb length *given their gender*. Thus, if the student is female, we will predict her thumb length as the mean of female thumb lengths, and if male, the mean of males.

This is a two-parameter model, because it will require us to make two estimates, one for each of the genders. We have added a visualization of the `Gender` model to the plot below (the red horizontal lines), in addition to a visualization of the empty model (the blue horizontal line).

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_01_Quantifying_1.jpg" width=80%  alt="A jitter plot of the distribution of Thumb by Gender, overlaid with a horizontal line in blue showing the empty model for Thumb. It is also overlaid with a red horizontal line in each group showing the group mean." /></p>

::: { .qti-item #b3_Explaining_03 }
:::::: { #eeeb7045-f270-4a83-b492-9d11293ed870 .qti-question .multiple-choice points="1" }

Based on the visualization, what would the `Gender` model predict for a female student's thumb length?

::::::::: { .choices }

- [Around 58]{ .correct }
- Around 60
- Around 65

:::::::::

::::::

:::::: { #9366c63d-3b6f-4815-9fa0-d0c0c670b855 .qti-question .multiple-choice points="1" scoring="partial" }

Based on the visualization, what would the `Gender` model predict for a male student's thumb length? (Check all that apply.)

::::::::: { .choices }

- Around 58
- Around 60
- [Around 65]{ .correct }
- [About 7 mm more than the female prediction]{ .correct }
- About 7 mm less than the female prediction

:::::::::

::::::
:::

In the following pages we will learn how to use R to fit the `Gender` model to the `Fingers` data; how to interpret the parameter estimates; how to write the model in GLM notation; how to quantify error around the model; and how to compare the model to the empty model.
