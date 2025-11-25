from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.responses  import HTMLResponse
from fastapi.responses import Response
router = APIRouter(
    prefix = 'template',
    tag =['template']


)

template =Jinja2Templates(directory='templates')
@router.get("/products/{id}",responses= HTMLResponse)
def get_pproduct(id:str,resposes:Response):
    return template.TemplateResponse
    "product.html",
    {
        "request":request
    }