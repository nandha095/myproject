from fastapi import FastAPI, Response
from blog.database import engine, Base
from blog.routers import auth, user, post
from blog.models import user as user_model, post as post_model
from blog.routers import auth, user
from fastapi.responses import JSONResponse
from blog import models
Base.metadata.create_all(bind=engine)  

app = FastAPI()

@app.get("/")
def Wlecome():
    return {"Greeting": "Wlecome to my blog"}


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)

    
@app.get("/cookie/")
def create_cookie():
    content = {"message": "Come to the dark side, we have cookies"}
    response = JSONResponse(content=content)
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return response


@app.get("/headers-and-object/")
def get_headers():
    content = {"message": "Hello World"}
    headers = {"X-Cat-Dog": "alone in the world", "Content-Language": "en-US"}
    return JSONResponse(content=content, headers=headers)






