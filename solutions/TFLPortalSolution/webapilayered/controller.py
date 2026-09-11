from fastapi import APIRouter
import service

router = APIRouter()

@router.get("/products")
def get_products():
    return service.get_products()

@router.get("/products/{product_id}")
def get_product(product_id: int):
    product = service.get_product(product_id)
    if not product:
        return {"message": "Product not found"}
    return product

@router.post("/products")
def create_product(product: dict):
    return service.create_product(product)

@router.put("/products/{product_id}")
def update_product(product_id: int, product_data: dict):
    product = service.update_product(product_id, product_data)
    if not product:
        return {"message": "Product not found"}
    return product

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    result = service.delete_product(product_id)
    if not result:
        return {"message": "Product not found"}
    return {"message": "Product deleted"}