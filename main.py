from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from router import file, product, user, article, blog_get, blog_post
from router.templates import templates
from exceptions import StoryException
import authentication
import models
from db.database import engine
import os
import time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}
app.include_router(file.router)
app.include_router(templates.router)
app.include_router(article.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(blog_post.router)
app.include_router(blog_get.router)

@app.get("/")
def root():
    return {"message": "FastAPI app is running on Vercel!"}


@app.exception_handler(StoryException)
async def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})
                                                  
models.Base.metadata.create_all(engine)

@app.middleware("http")
async def add_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["duration"] = str(time.time() - start)
    return response


origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="templates/static"), name="static")

app.mount("/files", StaticFiles(directory="files"), name="files")

@app.get("/test-static")
def test_static():
    return {"file_exists": os.path.exists("templates/static/style.css")}
