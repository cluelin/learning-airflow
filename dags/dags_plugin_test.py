from airflow.models.dag import DAG
import datetime

import pendulum

from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_plugin_test",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60)
) as dag:
    
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="/opt/airflow/plugins/shell/select.sh",
    )

    bash_t3 = BashOperator(
        task_id="bash_t3",
        bash_command="ls -al /opt/airflow/plugins/shell",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2
    bash_t3
