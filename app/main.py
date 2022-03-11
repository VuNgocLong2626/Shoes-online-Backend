from fastapi import FastAPI

from app.db.database import engine
import app.db.tables as models
from app.api.routers import permission, name_services, user


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


app.include_router(permission.router)
app.include_router(name_services.router)
app.include_router(user.router)