 # Note Taking App

This is a simple note taking app written in Python. It allows users to add and view notes.

## How to Use

To use the app, simply run the `main.py` file. You will be presented with a menu of options:

```
1. Add a note
2. View notes
3. Quit
```

Select the option you want by entering the corresponding number.

### Adding a Note

To add a note, select option 1. You will be prompted to enter your note. Once you have entered your note, press Enter. Your note will be saved to a file called `notes.txt`.

### Viewing Notes

To view your notes, select option 2. If you have any notes saved, they will be displayed in the console.

### Quitting the App

To quit the app, select option 3.

## Code Explanation

The code for this app is relatively simple. Let's go through it step by step:

### `display_menu()` Function

This function displays the menu of options to the user.

```python
def display_menu():
    print("1. Add a note")
    print("2. View notes")
    print("3. Quit")
```

### `add_note()` Function

This function allows the user to add a note. It prompts the user to enter a note, and then saves the note to a file called `notes.txt`.

```python
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added successfully!")
```

### `view_notes()` Function

This function allows the user to view their notes. It opens the `notes.txt` file and reads the contents. If there are any notes, they are displayed in the console.

```python
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
```

### `main()` Function

This function is the main entry point of the program. It displays the menu, gets the user's choice, and calls the appropriate function based on the choice.

```python
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
```
