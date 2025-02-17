import os
import json
from datetime import datetime
from tabulate import tabulate  # Import tabulate for table formatting

# File paths
JOURNAL_FILE = "journal_entries.json"
USER_FILE = "user.json"


def load_users():
    """Load users from JSON file."""
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}


def save_users(users):
    """Save users to JSON file."""
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def load_journal():
    """Load journal entries from JSON file."""
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r") as file:
            return json.load(file)
    return []


def save_journal(entries):
    """Save journal entries to JSON file."""
    with open(JOURNAL_FILE, "w") as file:
        json.dump(entries, file, indent=4)


def user_login():
    """Handles user login."""
    print("\n--- User Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    users = load_users()

    if username in users and users[username] == password:
        print("Login successful!\n")
        return username
    else:
        print("Invalid username or password. Please try again.\n")
        return None


def user_create():
    """Handles user registration."""
    if not os.path.exists(USER_FILE):
        save_users({})

    print("\n--- Create User ---")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    users = load_users()

    if username in users:
        print("Username already exists. Try another one.\n")
        return None

    users[username] = password
    save_users(users)
    print("User created successfully!\n")
    return username


def add_entry(username):
    """Allows the user to add a journal entry."""
    print("\n--- Add New Entry ---")
    title = input("Enter title: ").strip()
    content = input("Write your entry: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entries = load_journal()
    entries.append({
        "username": username,
        "title": title,
        "content": content,
        "timestamp": timestamp
    })
    save_journal(entries)
    print("Entry added successfully!\n")


def view_entries(username):
    """Displays all journal entries in a table format."""
    print("\n--- Your Journal Entries ---")
    entries = load_journal()
    user_entries = [entry for entry in entries if entry["username"] == username]

    if not user_entries:
        print("No entries found. Start by adding a new entry.\n")
        return

    table_data = [[idx + 1, entry["title"], entry["timestamp"], entry["content"][:50] + "..."]
                  for idx, entry in enumerate(user_entries)]
    headers = ["Entry #", "Title", "Date", "Content Preview"]

    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def search_entries(username):
    """Allows users to search for journal entries."""
    print("\n--- Search Entries ---")
    keyword = input("Enter keyword to search: ").strip().lower()
    entries = load_journal()

    user_entries = [entry for entry in entries if entry["username"] == username and keyword in entry["content"].lower()]

    if user_entries:
        print("\n--- Matching Entries ---")
        table_data = [[idx + 1, entry["title"], entry["timestamp"], entry["content"][:50] + "..."]
                      for idx, entry in enumerate(user_entries)]
        headers = ["Entry #", "Title", "Date", "Content Preview"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    else:
        print("No matching entries found.\n")


def main():
    """Main function to run the journal program."""
    while True:
        print("\n--- Journal Program ---")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            username = user_login()
        elif choice == "2":
            username = user_create()
        elif choice == "3":
            print("Thank you for using My Journal app!")
            break
        else:
            print("Invalid choice. Please try again.\n")
            continue

        if not username:
            continue

        while True:
            print("\n--- Journal Menu ---")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Search Entries")
            print("4. Logout")
            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                add_entry(username)
            elif choice == "2":
                view_entries(username)
            elif choice == "3":
                search_entries(username)
            elif choice == "4":
                print("Logged out successfully!\n")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()