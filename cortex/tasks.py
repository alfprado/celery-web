from worker import celery_app
from util.gen_csv import create_file
from requests.exceptions import RequestException
import requests

@celery_app.task(bind=True)
def process_result(self, content):
    if content is not None:
        create_file(content)
        return 'SUCCESS'
    return 'ERROR'

@celery_app.task(
    bind=True,
    name='call_ibge',
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
    