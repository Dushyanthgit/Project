# Library Management System in Python

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Copies Available: {self.copies}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def display_books(self):
        if self.books:
            print("\nAvailable Books:")
            for book in self.books:
                book.display_details()
        else:
            print("No books available in the library.")

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                book.copies -= 1
                print(f"You have borrowed '{book.title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"Thank you for returning '{book.title}'.")
                return
        print(f"Book '{title}' does not belong to this library.")


def main():
    library = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            new_book = Book(title, author, copies)
            library.add_book(new_book)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            library.lend_book(title)

        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)

        elif choice == '5':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
