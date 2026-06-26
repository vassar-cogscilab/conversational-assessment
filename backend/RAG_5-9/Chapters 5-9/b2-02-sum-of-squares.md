## 6.2 The Beauty of Sum of Squares

As it turns out, Sum of Squares (SS) has a special relationship to the mean. In the previous chapter we extolled the virtues of the mean. Now it’s time to start appreciating the beauty of sum of squares!

### Sum of Squares is Minimized at the Mean

The advantage of SS as a measure of total error is that it is minimized exactly at the mean. And because our goal in statistical modeling is to reduce error as much as possible, this is a good thing.

Let's explore this idea and see if it really holds up. As a reminder, if we use the mean of 60.1 mm to predict thumb length, and then square and sum the residuals from the mean across all rows in the `Fingers` dataset, we get 11,880.

```
model <- mean(Fingers$Thumb)
sum((Fingers$Thumb - model)^2)
```

```
11880.2109191083
```

By saying the sum of squares is minimized at the mean we are saying that if we calculated residuals from any number other than the mean, the sum of squares would be larger than 11880.21. Is this true?

::: { .qti-item #b2_Sum_11 }
:::::: { #f7b7e04f-d857-4eb0-98bc-407f16b062c8 .qti-question .multiple-choice points="1" }

What do you think? If we used 60.0 as a model of thumb length instead of 60.1, what would you predict would happen to the sum of squares?

::::::::: { .choices }

- [it would be larger than 11880.21]{ .correct }
- it would be smaller than 11880.21
- there is no way to know without calculating the sum of squares

:::::::::

::::::
:::

In the code window below, we've set the mean of `Thumb` as the model prediction (`model <- 60.1`). Run the code and confirm that you get 11880.21 as the sum of squares.

```{ data-ckcode=true #B2_Code_Sum_01 }

%%% setup
require(coursekata)

%%% prompt
# this sets the model at a particular value
model <- 60.1

# this calculates the sum of squares from the model
sum((Fingers$Thumb - model)^2)

%%% solution
# this sets the model at a particular value
model <- 60.1

# this calculates the sum of squares from the model
sum((Fingers$Thumb - model)^2)

%%% test
ex() %>% check_error()
```

Now change the model from 60.1 to 60.0 and run the code again. What happens to the sum of squares? If SS is really minimized at the mean, then it should be greater than 11,880.21 when you use any number other than the mean.

Try using some other numbers as the model and see if you can make the SS go lower! We've tried some ourselves and plotted them on the graph below.

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/1yF8gGkN.png" width=80% alt="Scatter plot of SS on the y-axis and model on the x-axis. The points are distributed in a curved shape, starting near the midrange of SS and a model of 40, then dropping down to its lowest SS of 11,880 near a model of 60, and curving back up as the model goes up to 90." /></p>

When we plot the sums of squares this way they form a pattern – a kind of parabola (if you remember the shape from your algebra days). In fact, it can be proven mathematically, using calculus, that the sums of squares can never be lower for any number other than at the mean of the distribution. (A smoothed out version of the function is shown below).

<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/2m3hkZSn.png" width=80% alt="Scatter plot of SS on the y-axis and model on the x-axis. The points are distributed in a curved shape, and are overlaid with a smoothed out line along the points. The lowest point of the curve is the mean at a model of 60." /></p>

### The Mean and SS Go Hand-in-Hand

Because SS is minimized at the mean, it is a useful measure of error when our model is the mean. If we were to choose another number, such as the median, to model a distribution, we would probably choose a different measure of error – presumably one that is minimized at the median. In this course we focus primarily on the mean, so we will choose SS as our preferred measure of error.

At first glance, many topics in statistics seem like part of some endless list of unrelated formulas—the mean, the sum of squares, linear models. But hopefully you are starting to see that these all fit together. The relationship between the mean and the SS is actually just one example of the interlocking relationships that connect all these concepts. The sum of squares will link up with other ideas in statistics later.

It is somewhat like the Pythagorean Theorem. You learned in school that the square of the hypotenuse of a right triangle is equal to the sum of the squares of the two sides. Thus, $a^2+b^2=c^2$. Squaring the sides makes everything add up and fit together. But if you don’t square them, the theorem no longer holds: $a+b\neq{c}$. By using sum of squares as a quantification of total error, lots of things will fit together that otherwise would not.

### Finding Sum of Squares

Hopefully we have convinced you that SS goes hand-in-hand with the mean. More generally, we will use SS as our indication of model fit – and seek to minimize it – for all models we consider under the General Linear Model (GLM). So far, we have only explored one model – the empty model ($Y_i=b_0+e_i$) – in which $b_0$ represents the sample mean (which is also our estimate of the parameter, the population mean).

As we move later to fit more complex models to data we will rely on ANOVA tables to compute the sums of squares. (ANOVA stands for ANalysis Of VAriance.) In this book we will use the `supernova()` function in R to produce ANOVA tables. Let's see how it works for the empty model of `Thumb`.

```
supernova(empty_model)
```

In the code window below, save the best-fitting empty model of `Thumb` as `empty_model`.  Then try out the `supernova()` function, using `empty_model` as the input.

```{ data-ckcode=true #B2_Code_Sum_02 }
%%% setup
require(coursekata)

%%% prompt
# create an empty model of Thumb length from Fingers
empty_model <-

# analyze the model with supernova() to get the SS
supernova()

%%% solution
# create an empty model of Thumb length from Fingers
empty_model <- lm(Thumb ~ NULL, data = Fingers)

# analyze the model with supernova() to get the SS
supernova(empty_model)

%%% test
ex() %>% {
    check_object(., "empty_model") %>% check_equal()
    check_output_expr(., "supernova(empty_model)")
}
```

<pre><code>Analysis of Variance Table (Type III SS)
Model: Thumb ~ NULL

                               SS  df     MS   F PRE   p
----- ----------------- --------- --- ------ --- --- ---
Model (error reduced) |       --- ---    --- --- --- ---
Error (from model)    |       --- ---    --- --- --- ---
----- ----------------- --------- --- ------ --- --- ---
Total (empty model)   | <mark>11880.211</mark> 156 76.155            </code></pre>

As you can see, most cells in this ANOVA table are empty; we will be filling them up later as we learn how to fit more complex models. For now, we will focus on the last row, labeled `Total (empty model)`, and the column labeled `SS`.

In the table, the SS for the empty model is 11880.211, the same number we got before by calculating residuals, squaring them, and then summing them across each row of the dataset.

::: { .qti-item #Ch6_Sum_3 }
:::::: { #aefc3124-1dcf-474d-8d5b-c9c0d68e9782 .qti-question .multiple-choice points="1" }

We got an SS of 11,880. What unit would be attached to this number?

::::::::: { .choices }

- Inches
- Not possible to tell
- Millimeters
- [Square millimeters]{ .correct }

:::::::::

::::::
:::
