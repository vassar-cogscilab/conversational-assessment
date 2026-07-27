## 5.6 Generating Predictions From the Empty Model

The mean of the sample distribution is our best, unbiased estimate of the mean of the population. For this reason, we use the mean as our model for the population. And, if we want to predict what the next randomly sampled observation might be, without any other information, we would use the mean.

In data analysis, we also use the word "predict" in another sense and for another purpose. Using our `Fingers` data, we found the mean thumb length to be 60.1 mm. So, if we were predicting a new student's thumb length, we’d go with 60.1 mm. But if we take the mean and look backwards at the data we have already collected, we could also generate a "predicted" thumb length for each of the data points we already have. This prediction answers the question: **what would our model have predicted this thumb length to be if we hadn't collected the data?**

There’s an R function called `predict()` that will actually do this for you. Here’s how we can use it to generate the predicted thumb lengths for each of the 157 students in the `Fingers` data frame. Remember, we already fit the model and saved the results in `empty_model`:

```
predict(empty_model)
```

Try using the `predict()` function to generate predicted thumb lengths using the empty model in the code window below.

```{ data-ckcode=true #B1_Code_Predictions_01 }
%%% setup
require(coursekata)


%%% prompt
# saves the empty model
empty_model <- lm(Thumb ~ NULL, data = Fingers)

# write code to generate predictions of the empty model

%%% solution
# saves the empty model
empty_model <- lm(Thumb ~ NULL, data = Fingers)

# write code to generate predictions of the empty model
predict(empty_model)

%%% test
ex() %>% check_object("empty_model") %>% check_equal()

```

::: { .qti-item #b1_Predictions_1 }
:::::: { #d4a3c596-7646-4fb5-bf00-f0374cab49bb .qti-question .multiple-choice points="1" }

Wow, that is a lot of (rounded) 60.1s. How many of them are there?

::::::::: { .choices }

- 60
- [157, one predicted thumb length for each student in the `Fingers` data frame]{ .correct }
- an infinite number, we can predict any student using the empty model

:::::::::

::::::
:::

You may be wondering: why would we want to create *predicted* thumb lengths for these 157 students when we already know their *actual* thumb lengths? We will go into this a lot more in the next chapter, but briefly, the reason is so we can get a sense of how far off the model predictions are from the actual data. In other words, it gives us a rough idea of how much error there is around the model predictions, i.e., how well our model fits our current data.

In order to use these predicted scores as a way of seeing how much error there is, we first need to save the prediction for each student in the dataset. When there is only one prediction for everyone, as with the empty model, it seems like overkill to save the predictions.

But as we go, we'll start to appreciate how useful it is to save the individual predicted scores. For example, if we save the predicted score for each student in a new variable called `Predict`, we can then subtract each student’s actual thumb length from their predicted thumb length to see how far off the prediction is for each student.

In the code window below, use the `predict()` function to  save the predicted thumb lengths for each of the 157 students as a new variable in the `Fingers` dataset. We've added some code to overlay these predictions onto a scatter plot we've looked at before (`Thumb` by `Height`).

```{ data-ckcode=true #B1_Code_Predictions_02 }
%%% setup
require(coursekata)

%%% prompt
# this saves the empty_model
empty_model <- lm(Thumb ~ NULL, data = Fingers)

# modify this to save the predictions from the empty_model in a new variable
Fingers$Predict <-

# prints out selected variables from Fingers
head(select(Fingers, Thumb, Predict), 10)

# this makes a scatter plot of Thumb by Height and overlays the empty model's predictions as open blue circles
gf_point(Thumb ~ Height, data = Fingers, width = .1) %>%
  gf_point(Predict ~ Height, color = "blue", shape = 1, height = 0)

%%% solution
# this saves the empty_model
empty_model <- lm(Thumb ~ NULL, data = Fingers)

# modify this to save the predictions from the empty_model in a new variable
Fingers$Predict <- predict(empty_model)

# prints out selected variables from Fingers
head(select(Fingers, Thumb, Predict), 10)

# this makes a scatter plot of Thumb by Height and overlays the empty model's predictions as open blue circles
gf_point(Thumb ~ Height, data = Fingers, alpha = .2) %>%
  gf_point(Predict ~ Height, color = "blue", shape = 1)

%%% test
ex() %>%
  check_object("Fingers") %>%
  check_column("Predict") %>%
  check_equal()
```

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto; margin-top: 1.5em;  }
    table.table--outlined th { border: 1px solid black; padding: .5em; vertical-align: bottom; }
    table.table--outlined td  { border: 1px solid black; padding: .5em; vertical-align: top;}
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th valign="top">A snippet of the <code>Fingers</code> data frame</th>
            <th style="width:75%">A scatter plot of <code>Thumb</code> by <code>Height</code></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><pre><code> Thumb  Predict
1 66.00 60.10366
2 64.00 60.10366
3 56.00 60.10366
4 58.42 60.10366
5 74.00 60.10366
6 60.00 60.10366</code></pre></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/BJHnfG1d.png" alt="Scatter plot of Thumb predicted by Height in Fingers with the empty model overlaid as point predictions for each data point. The predictions are aligned in a horizontal line." /></p></td>
        </tr>
    </tbody>
</table>

As we can see from the sample rows from the `Fingers` data frame (on the left), every student, regardless of their thumb length, is given the same model prediction (60.1). This is because in the empty model, there is only one prediction, and that is the mean.

In the scatter plot, we might see a relationship between `Thumb` and `Height` in the data. But the empty model ignores all that and just predicts the same thumb length for every student, which is why the predictions (`Fingers$Predict`) form a straight horizontal line. (Later we will learn how to adjust predictions based on explanatory variables such as gender or height).
