from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    print("Hello")
    return {"message": "Welcome to the AssignIt"}