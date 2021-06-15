from fastapi import APIRouter
from fastapi.responses import JSONResponse
from tasks import get_ibge, process_result
from models import Result
from celery.result import AsyncResult
from celery import chain

router = APIRouter(
    tags=['IBGE']
)

@router.get('/', status_code=200)
def show(tabela, periodo, variavel, nivel):
    task_id = chain(
        get_ibge.s(tabela, periodo, variavel, nivel),
        process_result.s(),)()
    return {'task_id': str(task_id.parent), 'status': 'Processing'}

@router.get('/result/{task_id}', response_model=Result, status_code=200)
async def fetch_result(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})

    if task.state == 'FAILURE':
        return {'task_id': task_id, 'status': f'ERROR - {task.result}'}
    if task.state == 'SUCCESS':
        return {'task_id': task_id, 'status': 'SUCCESS'}