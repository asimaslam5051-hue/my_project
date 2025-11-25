from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/templates",
    tags=["templates"]
)

template = Jinja2Templates(directory="templates")  

@router.get("/products/{id}", response_class=HTMLResponse)
def get_product(id: str, request: Request):
    return template.TemplateResponse(
        "product.html", 
        {"request": request, "id": id}
    )

