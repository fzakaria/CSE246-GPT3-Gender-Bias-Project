SELECT
    name,
    SUM(number) count
FROM
    `bigquery-public-data.usa_names.usa_1910_current`
WHERE
    gender = 'F'
    AND name NOT IN (
        SELECT
            name
        FROM
            `bigquery-public-data.usa_names.usa_1910_current`
        WHERE
            gender = 'M'
    )
GROUP BY
    name
HAVING
    count > 10000
ORDER BY
    count DESC