# Register User
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import schema, models, utils
from ..database import get_db

router = APIRouter(prefix="/user", tags=["Register/Sign Up"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def register(user: schema.Createuser, db: Session = Depends(get_db), ):
    # Hash User Password
    hashed = utils.hash(user.password)
    user.password = hashed
    register_user = models.User(**user.model_dump())
    db.add(register_user)
    db.commit()
    return {"Message": f"Welcome to AssignIt {register_user.name}, Your account is successfully created"}