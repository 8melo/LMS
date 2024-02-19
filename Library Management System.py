class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Reset file pointer to the beginning
        books = self.file.readlines()
        if books:
            print("*** List of Books ***")
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")
        else:
            print("No books found.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        books = self.file.readlines()
        self.file.seek(0)  # Reset file pointer to the beginning
        new_books = []
        removed = False
        for book in books:
            if title not in book:
                new_books.append(book)
            else:
                removed = True
        if removed:
            self.file.truncate(0)  # Clear the contents of the file
            for book in new_books:
                self.file.write(book)
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found.")


# Create an object named "lib" with "Library" class
lib = Library()

# Menu system
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        del lib  # Call destructor explicitly
        break
    else:
        print("Invalid choice. Please enter a valid option.")
