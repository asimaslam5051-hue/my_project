from typing import Optional, List
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

# Nested image model
class Image(BaseModel):
    url: str
    alt: str

# Blog model
class BlogModel(BaseModel):
    title: str
    content: str
    nb_comment: int
    published: bool
    tags: List[str] = []
    metadata: dict[str, str] = {'key': 'value'}
    image: Optional[Image] = None

# Create a new blog
@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog.model_dump(),  # ensures proper serialization
        'version': version
    }

# Create a comment on a blog
@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
        blog: BlogModel,
        id: int,
        comment_title: Optional[str] = Query(
            None,
            title="Title of the comment",
            description="Some description for comment_title",
            alias="commentTitle",
            deprecated=True
        ),
        content: str = Body(
            ..., 
            min_length=10,
            max_length=50,
            regex='^[a-z\s]*$'
        ),
        v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"]),
        comment_id: int = Path(..., gt=5, le=10),
        version: int = 1
    ): 
    return {
        'id': id,
        'blog': blog.model_dump(),
        'comment_id': comment_id,
        'content': content,
        'version': version,
        'comment_title': comment_title,
        'versions': v
    }
