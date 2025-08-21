from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Hashing User Password
def hash(password: str):
    return pwd_context.hash(password)

#Verify User Password
def Verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)