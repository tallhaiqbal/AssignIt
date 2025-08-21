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
    email: Optional[str] = None

#Task Scheme
#id, title, content, priority, deadline, type, Task_status
class TaskBase(BaseModel):
    title: str
    description: str
    priority: Optional[models.PriorityEnum] = None
    deadline: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    priority: Optional[models.PriorityEnum] = None
    deadline: Optional[datetime] = None