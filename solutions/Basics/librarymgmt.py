

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.checked_out_books = []

    def checkout_book(self, book):
        if not book.is_checked_out:
            book.is_checked_out = True
            self.checked_out_books.append(book)
            print(f"{self.name} checked out '{book.title}'.")
        else:
            print(f"'{book.title}' is already checked out.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.is_checked_out = False
            self.checked_out_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' checked out.")

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: '{book.title}'.")

    def add_user(self, user):
        self.users.append(user)
        print(f"Added user: {user.name}.")

    def list_books(self):
        print("Available books:")
        for book in self.books:
            if not book.is_checked_out:
                print(book)

    def list_users(self):
        print("Registered users:")
        for user in self.users:
            print(user)

# Example usage
if __name__ == "__main__":
    library = Library()

    # Create some books
    book1 = Book("Let us C", "Yashwant Kanetkar", "123456789")
    book2 = Book("Wings of Fire", "Dr. A.P.J. Kalam", "987654321")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Create users
    user1 = User("Yash", 1)
    user2 = User("Disha", 2)

    # Add users to the library
    library.add_user(user1)
    library.add_user(user2)

    # List available books
    library.list_books()

    # Users checking out and returning books
    user1.checkout_book(book1)
    user2.checkout_book(book1)  # Should show that the book is already checked out
    user1.return_book(book1)
    user2.checkout_book(book1)  # Now it should succeed

    # List available books again
    library.list_books()