from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users = []

class RegisterUser(BaseModel):
    username: str
    password: str
    role: Optional[str] = "volunteer"

class LoginUser(BaseModel):
    username: str
    password: str

@app.post("/auth/register")
def register(user: RegisterUser):
    for u in users:
        if u["username"] == user.username:
            raise HTTPException(status_code=400, detail="User already exists")
    users.append(user.dict())
    return {"message": "User registered successfully"}

@app.post("/auth/login")
def login(user: LoginUser):
    for u in users:
        if u["username"] == user.username and u["password"] == user.password:
            return {"access_token": "fake-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")