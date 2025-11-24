from fastapi import APIRouter, Query,Cookie,Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional, List
from router.custom_log import Log
router = APIRouter(
    prefix="/product",
    tags=["product"]
)

products = ['watch', 'laptop', 'mobile', 'tablet']

@router.post("/new")
def create_product(name: str = Form()):
   products.append(name)
   return products


@router.get("/all")
def get_all_products():
    Log("my Api","call to get all products")
    
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response
@router.get("/withheader")
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Query(...),
    test_cookie: Optional[str] = Cookie(None)
):
    if custom_header:
     response.headers["Custom-Header-Response"] = ",".join(custom_header)

    return{
        "data": products,
        "custom_header": custom_header,
        "test_cookie": test_cookie
    }

@router.get(
    "/{id}",
    responses={
        200: {
            "content": {
                "text/html": {
                    "example": "<div>product</div>"
                }
            },
            "description": "Return the HTML for a product"
        },
        404: {
            "content": {
                "text/plain": {
                    "example": "Product not available"
                }
            },
            "description": "Product not found message"
        }
    }
)
def get_product(id: int):

    # id validation
    if id < 0 or id >= len(products):
        return PlainTextResponse(
            status_code=404,
            content="Product not found",
            media_type="text/plain"
        )

    product = products[id]

    out = f"""
    <html>
    <head>
        <style>
            .product {{
                font-size: 20px;
                color: blue;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="product">Random {product}</div>
    </body>
    </html>
    """

    return HTMLResponse(content=out, media_type="text/html")
