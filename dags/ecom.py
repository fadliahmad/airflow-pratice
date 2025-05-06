from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from pendulum import datetime, duration

@dag(
    start_date=datetime(2025, 1, 1), 
    schedule='@daily', 
    catchup=True, 
    description='This DAG proceses ecommerce data', 
    tags=['team_A', 'ecom'], 
    default_args= {"retries": 1}, 
    dagrun_timeout=duration(minutes=20), 
    max_consecutive_failed_dag_runs=2
    )  

def ecom(): 

    ta = EmptyOperator(task_id='ta')

ecom()