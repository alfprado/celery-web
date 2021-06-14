from pydantic import BaseModel

class Task(BaseModel):
    task_id: str
    status: str

class Result(BaseModel):
    task_id: str
    status: str