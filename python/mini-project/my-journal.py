import os
import json
from datetime import datetime

# File to store journal entries
JOURNAL_FILE = "journal_entries.txt"
# File to store user credentials
USER_FILE = "user.json"

# Function to load user data from user.json
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save user data to user.json
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file)

# Function to authenticate users
def user_login():
    print("\n--- User Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    users = load_users()
    if username in users and users[username] == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password. Please try again.\n")
        return False

# Function to create users
def user_create():
    # Check if user.json exists, if not, create it with a default user
    if not os.path.exists(USER_FILE):
        default_users = {"admin": "password123"}  # Default username and password
        save_users(default_users)
        print("\n--- User Create ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        users = load_users()
        if username in users and users[username] == password:
            print("Login successful!\n")
            return True
        else:
            print("Invalid username or password. Please try again.\n")
            return False

# Function to add a new journal entry
def add_entry():
    print("\n--- Add New Entry ---")
    title = input("Enter title: ")
    content = input("Write your entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Append the entry to the journal file
    with open(JOURNAL_FILE, "a") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Date: {timestamp}\n")
        file.write(f"Content: {content}\n")
        file.write("-" * 40 + "\n")
    print("Entry added successfully!\n")

# Function to view all journal entries
def view_entries():
    print("\n--- View Entries ---")
    if not os.path.exists(JOURNAL_FILE):
        print("No entries found. Start by adding a new entry.\n")
        return
    with open(JOURNAL_FILE, "r") as file:
        entries = file.read()
        print(entries if entries else "No entries found.\n")

# Function to search entries by keyword
def search_entries():
    print("\n--- Search Entries ---")
    if not os.path.exists(JOURNAL_FILE):
        print("No entries found to search.\n")
        return
    keyword = input("Enter keyword to search: ").lower()
    with open(JOURNAL_FILE, "r") as file:
        entries = file.read()

    matching_entries = [entry for entry in entries.split("-" * 40) if keyword in entry.lower()]

    if matching_entries:
        print("\n--- Matching Entries ---")
        for entry in matching_entries:
            print(entry)
            print("-" * 40)
    else:
        print("No matching entries found.\n")

# Main program loop
def main():
    while True:
        choice = input("Choose an option (1,2): ")
        if choice == "1": # login
            result = user_login()
        elif choice == "2": # create user
            result = user_create()
        else:
            print("Invalid choice. Please try again.\n")

        # Authenticate user
        if not user_login():
            return  # Exit if login fails

        while True:
            print("\n--- Journal Program ---")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Search Entries")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                add_entry()
            elif choice == "2":
                view_entries()
            elif choice == "3":
                search_entries()
            elif choice == "4":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()