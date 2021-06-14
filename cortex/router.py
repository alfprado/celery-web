from fastapi import APIRouter
from fastapi.responses import JSONResponse
from tasks import get_ibge, process_result
from models import Task, Result
from celery.result import AsyncResult
from celery import chain

router = APIRouter(
    tags=['IBGE']
)

@router.get('/', status_code=200)
def show(tabela, periodo, variavel, nivel):
    task_id = chain(
        get_ibge.s(tabela, periodo, variavel, nivel),
        process_result.s(),
    )()
    return {'task_id': str(task_id), 'status': 'Processing'}

@router.get('/result/{task_id}', response_model=Result, status_code=200)
async def fetch_result(task_id):
    task = AsyncResult(task_id)
    if not task.ready():
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': task_id, 'status': str(result)}