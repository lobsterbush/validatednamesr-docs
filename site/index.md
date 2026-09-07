# validatednamesr

<div class="repllm-hero">
<p class="eyebrow">Research software · R package</p>
<p class="hero-title">Choose names for your experiment.</p>
<p class="hero-summary">We built validatednamesr to help choose experimental names using evidence about how people perceive them.</p>
<p class="hero-links"><a class="hero-primary" href="#installation">Get started ↗</a><a href="reference/index.html">See the functions →</a></p>
<p class="hero-meta">Jae Yeon Kim and Charles Crabtree</p>
</div>

[![validatednamesr: Human – AI (editor) 👤✏️🤖](reference/figures/provenance.svg)](https://thelatentreview.com/provenance/)

## Provenance

**Human – AI (editor) 👤✏️🤖**

We wrote every initial version ourselves, without AI. We've used AI only for
later updates and code fixes. I'm Charles Crabtree, and this is my account of
how the package was made.

The label follows [The Latent Review’s provenance standard](https://thelatentreview.com/provenance/),
shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
The software remains MIT licensed.

This documentation copy is maintained by Charles Crabtree. The
[upstream package](https://github.com/jaeyk/validatednamesr) and
[original documentation](https://jaeyk.github.io/validatednamesr/)
are maintained by Jae Yeon Kim. Package code comes from the pinned upstream source. I've edited the explanatory
text in this documentation copy; the function arguments and behaviour are unchanged.


Authors: [Jae Yeon Kim](https://jaeyk.github.io/) and [Charles Crabtree](https://charlescrabtree.com/)

## Why we built it

A name can signal more than the racial category a researcher intends. People
may also make assumptions about citizenship, education, or income. We want to
see those perceptions before choosing names for an experiment.

This R package provides functions to perform each task based on a validated dataset of 600 names (100 white, 300 Asian, 100 black, and 100 Hispanic) published in *Nature Scientific Data* ([Crabtree, Kim, Gaddis, Holbein, Guage, and Marx, 2023](https://www.nature.com/articles/s41597-023-01947-0#Sec10)).

Use several names per group, then check whether their perceived attributes fit
your design. You might want similar income ratings across racial groups, or
you might want to vary both. The package helps you select names under those
constraints; the design decision is yours.

## Installation 

``` r
devtools::install_github("jaeyk/validatednamesr", dependencies = TRUE)
```

## Usage 

### View and load datasets 

Start with `view_data()` to see the available files and their descriptions.

``` r
library(validatednamesr)
view_data()
```

Use `load_data()` to read one of those files. You can identify it by filename or note.

``` r
# Read by filename
raw_names <- load_data(file_name = "names.rds")

# Or read the same file by its note
raw_names <- load_data(file_note = "Raw names")
```

### Select names 

Pass `"Asian"`, `"Black"`, `"Hispanic"`, or `"White"` to `race` in `select_names()`. These are the intended signals used in the study.

The pinned package returns six columns: `name`, `identity`, `pct_correct`,
`avg_income`, `avg_education`, and `avg_citizenship`. The first two identify
the name and its intended signal. `pct_correct` is the share who perceived that
signal. Income and education are average ratings on 1–5 scales; citizenship
is a share on a 0–1 scale.

``` r
asian_names <- select_names(race = "Asian") # Asian signalling names 

asian_names
```

By default, at least 80% of respondents must have perceived the intended racial signal. Set `pct_correct` to change that threshold.

``` r
# Lower the required share from 80% to 70%.

lower_threshold_names <- select_names(race = "Asian", pct_correct = 0.7)
```

The function samples five names by default. Set `n_names` to request more, and set a random seed if you need to reproduce the selection.

``` r
# Sample ten eligible names.
set.seed(42)

greater_n_names <- select_names(race = "Asian", n_names = 10)
```

You can order eligible names by a validation measure with `order_by_var`.
Use `pct_correct` for the share who perceived the intended racial signal,
`avg_income` or `avg_education` for average ratings, or `avg_citizenship` for
the share perceived as citizens. It selects the highest values and keeps ties, so an ordered result can contain more than `n_names` rows.

``` r
top_correct_names <- select_names(race = "Asian", order_by_var = "pct_correct")
```

`select_names_all()` combines the four racial groups using the default
selection for each. In this pinned version, it accepts selection arguments
but doesn't pass them to `select_names()`. Call `select_names()` separately
for each group if you want to change the threshold, ordering, or sample size.

``` r
all_race_names <- select_names_all()
```

## How to cite

Kim, J and Crabtree, C. (2022). validatednamesr: R package for viewing, loading, and visualizing the Validated Names for Experimental Studies on Race and Ethnicity datasets.
