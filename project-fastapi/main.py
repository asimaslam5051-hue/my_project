from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional
from router import file
from router import user
from router import article
from router import product
from router import blog_get
from router import authentication
from router import blog_post
from db.database import engine
import models
from exceptions import storyException
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.include_router(file.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello World!"}
@app.exception_handler(storyException)
def story_exception_handler(request: Request, exc: storyException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name},
    )
    #@app.exception_handler(HTTPException)
    #def custom_handler(request: Request, exc: storyException):
        #return PlainTextResponse(str(exc), status_code=400)
        
models.Base.metadata.create_all(bind=engine)

origin =["http://localhost:300"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/files',StaticFiles(directory='files'),name = 'files')
