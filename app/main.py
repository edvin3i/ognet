from fastapi import FastAPI
from app.api.extinguisher import router as extinguisher_router
from app.db import Base
from app.db import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(extinguisher_router, prefix="/ognet", tags=["Огнетушители"])


@app.get("/")
def read_root():
    return {"message": "Extinguishers API is ready!"}