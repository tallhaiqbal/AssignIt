from fastapi import APIRouter, status, HTTPException, Depends
from .. import schema, database, models
from sqlalchemy.orm import Session
from .. import oauth2
from typing import Optional

router = APIRouter(prefix="/tasks", tags=["Task Management"])

#create task
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.taskResp)
def create_task(task: schema.TaskCreate, db: Session = Depends(database.get_db), current_user: schema.TokenData = Depends(oauth2.get_current_user)):
    query = models.Task(creator_id= current_user.id, **task.model_dump()) 
    # query.creator_id = current_user.id # type: ignore
    db.add(query)
    db.commit()
    db.refresh(query)
    return {"Message": "Task Created", "Data": query}



@router.get("/" ,status_code=status.HTTP_200_OK)
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

# update
@router.put("/{id}",status_code=status.HTTP_200_OK)
def update_task(id: int, task: schema.TaskUpdate, db: Session = Depends(database.get_db), current_user: schema.TokenData = Depends(oauth2.get_current_user)):
    update_query = db.query(models.Task).where(models.Task.id == id, models.Task.creator_id == current_user.id)
    update = update_query.first()
    if update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    
    update_data = {getattr(models.Task, key): value for key, value in task.model_dump(exclude_unset=True).items()}
    update_query.update(update_data, synchronize_session=False)

    # update_data = task.model_dump(exclude_unset=True)
    # for field, value in update_data.items():
    #     setattr(task, field, value)

    db.commit()
    db.refresh(update)
    return update

#delete
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, db: Session = Depends(database.get_db),  current_user: schema.TokenData = Depends(oauth2.get_current_user)):
    delete_query = db.query(models.Task).where(models.Task.id == id, models.Task.creator_id == current_user.id)
    query = delete_query.first()

    if query is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    
    delete_query.delete(synchronize_session=False)
    db.commit()
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Task Deleted")

#Namz