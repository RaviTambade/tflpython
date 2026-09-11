import repository

def get_products():
    return repository.get_all()

def get_product(product_id):
    return repository.get_by_id(product_id)

def create_product(product):
    return repository.add(product)

def update_product(product_id, product_data):
    return repository.update(product_id, product_data)

def delete_product(product_id):
    return repository.delete(product_id)