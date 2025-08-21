# Register User
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import schema, models
from ..database import get_db

router = APIRouter(prefix="/user")

@router.post("/", status_code=status.HTTP_201_CREATED)
def register(user: schema.Createuser, db: Session = Depends(get_db), ):
    register = models.User(**user.model_dump())
    db.add(register)
    db.commit()
    return {"Message": f"{register.name}, Your account is created"}