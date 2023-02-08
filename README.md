This is data from various sources that I try to get for [Beyond Cars](https://github.com/andymckay/beyond-cars).

# The data

## ICBC data

Taken from [this site](https://icbc.com/about-icbc/newsroom/Pages/Statistics.aspx) and covered by ICBC's [Open Data License](https://icbc.com/policies/Pages/open-data-licence.aspx). Which allows: "you a worldwide, royalty-free, perpetual, non-exclusive licence to use the Information, including for commercial purposes". However, this requires attribution:

*Contains information licensed under ICBC’s Open Data Licence.*

Non-endorsement:

*All analysis, inferences, opinions, and conclusions drawn in this repository are those of the authors, and do not reflect the opinions, position or policies of ICBC.*

## Statistics Canada data

The terms and conditions [are here](https://www.statcan.gc.ca/en/reference/terms-conditions?MM=1) and data is under the [Statistics Canada Open License](https://www.statcan.gc.ca/eng/reference/licence). Which according to [this page](https://www.statcan.gc.ca/en/reference/copyright) "allows you to use Statistics Canada information without restrictions on sharing and redistribution, for commercial and non-commercial purposes".

# The rest

## Conventions

Files starting with `raw-...` are just data straight from the websites, in whatever format we can get to then convert into something better. It should end with a relevant date for example: `...-2021`.

Data will be put in comma seperated CSV files.

All times UTC.

All dates in ISO 8601, `YYYY-MM-DD` ([see also](https://twitter.com/TerribleMaps/status/1620111664078290945)).

The language of choice here is [Python](https://www.python.org/) 😀.