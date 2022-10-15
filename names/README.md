# Gender names

Using the BigQuery public data set for USA births `bigquery-public-data.usa_names.usa_1910_current`, we collect gender specific names.

```console
> bq query --max_rows=10000 --use_legacy_sql=false --format=csv "$(<all-names.sql)" > names.csv
```

We will then split the names into male-only, female-only & unisex names.
For posterity, the archived full data is included as `names.zip` which can be found from https://www.ssa.gov/OACT/babynames/limits.html