from fastapi import FastAPI
from . import config
from tabel import users as users_tables
import repository.users as users_repo
import routes.users as users_routes

users_tables.Base.metadata.create_all(bind=config.engine)

app = FastAPI()

app.include_router(users_routes.router)

# @app.get("/")
# async def roof():
#     return {"message": "Welcome to the FastAPI Authentication Service"}