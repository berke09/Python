import os
import datetime
import sys
import time

file = "Notebook.txt"  # The file that will be used


def Load_Notes():  # The reason we use Load_Notes is to convert the file to a list for easier manipulation.
    if os.path.exists(file):
        with open(file, "r") as f:
            return f.readlines()
    return []


def Save_Notes(Notes):
    with open(file, "w") as f:
        f.writelines(Notes)


def See_Notes(Notes):
    if not Notes:
        print("Notebook is empty")
    else:
        print("\nYour Notes:")
        for x, y in enumerate(Notes, 1):  # We start from 1 and print the notes line by line.
            print(f"{x}. {y.strip()}")  # We strip the whitespace at the beginning and end of each note.
    print("\n")


def Add_Notes(Notes):
    new_note = input("Write your note:")
    Notes.append(new_note + "\n")  # Since Notes is a list, we can append the new note directly.
    Save_Notes(Notes)


def Delete_Notes(Notes):
    if not Notes:
        print("Notebook is empty")
    else:
        See_Notes(Notes)
    try:
        note_index = int(input("\nPlease pick a note number to delete:")) - 1
        if 0 <= note_index < len(Notes):
            deleted_note = Notes.pop(note_index)
            time.sleep(0.5)
            print(f"Note '{deleted_note.strip()}' has been deleted.")
            Save_Notes(Notes)
        else:
            print("Invalid Number")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


def main():
    print("NOTEBOOK".center(150))
    while True:
        try:
            Notes = Load_Notes()
            print("1: See notes\n2: Add notes\n3: Delete notes\n4: Exit")
            Choose = input("\nPlease pick a number:")  # We receive the choice as a string.

            if Choose == "1":  # To see notes
                See_Notes(Notes)
            elif Choose == "2":  # To add notes
                Add_Notes(Notes)
            elif Choose == "3":  # To delete notes
                Delete_Notes(Notes)
            elif Choose == "4":  # To exit
                print("Logging out...")
                time.sleep(0.5)
                break
            else:
                print("Invalid choice, please try again.")
        except KeyboardInterrupt:
            print("\nStopped by user. Logging out...")
            sys.exit()


if __name__ == "__main__":
    main()
