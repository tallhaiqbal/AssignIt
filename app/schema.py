from pydantic import BaseModel, EmailStr

class Createuser(BaseModel):
    name: str
    email: EmailStr
    password: str