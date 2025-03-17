class Library:
    def __init__(self, book_name=None):
        self.book_name = book_name

    def adding_book(self):
        if self.book_name:
            with open("library.txt", "a", encoding="utf-8") as file:
                file.write(self.book_name + "\n")  # Add each book on a new line

    def getting_book(self):
        book_to_get = input("Which book do you want to get? ")
        found = False
        with open("library.txt", "r", encoding="utf-8") as file:
            books = file.readlines()

        # Check the books
        with open("library.txt", "w", encoding="utf-8") as file:
            for book in books:
                if book.strip() != book_to_get:  # If the book is found, it won't be removed
                    file.write(book)
                else:
                    found = True

        if found:
            print(f"Successfully got the book: {book_to_get}")
        else:
            print(f"Sorry, {book_to_get} is not available in the library.")

    def looking_book(self):
        print("\nCurrent Book List in Library:")
        with open("library.txt", "r", encoding="utf-8") as file:
            books = file.readlines()
            if books:
                for i, book in enumerate(books, start=1):
                    print(f"{i}. {book.strip()}")
            else:
                print("No books available.")


def display_menu():
    print("\nLibrary Menu:")
    print("Press 1 to add a book")
    print("Press 2 to get a book")
    print("Press 3 to look at the book list")
    print("Press 4 to exit")


# Create the file and add a welcome message if not exists
try:
    with open("library.txt", "x") as file:  # Only create the file if it doesn't exist
        file.write("                      WELCOME TO MY LIBRARY\n")
except FileExistsError:
    pass

try:
    while True:
        display_menu()

        while True:
            try:
                choice = int(input("Press a number button: "))
                if choice not in [1, 2, 3, 4]:
                    raise ValueError("Invalid input. Please enter a number between 1 and 4.")
            except ValueError as e:
                print(e)
            else:
                if choice == 1:
                    book_name = input("Please type the book name: ")
                    book = Library(book_name)
                    book.adding_book()
                    print(f"Book '{book_name}' added to the library.")
                elif choice == 2:
                    book = Library()
                    book.getting_book()
                elif choice == 3:
                    book = Library()
                    book.looking_book()
                elif choice == 4:
                    print("Exiting the program. Have a great day!")
                    break
                break
        if choice == 4:
            break

except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting gracefully...")
