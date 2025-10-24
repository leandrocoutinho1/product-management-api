from pydantic import BaseModel

class UserRegisterDTO(BaseModel):
    username: str
    password: str

class UserLoginDTO(BaseModel):
    username: str
    password: str