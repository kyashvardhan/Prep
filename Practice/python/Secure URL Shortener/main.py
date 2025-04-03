from fastapi import FastAPI
from app import routes, auth, database

app = FastAPI(title="🔗 Secure URL Shortener")

@app.on_event("startup")
def startup():
    database.init_db()

app.include_router(auth.router)
app.include_router(routes.router)
