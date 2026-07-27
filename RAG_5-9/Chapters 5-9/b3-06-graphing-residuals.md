## 7.6 Graphing Residuals From the Model

You might wonder, why are we bothering to generate and save residuals? There are a lot of reasons but one short answer is: it helps us to understand the error around our model, and can suggest ways of improving the model.

Just as the first thing we do when looking at a dataset is to examine the distributions of the variables, it is good to get in the habit of examining the distributions of residuals after we fit a new model.

In the following window, we have provided the code to create histograms of `Thumb` in a facet grid by `Gender`. Try modifying it to generate histograms of `Gender_resid` in a facet grid by `Gender`.

```{ data-ckcode=true #B3_Code_Graphing_01 }
%%% setup
require(coursekata)

%%% prompt
# this creates the residuals from the Gender_model
Gender_model <- lm(Fingers$Thumb ~ Fingers$Gender)
Fingers$Gender_resid <- resid(Gender_model)

# this creates histograms of Thumb for each Gender
# modify it to create histograms of Gender_resid for each Gender
gf_histogram(~Thumb, data = Fingers) %>%
  gf_facet_grid(Gender ~ .)

%%% solution
# this creates the residuals from the Gender_model
Gender_model <- lm(Fingers$Thumb ~ Fingers$Gender)
Fingers$Gender_resid <- resid(Gender_model)

# this creates histograms of Thumb for each Gender
# modify it to create histograms of Gender_resid for each Gender
gf_histogram(~Gender_resid, data = Fingers) %>%
  gf_facet_grid(Gender ~ .)

%%% test
ex() %>% {
  check_or(.,
    check_function(., "gf_histogram") %>% {
      check_arg(., "object") %>% check_equal()
      check_arg(., "data") %>% check_equal()
    },
    override_solution(., "gf_histogram(Fingers, ~ Gender_resid)") %>%
      check_function("gf_histogram") %>% {
        check_arg(., "object") %>% check_equal()
        check_arg(., "gformula") %>% check_equal()
      }
  )
  check_function(., "gf_facet_grid") %>%
    check_arg("...") %>%
    check_equal(incorrect_msg = "Make sure you keep the code to create a grid faceted by `Gender`")
}
```

Compare the histograms of residuals from the `Gender_model` with histograms of thumb length. Here we’ve depicted the histograms of `Thumb` by `Gender` (in teal) next to the histograms of `Gender_resid` by `Gender` (in darker gray).

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%"><code>Thumb</code></th>
            <th style="width:50%"><code>Gender_resid</code></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/vQ3d7cv2.png" width=100%  alt="On the left, a faceted histogram of Thumb faceted by Gender (female and male), in teal. The distributions are both roughly normal but the male group is distributed slightly more to the right." /></p>
</td>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_06_GraphingResid_1.jpg" width=100%  alt="On the right, a faceted histogram of Gender_resid faceted by Gender (female and male), in gray. The distributions are both roughly normal and are mostly overlapping." /></p>
</td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b3_Graphing_01 }
:::::: { #6e66c70a-3aeb-4bf3-8993-ff2c16122382 .qti-question .multiple-choice points="1" }

What do you notice about these pairs of histograms?

::::::::: { .choices }

- [In the `Thumb` histograms (in teal), it seems like the males are shifted higher than the females, but that is not true of the `Gender_resid` histograms.]{ .correct }
- In the `Gender_resid` histograms (in gray), it seems like the males are shifted higher than the females, but that is not true of the `Thumb` histograms.

:::::::::

::::::
:::

The residuals of the `Gender_model` represent the variation leftover after *taking out* the part of the variation that can be explained by `Gender`. The figures below show the mean `Thumb` length and mean `Gender_resid` of the two `Gender` groups.

<style>
    table.table--outlined { border: 1px solid black;  border-collapse: collapse; margin-left: auto; margin-right: auto;  }
    table.table--outlined th, table.table--outlined td  { border: 1px solid black; padding: .5em; }
</style>
<table class="table--outlined">
    <thead>
        <tr>
            <th style="width:50%">mean <code>Thumb</code> of each group</th>
            <th style="width:50%">mean <code>Gender_resid</code> of each group</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/pRG8SZLP.png" width=100%  alt="A faceted histogram of the distribution of Thumb by Gender on the left with vertical lines showing the mean for each Gender group. The mean for the male group is higher than the mean for the female group." /></p>
</td>
            <td>
<p align="center" style="text-align: center;"><img src="https://coursekata-course-assets.s3.us-west-1.amazonaws.com/UCLATALL/czi-stats-course/b3_06_GraphingResid_2.jpg" width=100%  alt="A faceted histogram of the distribution of Gender_resid by Gender on the right with vertical lines showing the mean for each Gender_resid group. The means for both the male group and the female group are 0." /></p>
</td>
        </tr>
    </tbody>
</table>
<br>

::: { .qti-item #b3_Graphing_02 }
:::::: { #96a03ec4-f820-43aa-831e-54a9e346c6ec .qti-question .multiple-choice points="1" }

Above, in the histogram of the residuals (in gray), why are the means of `Gender_resid` for the two groups not different any more?

::::::::: { .choices }

- [Because the residuals are what is left over after subtracting the means of the two `Gender` groups from the original thumb lengths.]{ .correct }
- Because the residuals are what is left over after modeling the data with `Gender_model`.
- Because the residuals are what is left over after taking out the effects of `Gender`.
- Because the residuals are what is left over after accounting for variation in `Gender`.
- All of the above are true.

:::::::::

::::::

:::::: { #0d37a62a-4d85-4290-a4f4-02fdd73c94d4 .qti-question .multiple-choice points="1" }

Above, in the histogram of the residuals (in gray), why are the means of `Gender_resid` for the two groups equal to 0?

::::::::: { .choices }

- [Because the mean of a bunch of residuals requires adding up all the residuals. Residuals are perfectly balanced around means so adding them up will equal 0.]{ .correct }
- Because the average thumb length for each group is 0.
- Because of coincidence; in this particular example, the mean of the residuals is equal to 0, but that's rarely the case.
- All of the above are true.

:::::::::

::::::
:::
