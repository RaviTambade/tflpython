
"""
Simple REST API using python
Products crud api



"""



# pip install fastapi uvicorn
# uvicorn main:app --reload




from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000}
]


# GET - Read all products
@app.get("/api/products")
def get_products():
    return products


# GET - Read one product
@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Product not found"}


# POST - Create product
@app.post("/api/products")
def add_product(product: dict):
    products.append(product)
    return product


# PUT - Update product
@app.put("/api/products/{product_id}")
def update_product(product_id: int, updated_product: dict):
    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_product["name"]
            product["price"] = updated_product["price"]
            return product

    return {"message": "Product not found"}


# DELETE - Delete product
@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Product deleted"}

    return {"message": "Product not found"}