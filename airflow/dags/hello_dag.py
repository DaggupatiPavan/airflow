from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define the default arguments dictionary
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='A simple hello world DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Define the task function
def print_hello():
    print("Hello World")

# Define the task
hello_world_task = PythonOperator(
    task_id='hello_world',
    python_callable=print_hello,
    dag=dag,
)

# Set the task in the DAG
hello_world_task
