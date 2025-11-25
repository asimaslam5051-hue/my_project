from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.responses  import HTMLResponse
from fastapi.responses import Response
router = APIRouter(
    prefix = '/templates',
    tags =['templates']


)

template =Jinja2Templates(directory='templates')
@router.get("/products/{id}",response_class= HTMLResponse)
def get_pproduct(id:str,resposes:Response):
    return Jinja2Templates.TemplateResponse
    "product.html",
    {
        "request":request
    }