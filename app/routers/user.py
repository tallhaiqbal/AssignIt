# Register User
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from .. import schema
from ..database import get_db

router = APIRouter(prefix="/user")

# @router.post("/")
# def register(user: schema.user, db: Session = Depends(get_db), status_code=status.HTTP_201_CREATED):
#     db.query()