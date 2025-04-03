from fastapi import APIRouter, HTTPException, Depends
import string, random
from app.database import get_db
from app.auth import get_current_user
from fastapi.responses import RedirectResponse

router = APIRouter(tags=["URL Shortener"])

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@router.post("/shorten")
def shorten_url(original: str, user: str = Depends(get_current_user)):
    short = generate_short_url()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO urls (short, original, owner) VALUES (?, ?, ?)", (short, original, user))
    conn.commit()
    return {"short_url": f"http://localhost:8000/{short}"}

@router.get("/{short}")
def redirect(short: str):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT original FROM urls WHERE short=?", (short,))
    row = cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(row[0])
