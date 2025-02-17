import os
import json
from datetime import datetime

# File to store journal entries
JOURNAL_FILE = "journal_entries.json"
# File to store user credentials
USER_FILE = "user.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            return json.load(file)
    return {}

def save_users(users):

    with open(USER_FILE, "w") as file:
        json.dump(users, file)

def load_journal():
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r") as file:
            return json.load(file)
    return []

def save_journal(entries):
    with open(JOURNAL_FILE, "w") as file:
        json.dump(entries, file, indent=4)

def user_login():
    print("\n--- User Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    users = load_users()
    if username in users and users[username] == password:
        print("Login successful!\n")
        return username
    else:
        print("Invalid username or password. Please try again.\n")
        return None

def user_create():
    if not os.path.exists(USER_FILE):
        save_users({})
    print("\n--- User Create ---")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users = load_users()
    if username in users:
        print("Username already taken.\n")
        return None
    users[username] = password
    save_users(users)
    print("User created successfully!\n")
    return username

def add_entry(username):
    print("\n--- Add New Entry ---")
    title = input("Enter title: ")
    content = input("Write your entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries = load_journal()
    entries.append({"username": username, "title": title, "content": content, "timestamp": timestamp})
    save_journal(entries)
    print("Entry added successfully!\n")

def view_entries(username):
    print("\n--- View Entries ---")
    entries = load_journal()
    user_entries = [entry for entry in entries if entry["username"] == username]
    if not user_entries:
        print("No entries found. Start by adding a new entry.\n")
        return
    for entry in user_entries:
        print(f"Title: {entry['title']}\nDate: {entry['timestamp']}\nContent: {entry['content']}\n" + "-" * 40)

def search_entries(username):
    print("\n--- Search Entries ---")
    entries = load_journal()
    keyword = input("Enter keyword to search: ").lower()
    user_entries = [entry for entry in entries if entry["username"] == username and keyword in entry["content"].lower()]
    if user_entries:
        print("\n--- Matching Entries ---")
        for entry in user_entries:
            print(f"Title: {entry['title']}\nDate: {entry['timestamp']}\nContent: {entry['content']}\n" + "-" * 40)
    else:
        print("No matching entries found.\n")

def main():
    while True:
        print("\n--- Journal Program ---")
        print("1. User Login")
        print("2. User Create")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
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
            print("\n--- Journal Program ---")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Search Entries")
            print("4. Logout")
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                add_entry(username)
            elif choice == "2":
                view_entries(username)
            elif choice == "3":
                search_entries(username)
            elif choice == "4":
                print("Logged out successfully!\n")
                print("Thank you for using My Journal app!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
