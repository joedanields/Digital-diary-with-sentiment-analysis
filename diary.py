import os
from datetime import datetime
from textblob import TextBlob

DIARY_FILE = "diary.txt"
#defining functions
def load_entries():
    if not os.path.exists(DIARY_FILE):
        return []
    with open(DIARY_FILE, "r") as file:
        return [line.strip().split(",") for line in file.readlines()]

def save_entries(entries):
    with open(DIARY_FILE, "w") as file:
        for entry in entries:
            file.write(",".join(entry) + "\n")

def analyze_sentiment(entry):
    blob = TextBlob(entry)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

def add_entry(entries):
    entry_text = input("Write your journal entry: ")
    sentiment = analyze_sentiment(entry_text)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries.append([date, entry_text, sentiment])
    print(f"Entry added with sentiment: {sentiment}")
    
def view_entries(entries):
    if not entries:
        print("No entries found.")
        return
    for entry in entries:
        print(f"\nDate: {entry[0]}\nMood: {entry[2]}\nEntry: {entry[1]}")
    
def search_entries(entries):
    keyword = input("Enter a keyword to search: ")
    found_entries = [entry for entry in entries if keyword.lower() in entry[1].lower()]
    if not found_entries:
        print("No matching entries found.")
    else:
        for entry in found_entries:
            print(f"\nDate: {entry[0]}\nMood: {entry[2]}\nEntry: {entry[1]}")

def mood_summary(entries):
    positive = sum(1 for entry in entries if entry[2] == "Positive")
    negative = sum(1 for entry in entries if entry[2] == "Negative")
    neutral = sum(1 for entry in entries if entry[2] == "Neutral")
    total = len(entries)
    
    print("\nMood Summary:")
    print(f"Positive: {positive} ({(positive/total)*100:.2f}%)")
    print(f"Negative: {negative} ({(negative/total)*100:.2f}%)")
    print(f"Neutral: {neutral} ({(neutral/total)*100:.2f}%)")

def main():
    entries = load_entries()
    while True:
        print("\nDigital Diary Menu:")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entries")
        print("4. Mood Summary")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_entry(entries)
            save_entries(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            search_entries(entries)
        elif choice == "4":
            mood_summary(entries)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
