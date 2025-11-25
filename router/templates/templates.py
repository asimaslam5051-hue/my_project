from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.responses  import HTMLResponse
from fastapi.requests import Request
router = APIRouter(
    prefix = '/templates',
    tags =['templates']


)

template =Jinja2Templates(directory='templates')
@router.get("/products/{id}",response_class= HTMLResponse)
def get_pproduct(id:str,request:Request):
    return Jinja2Templates.TemplateResponse(
      "product.html",
      {
         "request": request,
         "id": id
      }
    )