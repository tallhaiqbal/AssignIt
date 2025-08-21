from pydantic import BaseModel, EmailStr

class user(BaseModel):
    name: str
    email: EmailStr
    password: str