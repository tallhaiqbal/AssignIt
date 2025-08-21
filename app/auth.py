from fastapi import APIRouter, Depends, HTTPException, status
from . import oauth2, schema, database, models, utils
from sqlalchemy.orm import Session

# Login User

router = APIRouter(prefix="/login", tags=["Authentication"])

@router.post("/")
def login(user: schema.login, db: Session = Depends(database.get_db)):
    user_query = db.query(models.User).where(models.User.email == user.email).first()

    if not user_query:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.Verify(user.password, user_query.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    token = oauth2.create_access_token(data = {"user_id": user_query.id})

    return{"Access_token": token, "token_id": "bearer"}