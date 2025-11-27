from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from static import article, blog_get
import blog_post
from router import file, product, user
from router.templates import templates
from exceptions import StoryException
import authentication
import models
from db.database import engine
import os
import time
import html
from fastapi import WebSocket

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


@app.exception_handler(StoryException)
async def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418, 
        content={"detail": exc.name})


@app.get("/chat")
async def get_chat():
    return HTMLResponse(html)
@app.websocket("/ws")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            await websocket.send_text(f"You said: {data}")
        except:
            break

models.Base.metadata.create_all(bind=engine)


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
