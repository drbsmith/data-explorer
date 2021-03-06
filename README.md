# data-explorer

How much can we automatically extract from a dataset? This codebase takes a data set and runs as many hypothesis tests as we can come up with, to try and tell us about the nature of the data and what tools are most appropriate in analyzing it.

It learns in a dynamic-Baysian fashion, using training sets to propose the most probable interpretations of the data.

## Phase 1
Identify the most likely data type for each column. 

## Notes & ToDos

### Measures

* Timeseries: first, a hypothesis test to assess the probability that any element is a time stamp. Then, analysis that assesses distribution, clustering, trends in frequency.
* Text, language: Keywords, tags, hashtags, words. See "Strings", below. Also, see import strings, strings.punctuation for the power plays
* uuids, Tokens, IDs, categories: ints or textual labels
* Code, HTML, json, xml: identify, but propose analysis in later version.
* Freign keys, sub-tables, relational structures, meta d-type: in later version identify possible linkages between tables, across an entire database. Would be great for auto-documentation purposes
* Quantile stats: min, max, range, 5th %, 95th %, Q1, Q3, IQR
* Descriptive Stats: coeff of var, kurtosis, mean, median abs deviation, sum, skewness, variance, monotocity
* General: % distinct, missing
* Strings: 
** length [min, med, mean, max], 
** distinct char, distinct categories [letter, number, symbol, punct, etc.], unique punctuation in the column, unique alpha in the column
** script types [arabic, greek, latin, etc.], 
** unique values, % unique <-- the unique tests for ints, etc works the same here
** categories


### Hypotheses

* Entity ID, name, local/foreign keys
* ints: labels, IDs, keys, also treat as floats that have been rounded ->
* floats: continuous values, observations or measures of a thing
* Financial: is it money? Then see quantile, descriptive
** can we propose optimal number of modes that describe the data the best? , for any continuous numeric data


Missing values: an empty entry can be cast to int/float, it's still empty. In hypothesis testing these need to be excluded.

## References

https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html
