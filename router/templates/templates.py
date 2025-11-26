from fastapi import APIRouter, Request, BackgroundTasks
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

from schemas import ProductBase
from router.custom_log import Log


router = APIRouter(
    prefix="/templates",
    tags=["templates"]
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))



@router.get("/products/{id}", response_class=HTMLResponse)
def get_product(id: str, request: Request):
    return templates.TemplateResponse(
        "product.html",
        {"request": request, "id": id}
    )

@router.get("/", response_class=HTMLResponse)
def get_all_products(request: Request):
    return templates.TemplateResponse(
        "product.html",
        {"request": request}
    )



@router.post("/products/{id}", response_class=HTMLResponse)
def create_product(
    id: str,
    product: ProductBase,
    request: Request,
    bt: BackgroundTasks
):
    bt.add_task(log_template_call, f"template read for product with id {id}")

    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id,
            "title": product.title,
            "description": product.description,
            "price": product.price
        }
    )



@router.delete("/products/{id}")
def delete_product(id: str):
    return {"message": f"Product {id} deleted"}



@router.put("/products/{id}", response_class=HTMLResponse)
def update_product(
    id: str,
    product: ProductBase,
    request: Request
):
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id,
            "title": product.title,
            "description": product.description,
            "price": product.price
        }
    )   
def log_template_call(message: str):
    Log("myapi", message)
