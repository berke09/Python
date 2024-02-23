

# By Berke Çakır
import time
import os
def adding_book(book_number):
    for i in range(book_number):
        book_name = input("Type your book name:")
        book_name=book_name.title()
        book_name = book_name.strip()
        with open("Library.txt","r",encoding="utf-8") as file:
             A = file.read()
        if not book_name in A:
            with open("Library.txt","a",encoding="utf-8") as file:
                file.write(book_name+"\n")
        else:
            print("This book is already in your library...\n")


def getting_book():
    book = input("Type the book name that you want:")
    book = book.strip().title()
    global B
    B = list()
    with open("Library.txt","r",encoding="utf-8") as file:
        for i in file:
            i = i.strip()
            B.append(i)
    if book in B:
        print("We found the book that you want\n")
        B.remove(book)
        with open("Library.txt","w",encoding="utf-8") as file:
            for i in B:
                file.write(i+"\n")
    else :
        print("We could not found the book that you want\n")
        with open("Library.txt","r") as file:
            file_location = file.read()
            if len(file_location) == 0:
                print("No more books in your library...\n")
            else :
                print("You can look book list and then get another book...\n")
                while True:
                    try:
                        again = int(input("To searh another book press 1 :"))
                    except :
                        print("Please press only a number...")
                        continue
                    else:
                        if again == 1:
                            print("Loading...")
                            time.sleep(1)
                            getting_book()
                            break
                        else:
                            break

def looking_book_list():
    title = " Your Library Book list "
    title = title.center(75,"*")
    print("\n"+title)
    with open("Library.txt","r",encoding="utf-8") as file:
        for i in file:
            print(i,end="")

while True:
    try:
        new_file = int(input("Press 1 to delete the current file  Press 2 to continue with the same file again:"))
        if not 1 <= new_file <= 2:
            raise("Number error")
    except:
        print("Press only a number that one or two...\n")
        continue
    else:

        if new_file == 1:
            print("New file is loading...\n")
            time.sleep(0.5)
            with open("Library.txt","w") as file:
                pass
        else:
            if os.path.exists("Library.txt"):
                print("Same file is loading...\n")
                time.sleep(0.5)
                with open("Library.txt","a") as file:
                    pass
            else :
                print("There is no file new file is loading...")
                with open("Library.txt","w") as file:
                    pass
        while True:
            try:
                choosing = int(input("\n1- Adding Book\n2- Getting Book\n3- Look at Book List\n4- Exit\nYour Choosing:"))
                if not 1<= choosing <=4:
                    raise ("Number Error\n")
                else:
                    pass
            except:
                print("Please Press only a number from 1 to 4 ...\n")
                continue
            else:
                if choosing == 1:
                    while True:
                        try:
                            book_number = int(input("How many book will you add ?:"))
                            if book_number > 5 :
                                raise("Number Error\n")
                        except:
                            print("Book number should be a number and max 5...\n")
                        else:
                            adding_book(book_number)
                            break
                elif choosing == 2:
                    getting_book()
                elif choosing == 3:
                    looking_book_list()
                else:
                    while True:
                        try:
                            delete_or_not = int(input("To save file press 1\nTo delete file press 2\nYour choosing:"))
                            if not 1<= delete_or_not <=2 :
                                raise("Number Error...")
                        except:
                                print("Please press only 1 or 2...")
                                continue
                        else:
                            if delete_or_not == 1:
                                print("File saved...")
                                break
                            else:
                                os.remove("Library.txt")
                                print("File is removing...")
                                time.sleep(1)
                                break

                    print("Application is over...\n")
                    break

    break



