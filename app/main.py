from fastapi import FastAPI, APIRouter
from .routers import user, task
from . import models, auth
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(task.router)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    print("Hello")
    return {"message": "Welcome to the AssignIt From VM"}

# Create models for user table
# create schema for login validation