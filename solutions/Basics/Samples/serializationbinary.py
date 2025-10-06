import pickle

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

def serialize(filename, customers):
    """Serialize the list of customers and save it to a file."""
    with open(filename, 'wb') as file:  # 'wb' for writing in binary mode
        pickle.dump(customers, file)
    print(f"Customers saved to {filename}.")

def deserialize(filename):
    """Deserialize the list of customers from a file."""
    try:
        with open(filename, 'rb') as file:  # 'rb' for reading in binary mode
            customers = pickle.load(file)
        print(f"Customers loaded from {filename}:")
        for customer in customers:
            print(customer)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    customers = [
        Customer("Chitra Pathak", "765-456-798"),
        Customer("Amit Patil", "124-765-8794"),
        Customer("Rajashree Bhor", "555-876-6098")
    ]

    filename = 'customers.pkl'
    
    # Save the contacts to a file
    serialize(filename, customers)

    # Load the contacts from the file
    deserialize(filename)
