SELECT
    name,
    gender,
    SUM(number) count
FROM
    `bigquery-public-data.usa_names.usa_1910_current`
GROUP BY
    name,
    gender
HAVING
    count > 10000
ORDER BY
    gender,
    count DESC