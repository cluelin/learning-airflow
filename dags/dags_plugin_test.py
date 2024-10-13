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
        bash_command="/opt/airflow/plugins/shell/select.sh aaa",
    )

    bash_t3 = BashOperator(
        task_id="bash_t3",
        bash_command="ls -al /opt/airflow/plugins/shell",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="/opt/airflow/plugins/shell/select.sh aaa",
    )

    from airflow.utils.edgemodifier import Label

    bash_t1 >> [Label('label 1'), Label('label 2')] >> [bash_t2, bash_t3]
    
