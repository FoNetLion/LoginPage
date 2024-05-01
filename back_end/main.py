from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    # Thêm phiên bản localhost khác nếu cần
    "http://192.168.10.3:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Sử dụng danh sách origins đã định nghĩa
    allow_credentials=True,
    allow_methods=["*"],  # Cho phép tất cả các phương thức HTTP
    allow_headers=["*"],  # Cho phép tất cả các tiêu đề
)

# Dummy data for users
users_db = {
    "user@example.com": {
        "username": "user",
        "password": "1"
    }
}

# Pydantic model for login
class Login(BaseModel):
    username: str
    password: str

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(login: Login):
    user = users_db.get(login.username)
    if not user or user['password'] != login.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"message": "Login successful for user: {}".format(login.username)}