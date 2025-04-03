from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import sqlite3
from datetime import datetime, timedelta
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

@router.post("/register")
def register(form: OAuth2PasswordRequestForm = Depends()):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users VALUES (?, ?)", (form.username, form.password))
        conn.commit()
    except:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"msg": "Registered successfully"}

@router.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (form.username, form.password))
    if not cur.fetchone():
        raise HTTPException(status_code=401, detail="Invalid credentials")
    payload = {
        "sub": form.username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token")
