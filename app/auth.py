from fastapi import APIRouter, Depends, HTTPException, status
from . import schema, database, models, utils, oauth
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
    
    token = oauth.create_access_token(data = {"user_email": user_query.email})

    return{"Access_token": token, "token_id": "bearer"}