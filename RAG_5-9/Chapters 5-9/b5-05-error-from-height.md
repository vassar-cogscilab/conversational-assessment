## 9.5 Error from the Height Model

Regardless of model, error from the model (or residuals) are always calculated the same way for each data point:

$$\text{residual}=\text{observed value} - \text{predicted value}$$

::::::::: { .qti-item #b5_Error_01 }
:::::: { #88885641-c3c9-47c9-bb68-e5a6935f7fe6 .qti-question .association
points="1" }
Match these elements up with DATA = MODEL + ERROR
::: associations

- [residual]{match="1"}
- [observed value]{match="2"}
- [predicted value]{match="3"}  }
:::
::: choices

1. ERROR
2. DATA
3. MODEL
:::
::::::
:::::::::

For regression models, the predicted value of $Y_i$ will be right on the regression line. Error, therefore, is calculated based on the vertical gap between a data point's value on the Y axis (the outcome variable) and its predicted value based on the regression line.

Below we have depicted just 6 data points (in black) and their residuals (`firebrick` vertical lines) from the `Height` model.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/rq2JJHcP.png" width=80%  alt="A scatter plot of the distribution of Thumb by Height overlaid with the regression line in red. A few residuals are drawn above and below the regression line as vertical lines from the data points to the model." /></p>

Note that a negative residual (shown below the regression line) means that the data (e.g., `Thumb`) was lower than the predicted thumb length given the student's height.

::: { .qti-item #b5_Error_02 }
:::::: { #4e6365a3-d1c5-42c9-ac40-615cd329765e .qti-question .essay points="1" max-words="200" }

What does a positive residual mean?

::::::::: { .feedback }

A positive residual means that the student's thumb was longer than its predicted length based on the student's height

:::::::::

::::::
:::

The residuals from the `Height` model represent the variation in `Thumb` that is *leftover* after we take out the part that can be explained by `Height`. As an example, take a particular student (highlighted in the plot below) with a thumb length of 70 mm. The residual of 7 means that the student's thumb is 7 mm longer than would have been predicted for this student based on their height.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/XN3St46R.png" width=80%  alt="A scatter plot of the distribution of Thumb by Height overlaid with the regression line in red. A single residual is drawn above the regression line as a vertical line from the data point to the model. The data point is labeled as: Thumb equals 70. The vertical line is labeled as: residual equals 7. The point along the regression line is labeled as: predicted Thumb equals 63." /></p>

Another way we could say this is: *controlling for* height, this student's thumb is 7 mm longer than expected. A positive residual indicates that a thumb is long for a person of that height. A negative residual indicates that a thumb is shorter than expected based on the person's height. These residuals may prompt us to ask, what *other stuff* besides `Height` might account for these differences?

### SS Error for the `Height` Model

Just like for other models we have seen (e.g., the empty model and the group model), the metric we use for quantifying total error from the `Height` model is the sum of squared residuals from the model, or SS Error. SS Error is calculated from the residuals in the same way as it is for a group model, by squaring and then summing the residuals (see figure below).

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/m4KFCHTd.png" width=80%  alt="A scatter plot of the distribution of Thumb by Height, overlaid with the regression line in red.  A few squared residuals are drawn above and below the regression model as vertical lines from the data points to the model that have been scaled into squares." /></p>

Compare the sums of squares for the empty model (SST) and the height model (SSE) for 6 data points in the figures below.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%">SS Total, Sum of Squared Residuals from empty model</th>
            <th style="width:50%">SS Error, Sum of Squared Residuals from height model</th>
    </thead>
    <tbody>
        <tr>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/npqd6mFr.png" alt="A scatter plot of the distribution of Thumb by Height, overlaid with the empty model in blue.  A few squared residuals are drawn above and below the model as vertical lines from the data points to the model that have been scaled into squares."/></p></td>
            <td><p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/m4KFCHTd.png" alt="A scatter plot of the distribution of Thumb by Height, overlaid with the height model in red.  A few squared residuals are drawn above and below the model as vertical lines from the data points to the model that have been scaled into squares." /></p></td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b5_Error_03 }
:::::: { #acce3c15-2561-4f3b-9e2f-fb5f660f5d1a .qti-question .multiple-choice points="1" }

Based on the squared residuals for these 6 data points, which model do you think would have a smaller sum of squared errors? Put another way, where, on average, are the squares smaller?

::::::::: { .choices }

- SS (SST) looks lower for the empty model
- [SS (SSE) looks lower for the Height model]{ .correct }

:::::::::

::::::

:::::: { #be4d3e4e-9e40-4f9e-95a7-d8aee47adef5 .qti-question .essay points="1" max-words="100" }

What does it mean if a model has a lower SS than the empty model?

::::::::: { .feedback }

If a model has a lower SS Error than the empty model (SS Total) it means that the model has reduced (or explained) some of the error in the outcome variable.

:::::::::

::::::
:::

### Using R to Compare SS for the `Height` Model and the Empty Model

Just like we did with the group models (e.g., `Height2Group` model and `Gender` model), we can use the `resid()` function to get the residuals from the `Height` model. We can then square them and sum them to get the SS Error from the model like this:

```
Height_model <- lm(Thumb ~ Height, data = Fingers)
sum(resid(Height_model)^2)
```

::: { .qti-item #b5_Error_04 }
:::::: { #ae5ac7b2-d288-4f5d-a069-481378e16615 .qti-question .multiple-choice points="1" }

The SS Total (from the empty model) was 11,880. Make a prediction: How will the SS Error (from the Height model) compare?

::::::::: { .choices }

- [SSE will be smaller than SST]{ .correct }
- SSE will be larger than SST
- SSE will be equal to SST

:::::::::

::::::
:::

The code below will calculate SST from the empty model and SSE from the height model. Run it to check our predictions about SSE.

```{ data-ckcode=true #B5_Code_Error_01 }
%%% setup
require(coursekata)

%%% prompt
# this calculates SST
empty_model <- lm(Thumb ~ NULL, data=Fingers)
print("SST")
sum(resid(empty_model)^2)

# this calculates SSE
Height_model <- lm(Thumb ~ Height, data = Fingers)
print("SSE")
sum(resid(Height_model)^2)

%%% test
ex() %>% check_error()
```

```
[1] "SST"
11880.2109191083

[1] "SSE"
10063.3491457795
```

Notice that the SST is the same as it was for the `Height2Group` model: 11,880. This is because the empty model hasn't changed; SST is still based on residuals from the grand mean of `Thumb`. The SSE (10,063) is *smaller* than SST because the residuals are smaller (as represented in the figures above by shorter lines). Squaring and summing smaller residuals results in a smaller SSE. The total error has been reduced by this regression model.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/Z4FvwdM4.png" width=80%  alt="Diagram showing the partitioning of Sum of Squares. On the left, a single circle represents SS Total from the Empty Model of Thumb. On the right, that same circle (representing Thumb) now intersects with another circle (representing Height). The part of Thumb that does not overlap with Height is labeled SS Error from the Height Model of Thumb, and the other circle is labeled as Height. The intersection where the two circles overlap is labeled as Error Reduced by Height." /></p>

::: { .qti-item #b5_Error_05 }
:::::: { #6162a072-8853-4350-8f29-a7ae62cd79d3 .qti-question .multiple-choice points="1" }

The SSE for the height model was 10,063. What part of the figure above represents this number?

::::::::: { .choices }

- Whole blue circle (on left)
- [Blue crescent shape (on right)]{ .correct }
- Dotted area
- White crescent shape (on right)

:::::::::

::::::

:::::: { #dff5adc9-9305-4d9c-887e-06fe0410785d .qti-question .multiple-choice points="1" scoring="partial" }

The SSE for the height model was 10,063. What does this mean? (Check all that apply.)

::::::::: { .choices }

- [The SSE for the `Height` model was a bit smaller than it was for the empty model.]{ .correct }
- The SSE for the `Height` model was a bit larger than it was for the empty model.
- We calculated the SSE incorrectly because SSE should equal SST.
- [The `Height` model has less unexplained error than the empty model.]{ .correct }
- [The `Height` model explains more of the error than the empty model.]{ .correct }

:::::::::

::::::
:::

### Comparing the Regression Line with the Mean

Recall that the mean is the middle of a univariate distribution. It is the balancing point of the distribution, where the residuals are perfectly balanced above and below. In a similar way, the regression line is the middle of a bivariate distribution between two quantitative variables. **Just as the sum of the residuals around the mean add up to 0, so too the sum of the residuals around the regression line also add up to 0.**

Here’s another cool relationship between the mean and regression line. It turns out that the best-fitting regression line will always pass through a point that is mean of both variables (this is called the *point of means*). So, if someone's height is exactly at the mean, their predicted thumb length will also be exactly at the mean.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/37K9DZTJ.png" width=80%  alt="A scatter plot of the distribution of Thumb by Height overlaid with the regression line in red. A horizontal line representing the mean of Thumb intersects with a vertical line representing the mean of Height at the point of means which also lies on the regression line." /></p>

Finally, just as the mean is the point in the univariate distribution at which the SS Error is minimized, the same is true of error around the regression line. The sum of the squared deviations of the observed points is at its lowest possible value around the best-fitting regression line.
