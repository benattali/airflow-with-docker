from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

START_DATE = datetime.utcnow() - timedelta(days=1)

with DAG(dag_id='log_pip_freeze', schedule_interval=None, catchup=False, start_date=START_DATE) as dag:

    log_pip_freeze = BashOperator(
        task_id="freeze",
        bash_command="pip freeze",
        dag=dag)
