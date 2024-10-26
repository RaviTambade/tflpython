import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

def save_contacts(filename, contacts):
    """Serialize the list of contacts and save it to a file."""
    with open(filename, 'wb') as file:  # 'wb' for writing in binary mode
        pickle.dump(contacts, file)
    print(f"Contacts saved to {filename}.")

def load_contacts(filename):
    """Deserialize the list of contacts from a file."""
    try:
        with open(filename, 'rb') as file:  # 'rb' for reading in binary mode
            contacts = pickle.load(file)
        print(f"Contacts loaded from {filename}:")
        for contact in contacts:
            print(contact)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    contacts = [
        Contact("Alice", "123-456-7890"),
        Contact("Bob", "098-765-4321"),
        Contact("Charlie", "555-555-5555")
    ]

    filename = 'contacts.pkl'
    
    # Save the contacts to a file
    save_contacts(filename, contacts)

    # Load the contacts from the file
    load_contacts(filename)
