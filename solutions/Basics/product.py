class Product:
    def __init__(self, name, price, quantity):
        self.name = name        # Name of the product
        self.price = price      # Price of the product
        self.quantity = quantity # Quantity in stock

    def total_price(self):
        """Calculate total price for the quantity of the product."""
        return self.price * self.quantity

    def restock(self, amount):
        """Increase the quantity of the product."""
        self.quantity += amount
        print(f"Restocked {amount} units of {self.name}. New quantity: {self.quantity}")

    def sell(self, amount):
        """Sell a certain amount of the product."""
        if amount > self.quantity:
            print(f"Not enough {self.name} in stock to sell {amount} units.")
        else:
            self.quantity -= amount
            print(f"Sold {amount} units of {self.name}. Remaining quantity: {self.quantity}")

    # Provides a human-readable representation of the object for easy printing
    def __str__(self):
        """Return a string representation of the product."""
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

# Example usage
if __name__ == "__main__":
    product = Product("Gerbera", 35.33, 100)
    
    print(product)  # Output: Product: Laptop, Price: 999.99, Quantity: 10
    
    print(f"Total price of stock: ${product.total_price():.2f}")  # Output: Total price of stock: $9999.90
    
    product.sell(3)  # Output: Sold 3 units of Laptop. Remaining quantity: 7
    product.restock(5)  # Output: Restocked 5 units of Laptop. New quantity: 12
