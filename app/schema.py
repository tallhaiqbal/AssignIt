from pydantic import BaseModel, EmailStr

class Createuser(BaseModel):
    name: str
    email: EmailStr
    password: str

class login(BaseModel):
    email: EmailStr
    password: str


#Task Scheme
#id, title, content, priority, deadline, type