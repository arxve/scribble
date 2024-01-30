# Function to display the menu options for the user to interact with
def display_menu():
    print("1. Add a note")
    print("2. View notes")
    print("3. Quit")

# Function to add a note to the notes.txt file
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added successfully!")

# Function to view notes from the notes.txt file
def view_notes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            if notes:
                print("Your notes:")
                for note in notes:
                    print("- " + note.strip())
            else:
                print("No notes available.")
    except FileNotFoundError:
        print("No notes available.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
