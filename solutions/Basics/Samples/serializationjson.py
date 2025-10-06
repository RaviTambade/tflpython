# JSON for serialization and deserialization,
# making it easy to store and retrieve data in a human-readable format

import json

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        """Convert the customer to a dictionary for JSON serialization."""
        return {"name": self.name, "phone": self.phone}

    @staticmethod
    def from_dict(data):
        """Create a Customer instance from a dictionary."""
        return Customer(data['name'], data['phone'])

def serialize(filename, customers):
    """Serialize the list of customers and save it to a JSON file."""
    with open(filename, 'w') as file:  # Open in write mode
        json_customers = [customer.to_dict() for customer in customers]
        json.dump(json_customers, file, indent=4)
    print(f"Customers saved to {filename}.")

def deserialize(filename):
    """Deserialize the list of customer from a JSON file."""
    try:
        with open(filename, 'r') as file:  # Open in read mode
            json_customers = json.load(file)
            customers = [Customer.from_dict(customer) for customer in json_customers]
        print(f"Customer loaded from {filename}:")
        for customer in customers:
            print(customer.name, customer.phone)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {filename}.")

# Example usage
if __name__ == "__main__":

    customers = [
        Customer("Shivkumar", "654-456-7890"),
        Customer("Sameer", "876-765-4321"),
        Customer("Manoj", "987-234-9867")
    ]

    filename = 'customers.json'
    
    # Save the customers to a JSON file
    serialize(filename, customers)

    # Load the customers from the JSON file
    deserialize(filename)
