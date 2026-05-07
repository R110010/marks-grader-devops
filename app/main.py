from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import auth
from app.api.routes import grades
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(title="Marks Grader DevOps Project")
app.include_router(auth.router)
app.include_router(grades.router)
Instrumentator().instrument(app).expose(app)

@app.on_event("startup")
def startup():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database connected")
    except Exception as e:
        print("❌ Database connection failed:", e)

@app.get("/")
def root():
    return {"message": "Welcome to Marks Grader DevOps Project: Version 2"}
