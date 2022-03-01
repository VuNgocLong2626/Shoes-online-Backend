from fastapi import FastAPI

from app.db.database import engine
import app.db.tables as models


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


@app.get("/test/")
def test():
    return {"Hello"}