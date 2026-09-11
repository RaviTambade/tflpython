products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000}
]

def get_all():
    return products

def get_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

def add(product):
    products.append(product)
    return product

def update(product_id, product_data):
    product = get_by_id(product_id)
    if product:
        product["name"] = product_data["name"]
        product["price"] = product_data["price"]
    return product


def delete(product_id):
    product = get_by_id(product_id)
    if product:
        products.remove(product)
        return True
    return False