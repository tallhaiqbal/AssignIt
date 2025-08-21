from fastapi import APIRouter, status, HTTPException
from .. import schema

router = APIRouter(prefix="/tasks")

#create task
# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_task(task: schema.TaskCreate, )