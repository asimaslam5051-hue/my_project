from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from exceptions import StoryException
from router import file, product, user, article, blog_get, blog_post
from router import authentication

import models
from db.database import engine

app = FastAPI()

# Include routers
app.include_router(file.router)
app.include_router(article.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(blog_post.router)
app.include_router(blog_get.router)

# Simple hello route
@app.get('/hello')
def index():
    return {'message': 'Hello world!'}

# Custom exception handler
@app.exception_handler(StoryException)
async def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )

# Create all database tables
models.Base.metadata.create_all(engine)

# CORS configuration
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

# Serve static files
app.mount('/files', StaticFiles(directory="files"), name='files')

