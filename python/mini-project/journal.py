import os
from datetime import datetime

# File to store journal entries
JOURNAL_FILE = "journal_entries.txt"

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