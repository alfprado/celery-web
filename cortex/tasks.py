from worker import celery_app
from celery.utils.log import get_task_logger
from httpx import get
from util.gen_csv import create_file

@celery_app.task()
def process_result(content):
    if content is not None:
        create_file(content)

@celery_app.task(
    name='call_ibge',
    max_retry=5,
    retry_backoff=3
    )
def get_ibge(tabela, periodo, variavel, nivel):
    response = get(f'http://api.sidra.ibge.gov.br/values/t/{tabela}/p/{periodo}/v/{variavel}/{nivel}/all')
    if response.status_code == 200:
        return response.json()
    
