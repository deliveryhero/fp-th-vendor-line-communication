from google.cloud import bigquery
from google.oauth2 import service_account



key_path = "C:/Users/l.harchandani/Desktop/HAH/di-th-auto-253de33a30ba.json"

credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/cloud-platform"],
    )

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")

def query_BQ_table(query):
    job_config = bigquery.QueryJobConfig()
    return client.query(query, job_config=job_config).to_dataframe()

def record_line_communication_logs(table_id, rows_to_insert):
    status = client.insert_rows_json(table_id, rows_to_insert)
    return status


    
