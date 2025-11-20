from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from exceptions import StoryException
from router import file, product, user, article, blog_get, blog_post
from router import authentication
import models
from db.database import engine

app = FastAPI(title="My FastAPI App")

# Include routers
app.include_router(file.router)
app.include_router(article.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(blog_post.router)
app.include_router(blog_get.router)
@app.get("/hello")
def index():
    return {"message": "Hello world!"}

@app.exception_handler(StoryException)
async def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


models.Base.metadata.create_all(bind=engine)


origins = [
    os.getenv("FRONTEND_URL", "http://localhost:3000")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Serve static files from /public/files
# Move your local 'files/' folder to '/public/files' in the project root
app.mount("/files", StaticFiles(directory="public/files"), name="files")
