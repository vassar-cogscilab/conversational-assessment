## 5.2 Modeling a Distribution with a Single Number

Building on this concept of model, let’s now develop what we mean by a *statistical model*. Whereas in the previous section we were building a model to help us estimate the area of the state of California, we now want to build a model we can use to characterize a distribution.

As you will see in subsequent chapters, statistical models are very useful. We use them to summarize distributions. We use them to make predictions about what the next observation added to a sample distribution might be. And we use them to explain variation in one variable with another. But we will start with the simplest model, which uses a single number to characterize a distribution.

At its most basic level, a statistical model can be thought of as a **function that produces a predicted score for each observation** in a distribution. By "function" we don't mean an R function; we mean a mathematical procedure for generating a number based on the data. The simplest models we consider generate the same predicted score for every observation in a distribution—a single number to characterize a whole distribution.

If you had to pick one number to represent an entire distribution, how would you pick it? And what would it be? Thought of in a different way: if you wanted to predict what the value of the next randomly chosen observation would be, what would be your best prediction?

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/TfnF2Wyt.png" alt="Histogram of Age in MindsetMatters. The distribution ranges from about 20 to about 65, with a peak around 27 to 28 and another peak around 39 to 40." width="80%"/></p>

::: { .qti-item #b1_Single_1 }
:::::: { #24af5ded-27a5-4d48-8b0f-c9908368059c .qti-question .essay points="1" max-words="200" }

Let's look at some distributions. What single number would you choose to represent, or model, this distribution of "Age of Housekeepers"? Why? If you wanted to predict what the next randomly chosen observation would be, what would be your prediction?

::::::
:::

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/jRwWJtb3.png" alt="Histogram of Wt in MindsetMatters. The distribution ranges from about 100 to about 200, and is roughly normally distributed, with a peak near 150."  width="80%"/></p>

::: { .qti-item #b1_Single_2 }
:::::: { #7f418f5a-7203-4ad0-8c64-6f37e5297cd1 .qti-question .essay points="1" max-words="200" }

What single number would you choose to represent, or model, this distribution of "Weight of Housekeepers"? Why? If you wanted to predict what the next randomly chosen observation would be, what would be your prediction?

::::::
:::

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/dJsh4rrX.png" alt="Histogram of GradePredict in Fingers. The distribution ranges from about 2.2 to 4.0 and is skewed left, with a peak near 3.7 to 4.0."  width="80%"/></p>

::: { .qti-item #b1_Single_3 }
:::::: { #7c2674f0-f3fc-4d42-a89d-64fae1192cb6 .qti-question .essay points="1" max-words="200" }

What single number would you choose to represent, or model, this distribution of "Predicted GPA of Students"? Why? If you wanted to predict what the next randomly chosen observation would be, what would be your prediction?

::::::
:::

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/fDZPqRLp.png" alt="Bar graph of RaceEthnic in Fingers. White and Asian groups have the highest counts, the Latino group has about half the count of these two groups, and the African American and Other groups have the lowest counts."  width="80%"/></p>

::: { .qti-item #b1_Single_4 }
:::::: { #73474db0-9a6b-4d94-90ae-02707e435dc7 .qti-question .essay points="1" max-words="200" }

What is the best value to represent, or model, this distribution of "Race/Ethnicity of Students"? Why? If you wanted to predict what the next randomly chosen observation would be, what would be your prediction?

::::::
:::

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/HHDg9HC8.png" alt="Bar graph of Job in Fingers. The Not Working group has the highest count, the part-time job group has the next highest count, and the full-time job has the lowest count."  width="80%"/></p>

::: { .qti-item #b1_Single_5 }
:::::: { #9de07fcc-5ffc-451c-b411-87ead0db9841 .qti-question .essay points="1" max-words="200" }

What is the best value to represent, or model, this distribution of "Job Status of Students"? Why? If you wanted to predict what the next randomly chosen observation would be, what would be your prediction?

::::::
:::

Depending on how a variable is measured (e.g., quantitative or categorical), and on the shape of the distribution, we will use different procedures (or different *functions*) for choosing one number as a model.

For a quantitative variable whose distribution is roughly symmetrical and bell shaped, a number right in the middle might be the best-fitting model. (Remember, we aren’t saying that such a simple model is a good model—just better than nothing!) If a distribution is skewed left or right, the best model might be a number toward where the middle would be if you ignored the long tail on one side or the other. For a categorical variable, the best model is generally the category that is most frequent.

### Model and Error

Let’s zero in on just distributions of quantitative variables. Take a look at the two distributions below for variables 1 and 2.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/6wJ82DjY.png" alt="A faceted density histogram of the distribution of a variable named “outcome” split into two groups labeled 1 and 2. The top histogram, labeled 1, is normally distributed, centered around 100 and ranges from about 85 to 115. The bottom histogram, labeled 2, is normally distributed, centered around 100, and ranges from about 50 to 150." width="80%" /></p>

::: { .qti-item #Ch5_Modeling_2 }
:::::: { #82658a76-4204-444d-b3a5-67799954d3bd .qti-question .essay points="1" max-words="100" }

What number would you choose as the best model for distribution 1 (in navy blue)? Why?

::::::

:::::: { #215bfdd0-7723-46b3-ad4d-d3f63113b6d1 .qti-question .essay points="1" max-words="100" }

What number would you choose as the best model for distribution 2 (in sky blue)? Why?

::::::

:::::: { #a0ee3e5a-7bb8-44f0-969b-c71d7f6c0b7d .qti-question .essay points="1" max-words="100" }

For which distribution (1 or 2) is the model a better fit for the data? Why?

::::::
:::

A single number—even a well-chosen number—is not a very good model. It may be a better model for variable 1 than variable 2 above, but it’s still not very good. Most scores are not the same as the number we choose as the model.

Which brings us to another important concept: once we choose a number to model a distribution (and we’ll talk soon about how we do that), we can think of the variation around that number as *error,* just as we considered the parts of California not covered by geometric shapes as error.

If we use a single number to model the distribution of a quantitative variable, error from the model can be seen as deviations of the observed scores from that predicted number. As we just saw, a one-number model for a distribution with less spread seems to have less error, and thus a better fit, than a one-number model for a distribution with more spread. The reason for this is that the error around the model is greater for the distribution with more spread.

The idea of modeling a distribution with a single number gives us a more concrete and detailed way of thinking about our models. Whereas we thought about the California example like this:

<p style="text-align: center;">**Area Of California = Area Of Geometric Figures + Error**</p>

We can think of a statistical model like this:

<p style="text-align: center;">**DATA = MODEL + ERROR**</p>

Each data point in a distribution can be decomposed into two parts: the model (i.e., the number we are using to represent the whole distribution), and the data point’s deviation from the model (the error).
