## 7.7 Error Reduced by the Group Model

Remember that our goal in adding an explanatory variable to the model was to *explain variation* in the outcome variable, or to put it another way, *reduce error* compared with the empty model.

To know that error has been reduced, and by how much it has been reduced, we will compare the sum of squared errors for the empty model with the sum of squared errors from the `Gender` model. If the sum of squared errors from the `Gender` model is smaller, then it has reduced error compared to the empty model.

::: { .qti-item #b3_ErrorReduc_01 }
:::::: { #d765a569-a3b1-4f30-bac5-d5b92c8930b2 .qti-question .multiple-choice points="1" }

Why do we use the sum of *squared* residuals instead of just the sum of the residuals to measure total error from a model?

::::::::: { .choices }

- [Because the sum of the residuals from a model that predicts the mean is always 0, whether it predicts one mean or two]{ .correct }
- Because the sum of the residuals becomes negative as we add more groups to the model
- Because the sum of the residuals is not as precise as the sum of squared residuals

:::::::::

::::::
:::

For the empty model, we take each residual from the model prediction (the mean for all students) and square it. Then we add up these squared residuals to get the sum of squared errors from the empty model. The special name we use to refer to the sum of squared errors from the empty model is SST, or Sum of Squares Total.

We have illustrated this idea for our subsample of six data points in the left panel of the figure below. The residuals are represented by the vertical lines from each data point to the empty model prediction. The square of each of these residuals is represented, literally, by a square.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th><i>SS Total</i>, Sum of Squared Residuals from empty model</th>
            <th><i>SS Error</i>, Sum of Squared Residuals from <code>Gender</code> model</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_07_ErrorReduced_1.jpg" width=100%  alt="On the left, a jitter plot of the distribution of Thumb by Gender in the Fingers data frame, overlaid with a horizontal line in blue showing the empty model for Thumb. A few squared residuals are drawn above and below the empty model as vertical lines from the data points to the model that have been scaled into squares."/></p>
</td>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_07_ErrorReduced_2.jpg" width=100%  alt="On the right, a jitter plot of the distribution of Thumb by Gender in the Fingers data frame, overlaid with a red horizontal line in each group showing the group mean. The residuals for the same data points as the jitter plot on the left have been squared around the group means." /></p>
</td>
        </tr>
    </tbody>
</table>
<br>

For the `Gender` model (represented in the right panel of the figure above), we take the same approach, only this time the residuals are based on the model predictions of the `Gender` model. Again, we can sum up these squared residuals across the whole dataset to get the sum of squared errors from the model.

Although the procedure for calculating sums of squares is identical for the empty and `Gender` models, for the `Gender` model (and indeed, for all models other than the empty model) we call this sum the SSE, or Sum of Squared Errors.

::: { .qti-item #b3_ErrorReduc_02 }
:::::: { #180b2367-ab9a-4f05-ad87-a91ffa30be47 .qti-question .multiple-choice points="1" }

In the figure above, look closely at the squared errors for our sample of 6 data points from both the empty model and the `Gender` model. Try visually adding the 6 squares for each model together in your mind. Just based on these 6 squared errors, which model do you think would have a smaller sum of squares?

::::::::: { .choices }

- The empty model
- [The `Gender` model]{ .correct }

:::::::::

::::::

:::::: { #bb958b72-c4a5-454b-aed0-c0aa826461de .qti-question .multiple-choice points="1" }

What do we call the sums of squares leftover from these two models?

::::::::: { .choices }

- For both models, SS Error
- [For the empty model, SS Total, and for the `Gender` model, SS Error]{ .correct }
- For the `Gender` model, SS Total, and for the empty model, SS Error
- For both models, SS Total

:::::::::

::::::
:::

When R fits a model – including the empty model – the particular values of the parameter estimates (the $b$s) minimize the sum of squared residuals.

To fit the empty model, R finds the particular value of $b_0$ that produces the lowest possible SS Error (also known as SS Total) for this dataset, which we know is the mean of `Thumb`. To fit the `Gender` model, R finds the particular values of $b_0$ and $b_1$ that produce the lowest possible SS Error for this dataset.

::: { .qti-item #b3_ErrorReduc_03 }
:::::: { #d805cf36-662f-4712-a62a-393a68304b3c .qti-question .multiple-choice points="1" }

What would R try to minimize if it were fitting a model with some other explanatory variable (e.g., `RaceEthnic` or `Height`)?

::::::::: { .choices }

- The SS Total
- [The SS Error]{ .correct }
- The SS Model

:::::::::

::::::

:::::: { #d927a302-ff98-4ec3-a4af-6e02292dd503 .qti-question .multiple-choice points="1" }

Which will usually be smaller? SS Total or SS Error?

::::::::: { .choices }

- SS Total
- [SS Error]{ .correct }
- Sometimes the SS Total is smaller; sometimes the SS Error is smaller.

:::::::::

::::::
:::
