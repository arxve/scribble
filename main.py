import os

NOTES_FILE = "notes.txt" # Notes file name and extension

# Function to display the menu options for the user to interact with
def display_menu():
    print("\nNote App Menu:")
    print("1. Add a note")
    print("2. View notes")
    print("3. Clear all notes")
    print("4. Quit")

# Function to add a note to the notes.txt file
def add_note():
    note = input("Enter your note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    print("Note added successfully!")

# Function to view notes
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

# Function to clear notes
def clear_notes():
    try:
        os.remove(NOTES_FILE)
        print("\nAll notes cleared successfully!")
    except FileNotFoundError:
        print("\nNo notes available to clear.")

# Main function to run the program
def main():
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
