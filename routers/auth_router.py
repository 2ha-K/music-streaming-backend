from fastapi import APIRouter
from pydantic import BaseModel
from services.auth_service import register, login

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

class Register(BaseModel):
    email: str
    password: str
    username: str
    display_name: str
    role: str = "audience"

@router.post("/register")
def register_api(payload: Register):
    email = payload.email
    username = payload.username
    display_name = payload.display_name
    role = payload.role
    password = payload.password
    result = register(email, password, username, display_name, role)
    return {"result": result}


class Login(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_api(payload: Login):
    email = payload.email
    password = payload.password
    result = login(email, password)
    return {"result": result}
