# Generate JWT Token
import jwt 
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from fastapi import Depends
from . import schema

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#verify
def verify_token(token: str, credential_exeption):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email: str =  payload.get("user_email")

        if email is None:
            raise credential_exeption
        token_data = schema.TokenData(email =  email)
    except InvalidTokenError:
        raise credential_exeption
    return token_data

# function to validate access on each user request
def get_current_user(token: str = Depends(oauth2_schema)):
    credential_exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate Credentials")

    return token, credential_exeption