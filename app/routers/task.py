from fastapi import APIRouter, status, HTTPException, Depends
from .. import schema, database, models
from sqlalchemy.orm import Session
from .. import oauth2

router = APIRouter(prefix="/tasks", tags=["Task Management"])

#create task
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_task(task: schema.TaskCreate, db: Session = Depends(database.get_db), current_user: schema.TokenData = Depends(oauth2.get_current_user)):
    query = models.Task(creator_id= current_user.id, **task.model_dump()) 
    # query.creator_id = current_user.id # type: ignore
    db.add(query)
    db.commit()
    db.refresh(query)
    return {"Message": "Task Created", "Data": query}