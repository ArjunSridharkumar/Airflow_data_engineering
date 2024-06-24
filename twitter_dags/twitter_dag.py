from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from twitter_etl import twitter_etl
from datetime import datetime

default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'start_date':datetime(2021,11,8),
    'email':['airflow#examples.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':0,
    'retry_delay':False
}
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description="Airflow ETL"
)

run_etl  = PythonOperator(
    task_id= 'complete_twitter_etl',
    python_callable=twitter_etl,
    dag=dag
)