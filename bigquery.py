from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
QUERY = (
    'SELECT * FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    '--WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY).to_dataframe()  # API request
#rows = query_job.result()  # Waits for query to finish
pass
# for row in rows:
#     print(row.name)