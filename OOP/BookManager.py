import sys as s

class Books:
    def __init__(self, name, author, year, price, category):
        self.name = name
        self.author = author
        self.year = int(year)
        self.price = int(price)
        self.category = category

    def InfoCorrect(self):
        print("Book Name : {}\tAuthor Name : {}\tBook Year : {}\tBook Price : {}\tBook Category : {}".format(
            self.name, self.author, self.year, self.price, self.category))


def ShowMenu():
    print("\nChoose an Option\n1. Add Book\n2. View all books\n3. Search by author\n4. Search by category\n5. Upgrade book info\n6. Delete book\n7. View Book Price\n8. Exit")


def GetInfo():
    Name = input("Book Name: ").strip()
    Author = input("Book Author: ").strip()
    Year = input("Book Year: ").strip()
    Price = input("Book Price: ").strip()
    Category = input("Book Category: ").strip()

    if not all([Name, Author, Year, Price, Category]):
        print("Missing argument!")
        return None
    return Books(Name, Author, Year, Price, Category)


BookList = []

while True:
    try:
        ShowMenu()
        choice = int(input("Enter choice (1-8): "))

        if choice == 1:
            book = GetInfo()
            if book:
                BookList.append(book)
                print(f"{book.name} added to the book list.")

        elif choice == 2:
            if not BookList:
                print("Book List is empty.")
                continue

            print("\nAll Books:")
            for z, i in enumerate(BookList, start=1):
                print(f"{z}. Name: {i.name}, Author: {i.author}, Year: {i.year}, Price: {i.price} TL, Category: {i.category}")

        elif choice == 3:
            if not BookList:
                print("Book List is empty.")
                continue

            author = input("Author Name: ").strip().lower()
            found = False
            for i in BookList:
                if i.author.lower() == author:
                    print(f"Name: {i.name}, Author: {i.author}, Price: {i.price} TL")
                    found = True
            if not found:
                print("Not found.")

        elif choice == 4:
            if not BookList:
                print("Book List is empty.")
                continue

            category = input("Category Name: ").strip().lower()
            found = False
            for i in BookList:
                if i.category.lower() == category:
                    print(f"Name: {i.name}, Author: {i.author}, Price: {i.price} TL")
                    found = True
            if not found:
                print("Not found.")

        elif choice == 5:
            if not BookList:
                print("Book list empty.")
                continue

            print("\nAll Books:")
            for z, i in enumerate(BookList, start=1):
                print(f"{z}. {i.name}, {i.author}, {i.year}, {i.price}, {i.category}")

            try:
                index = int(input("Enter the book number to update: ")) - 1
                if not (0 <= index < len(BookList)):
                    print("Invalid book number.")
                    continue

                field = input("Enter field to update (name, author, year, price, category): ").strip().lower()
                if field not in ["name", "author", "year", "price", "category"]:
                    print("Invalid field name.")
                    continue

                new_value = input("Enter new value: ").strip()
                if field in ["year", "price"] and not new_value.isdigit():
                    print("Invalid input. Please enter a number.")
                    continue

                setattr(BookList[index], field, int(new_value) if field in ["year", "price"] else new_value)
                print(f"Book {BookList[index].name} updated successfully.")

            except ValueError:
                print("Invalid input. Try again.")

        elif choice == 6:
            if not BookList:
                print("Book list empty.")
                continue

            print("\nAll Books:")
            for z, i in enumerate(BookList, start=1):
                print(f"{z}. {i.name}, {i.author}, {i.year}, {i.price}, {i.category}")

            try:
                index = int(input("Enter the book number to delete: ")) - 1
                if not (0 <= index < len(BookList)):
                    print("Invalid book number.")
                    continue

                print(f"Book {BookList[index].name} deleted successfully.")
                del BookList[index]

            except ValueError:
                print("Invalid input. Try again.")

        elif choice == 7:
            if not BookList:
                print("Book list empty.")
                continue

            book_name = input("Book name to learn price: ").strip().lower()
            found = False
            for i in BookList:
                if i.name.lower() == book_name:
                    print(f"Price: {i.price} TL")
                    found = True
                    break
            if not found:
                print("Book not found.")

        elif choice == 8:
            print("Goodbye!")
            break

        else:
            print("Unknown Number. Please enter a valid option.")

    except KeyboardInterrupt:
        s.exit("\nUser Logged Out.")
    except ValueError:
        print("Error, try again.")
