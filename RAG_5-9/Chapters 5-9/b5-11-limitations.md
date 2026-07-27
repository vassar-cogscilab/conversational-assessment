## 9.11 Limitations to Keep in Mind

Regression and correlation are powerful tools for modeling relationships between variables. But each must be used thoughtfully. It is important always to interpret the findings in context, and use everything else you know about the context to help you draw reasonable conclusions based on the data.

### Correlation Does Not Imply Causation

Most important to bear in mind is that correlation does not imply causation, something you no doubt have heard before. Just the fact that an explanatory and outcome variable  are correlated does not necessarily mean we understand what causes this variation. And in this sense, regression is no different from correlation.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/gmJjqBsR.png" width=80%  alt="A circle on the left is labeled Explanatory with an arrow pointing from it to a circle on the right labeled Outcome. A question mark lies in the middle of the path of the arrow." /></p>

There are many examples of this. Children’s shoe size is correlated with their scores on an achievement test, but neither variable *causes* the other. An increase in age of the child, a confounding variable, causes both shoe size and achievement to go up.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/gcPz9gbz.png" width=80%  alt="Three circles arranged in an inverted triangle. The bottom circle is labeled Age, and has an arrow pointing from it to the circle in the top left labeled Shoe Size, and another arrow pointing from it to the circle in the top right labeled Achievement." /></p>

Also keep in mind that a relationship can be bidirectional, meaning each variable has a causal effect on the other. Reading skills and writing skills tend to be highly correlated. It might be that reading a lot causes writing to improve. But it's also plausible that practicing writing might help students improve their reading skills.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/ChsCD6NX.png" width=80%  alt="On the left, a circle is labeled as Reading with an arrow pointing from it to a circle on the right labeled as Writing. An arrow is also pointing from the Writing circle to the Reading circle." /></p>

As in all things, we should interpret statistics like the correlation coefficient and regression slope with common sense. The tendency to wear skimpy clothing is correlated with higher temperatures. In this case the relationship is real, but the causal direction must be sensibly interpreted. Hiking up the temperature might indeed cause people to shed their clothing. But taking off clothes is not going to cause the temperature to go up.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/VfkvGGw3.png" width=80%  alt="On the left, a circle labeled Temperature with an arrow pointing from it to a circle on the right labeled as Skimpy Clothes. A red arrow is also point from the Skimpy Clothes circle to the Temperature circle, but has an X over it to show that there is no causal connection in that direction." /></p>

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/MKDmbBQG.png" width=80% alt="Comic regarding correlation versus causation" /></p>
<font size="1">Correlation. (n.d.). Retrieved from https://xkcd.com/552/ </font>

Thumb length measured in millimeters is going to be perfectly correlated with thumb length measured in centimeters. The points will be perfectly laid out on a straight line. But does spotting this relationship get us any closer to understanding the DGP that produces variation in thumb length? Of course not.

::: { .qti-item #Ch8_Limitations_1 }
:::::: { #2ef3a4f7-37fc-4343-8cb7-d2fa3a6cfb08 .qti-question .essay points="1" max-words="100" }

Let's say we do a survey and find that time spent studying correlates with score on the final exam. Based on the study results, can we conclude that studying **caused** the increase in exam scores? Why or why not?

::::::
:::

Disambiguating causal relationships and controlling for possible confounds is not achievable through statistical analysis alone. Statistics can help, and correlation can certainly suggest that there might be causation there. But research design is a necessary tool. Random assignment of equivalent objects to conditions that do and don’t receive some treatment is often required to figure out whether a particular relationship is causal or not.

### Are All Lines Straight?

Another thing to point out is that the models we have considered in this chapter are linear models. We fit a straight line to a scatter of points, and then look to see how well it fits by measuring residuals around the regression line.

But sometimes a straight line is just not going to be a very good model for the relationship between two variables.

Take this graph showing the relationship of body weight to risk of death. Being underweight and being overweight both increase the risk of death, whereas being in the middle reduces that risk.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/9QQtxfdY.png" width=70% alt="A line chart of the distribution of absolute risk of death and body mass index. The graph is roughly U-shaped." /></p>

If you ignored the shape of the relationship and overlaid a regression line, the line would probably be close to flat, indicating no relationship. But if you did that you would be missing an important systematic curvilinear relationship.

**Before fitting a linear regression model, look at the relationship and see if a linear function would be a sensible model. If it isn't, think about a different model**. Mathematicians have lots of models to offer beyond just the simple straight line.

### Do Regression Lines Go On Forever?

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/g2ty1P4F.png" width=60% alt="Comic about regression lines" /></p>

Source of picture: <a href="http://smbc-comics.com/comic/2011-08-05" target="_blank">(http://smbc-comics.com/comic/2011-08-05)</a>

Finally, there is the problem of extrapolation. We have already pointed out from our regression of `Thumb` on `Height` that, according to the model, someone who is 0 inches tall would have a thumb length of -3.33 millimeters. Obviously, the regression model only works within a certain range, and it is risky to extend that range beyond where you have substantial amounts of data.

In general, common sense and a careful understanding of research methods must be applied to the interpretation of any statistical model.

### Mid-Course Survey #2

You're two-thirds through the book! Please tell us about your experience so far. (Estimated time: 5 minutes)

::: { #Mid2_Survey_0725 .qti-activity }

::: { #Mid2_Survey_0625 .qti-item }

::: { #67306728-7e51-4158-a60b-1580e6b17bec .qti-question .choice-matrix points="0" }
::: prompts

- In this class, you are using R to analyze data. How do you feel about this?
:::
::: scale
- Strongly negative
- Negative
- Somewhat negative
- Somewhat positive
- Positive
- Strongly Positive
:::
:::

::: { #7fad0ce8-4894-4546-9535-ee4a6d5e14c1 .qti-question .choice-matrix points="0" }
::: prompts

- How confident are you in your R skills?
:::
::: scale
- Not at all confident
- Only a little confident
- Somewhat confident
- Mostly confident
- Completely confident
:::
:::

::: { #ef8955ef-95b8-4ac9-95cb-085027cba931 .qti-question .choice-matrix points="0" }
::: prompts

- I look forward to learning more about math, statistics, or data science.
- I want to take more math, statistics, or data science classes in the future.
- I would be interested in having a job someday that involved things like math, science, statistics, or data science.
:::
::: scale
- Strongly disagree
- Disagree
- Slightly disagree
- Slightly agree
- Agree
- Strongly agree
:::
:::

:::

::: { #Mid2_ConfidenceUse_0725 .qti-item }

::: { #bbafca49-c402-49a6-8fff-d54473ff6947 .qti-question .choice-matrix points="0" }
::: prompts

- Given enough time, I feel confident that I could learn more advanced math/statistics.
- I can see how statistics would be useful for solving real-world problems.
- I can see how algebra would be useful for solving real-world problems.
- Using data helped me see why we learn math in the first place.
:::
::: scale
- Strongly disagree
- Disagree
- Slightly disagree
- Slightly agree
- Agree
- Strongly agree
:::
:::

:::

::: { #Mid2_Metacog1_0625 .qti-item }

::: { #05e0b1c4-c050-4ac0-9efe-124b3b089a89 .qti-question .choice-matrix points="0" }
In this section, you'll be asked again how well you think you could do certain tasks related to data, R programming, and statistical thinking. Some tasks might still feel challenging, and that's okay! Take this time to reflect on your skills and knowledge at this point in the course.

Thanks for sharing your judgments with us!

Using your best judgment, could you do each of the following right now?

::: prompts

- Write R code to find out what variables are included in the dataset.
- Explain the difference between an outcome variable and an explanatory variable.
- Explain the difference between a variable and a value in a dataset.
- Explain the difference between a quantitative and categorical variable.
- Create a histogram of a distribution of a quantitative variable using R.
- Examine a histogram and describe its shape, center, spread, and any unusual patterns.
- Write a word equation to represent a hypothesis about the relationship between an explanatory and outcome variable.
- Choose an appropriate visualization to represent the relationship between a quantitative outcome variable and a categorical explanatory variable.
- Use R to create a scatter plot to visualize a relationship between two quantitative variables.
- Explain whether a scatterplot supports a hypothesized relationship between two quantitative variables.
- Write R code to fit and save an empty model.
- Write R code to fit and save a two-group model.
:::
::: scale
- I definitely could not do it
- I probably could not do it
- I probably could do it
- I definitely could do it
:::
:::

:::

::: { #Mid2_Metacog2_0625 .qti-item }

::: { #0313496c-3548-4338-bbca-4e842278d5ba .qti-question .choice-matrix points="0" }
Using your best judgment, could you do each of the following right now?

::: prompts

- Explain what it means to fit a model (i.e., find the best-fitting model).
- Draw the best-fitting empty model on top of a scatter plot (either by hand or using R).
- Draw the best-fitting regression model on top of a scatter plot (either by hand or using R).
- Visually compare the amount of error around the empty model versus a regression model on a scatter plot.
- Interpret the parameter estimates that result from fitting a regression model.
- Write a regression model using GLM notation.
- Name three quantitative measures that indicate how well a model fits the data.
- Use R to find out how well a model fits the data.
- Explain what the PRE statistic means for a model.
- Explain how the results of a data analysis might support a hypothesis (or not).
- Discuss the implications of the results of a data analysis for a real-world contexts.
- Explain why understanding the context of a dataset is important for interpreting the parameter estimates.
:::
::: scale
- I definitely could not do it
- I probably could not do it
- I probably could do it
- I definitely could do it
:::
:::

:::

:::
