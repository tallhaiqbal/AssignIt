from fastapi import APIRouter, status, HTTPException, Depends
from .. import schema, database, models
from sqlalchemy.orm import Session
from .. import oauth2
from typing import Optional

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



@router.get("/")
def filter_tasks(db:Session = Depends(database.get_db), current_user: schema.TokenData = Depends(oauth2.get_current_user), status: models.StatusEnum | None = None, search: Optional[str] = "", priority: models.PriorityEnum | None = None):
    query = db.query(models.Task)

    # Login needed where user can only retirive his own tasks & not others

    if search:
        query = query.filter(models.Task.title.contains(search))

    if status:
        query = query.filter(models.Task.status == status)

    if priority:
        query = query.filter(models.Task.priority == priority)
    
    task = query.all()

    return task

# update status, and delete.