from fastapi import FastAPI, APIRouter
from .routers import user
from . import models, auth
from .database import engine

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    print("Hello")
    return {"message": "Welcome to the AssignIt"}

# Create models for user table
# create schema for login validation