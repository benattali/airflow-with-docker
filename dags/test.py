from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

from scripts.test import some_func

START_DATE = datetime.utcnow() - timedelta(days=1)

with DAG(dag_id='test_dag', schedule_interval=None, catchup=False, start_date=START_DATE) as dag:
    some_func = PythonOperator(
        task_id="some_func",
        python_callable=some_func,
        dag=dag)
