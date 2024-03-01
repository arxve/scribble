import os

NOTES_FILE = "notes.txt"

def display_menu():
    print("\nNote App Menu:")
    print("1. Add a note")
    print("2. View notes")
    print("3. Clear all notes")
    print("4. Quit")

def add_note():
    note = input("Enter your note: ").strip()
    if note:
        try:
            with open(NOTES_FILE, "a") as f:
                f.write(note + "\n")
            print("Note added successfully!")
        except IOError:
            print("Error: Unable to write to file.")
    else:
        print("Error: Note cannot be empty.")

def view_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            notes = f.readlines()
            if notes:
                print("\nYour notes:")
                for idx, note in enumerate(notes, start=1):
                    print(f"{idx}. {note.strip()}")
            else:
                print("\nNo notes available.")
    except FileNotFoundError:
        print("\nNo notes available.")

def clear_notes():
    try:
        os.remove(NOTES_FILE)
        print("\nAll notes cleared successfully!")
    except FileNotFoundError:
        print("\nNo notes available to clear.")
    except IOError:
        print("Error: Unable to clear notes.")

def main():
    if not os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, "w"):
                pass
        except IOError:
            print("Error: Unable to create notes file.")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            clear_notes()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
