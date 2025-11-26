from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from schemas import ProductBase
router = APIRouter(
    prefix="/templates",
    tags=["templates"]
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@router.get("/products/{id}", response_class=HTMLResponse)
def get_product(id: str, request: Request):
    return template.TemplateResponse(
        "product.html", 
        {"request": request, "id": id}
    )


@router.get("/", response_class=HTMLResponse)
def get_all_product( request: Request):
    return template.TemplateResponse(
        "product.html", 
        {"request": request}
    )

@router.post("/products/{id}", response_class=HTMLResponse)
def get_product(id: str,product: ProductBase, request: Request):
    return template.TemplateResponse(
        "product.html", 
        {"request": Request,
        "id": id,
        "title": product.title,
        "description":product.description,
        "price":product.price
        }
    )      


@router.delete("/product /{id}", response_class=HTMLResponse)
def delete_product(id: str,product: ProductBase):
    return "all"



@router.put("/product/", response_class=HTMLResponse)
def put_product(id: str,product: ProductBase):
    return   template.TemplateResponse(
        "product.html", 
        {"request": Request,
        "id": id,
        "title": product.title,
        "description":product.description,
        "price":product.price
        }
    )      
