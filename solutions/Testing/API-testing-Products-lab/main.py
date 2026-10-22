from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Transflower ProductCatalog API")

# Product request/response model
class Product(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)


# In-memory repository
products: dict[int, Product] = {}


# CREATE
@app.post("/api/products", response_model=Product,status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    if product.id in products:
        raise HTTPException(status_code=409,detail="Product already exists")

    products[product.id] = product
    return product

# READ ALL
@app.get("/api/products", response_model=list[Product])
def get_products():
    return list(products.values())


# READ ONE
@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = products.get(product_id)

    if product is None:
        raise HTTPException(status_code=404,detail="Product not found" )

    return product


# UPDATE
@app.put("/api/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    if product_id not in products:
        raise HTTPException(status_code=404,detail="Product not found" )

    if updated_product.id != product_id:
        raise HTTPException(status_code=400,detail="Product ID in URL must match body" )

    products[product_id] = updated_product
    return updated_product


# DELETE
@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in products:
        raise HTTPException(status_code=404,detail="Product not found")

    del products[product_id]

    return {"message": "Product deleted successfully"}