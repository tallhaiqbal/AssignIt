from pydantic import BaseModel, EmailStr
from typing import Optional
from . import models
from datetime import datetime

class Createuser(BaseModel):
    name: str
    email: EmailStr
    password: str

class login(BaseModel):
    email: EmailStr
    password: str

#Token Schema
class TokenData(BaseModel):
    id: Optional[str] = None

#Task Scheme
#id, title, content, priority, deadline, type, Task_status
class TaskBase(BaseModel):
    title: str
    description: str
    status: models.StatusEnum = models.StatusEnum.todo
    priority: Optional[models.PriorityEnum] = None
    deadline: Optional[datetime] = None
    completed_at: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[models.PriorityEnum] = None
    status: Optional[models.StatusEnum] = None
    deadline: Optional[datetime] = None


#Response Schemas

class taskResp(BaseModel):
    title: str
    discription: str
    priority: Optional[models.PriorityEnum] = None
    deadline: Optional[datetime] = None

    class config:
        orm_mode = True

class userResp(BaseModel):
    name: str
    email: EmailStr

    class config:
        orm_mode = True