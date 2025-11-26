from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from exceptions import StoryException
from fastapi.middleware.cors import CORSMiddleware
from exceptions import StoryException
from router import file, product, user, article, blog_get, blog_post
from router.templates import templates
from fastapi.staticfiles  import StaticFiles
import authentication
from os import name
import models
from db.database import engine
import os
import time
app = FastAPI()


# Include routers
app.include_router(file.router)
app.include_router(templates.router)
app.include_router(article.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(blog_post.router)
app.include_router(blog_get.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI app is running on Vercel!"}

@app.exception_handler(StoryException)
async def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )

models.Base.metadata.create_all(engine)


@app.middleware("http")
async def add_Middleware(request:Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() -  start_time
    response.headers['duration'] = str(duration)
    return response

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.mount('/files', StaticFiles(directory="files"), name='files')
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/test-static")
def test_static():
    return {"file_exists": os.path.exists("templates/static/style.css")}

