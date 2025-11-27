from fastapi import FastAPI, Response,APIRouter
from fastapi import status
from typing import Optional
from enum import Enum


router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

#@app.get("/blog/all")
#def get_all_blogs():
    #return {"message": "All blogs provided"}
@router.get("/all",

    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs",
    response_description="A list of available blogs"
)
@router.get("/all")
def get_all_blogs(page: int = 1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}

@router.get("/{id}/comments/{comment_id}",tags=["comments"])
def get_comment(id  : int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    simulates retrieving a  comment  of a blog post.
    - **id**: mandatory path parameter 
    - **comment_id**: mandatory path parameter 
    - **valid**: optional query parameter 
    - **username**: optional query parameter
    """
    return {"message": f"Blog id  {id}, comment id  {comment_id}, valid  {valid}, username  {username}"}


class BlogType(str , Enum):
    short = "short"
    howto = "howto"
    story = "story"

@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type is {type}"}

@router.get("/id/{id}",status_code=status.HTTP_200_OK)
def get_blog(id: int,response: Response):
   if id>5:
       response.status_code = status.HTTP_404_NOT_FOUND
       return{'error':f'Blog{id } not found'}
   else:
       response.status_code = status.HTTP_200_OK
       return {"message": f"Blog with id {id}"}
