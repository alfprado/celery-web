from worker import celery_app
from util.util import create_file, read_db
from requests.exceptions import RequestException
from celery import chain
import requests


@celery_app.task(
    bind=True,)
def process_result(self, content):
    if content is not None:
        create_file(self.request.id, content)
        return 'SUCCESS'
    return 'ERROR'

@celery_app.task(
    bind=True,
    max_retry=5,
    retry_backoff=True,
    autoretry_for=(RequestException,)
    )
def get_ibge(self, tabela, periodo, variavel, nivel):
    response = requests.get(f'http://api.sidra.ibge.gov.br/values/t/{tabela}/p/{periodo}/v/{variavel}/{nivel}/all')
    
    if not response.ok:
        raise ValueError(response.text)

    if response.status_code == 200:
        return response.json()

@celery_app.task()
def call_api_schedule():
    for item in read_db():
        item = item.split(',')
        chain(
            get_ibge.s(item[0], item[1], item[2], item[3]),
            process_result.s(),)()