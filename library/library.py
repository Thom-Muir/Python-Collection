import csv
import os.path
from pathlib import Path

class Book:
    def __init__(self,title,author,year,isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

class Lib:
    def __init__(self, collection):
        self.collection = collection
        
    def add_book(self, newTitle, newAuthor, newYear, newIsbn):        
        newBook = Book(newTitle, newAuthor, newYear, newIsbn)
        self.collection.append(newBook)
        
    def view_books(self):
        for book in self.collection:
            print(f"{book.title} By: {book.author} ({book.year}) - ISBN: {book.isbn}")
            
    def search_books(self, query):
        print(f"Searching for {query}...\n")
        for book in self.collection:
            if book.title.lower() == query.lower():
                print(f"{book.title} By: {book.author} ({book.year}) - ISBN: {book.isbn}")
                return
            elif book.author.lower() == query.lower():
                print(f"{book.title} By: {book.author} ({book.year}) - ISBN: {book.isbn}")
                return
        print("No matches found")
                
        print("\n")
        
    def remove_books(self, title):
        print(f"Searching for {title}...\n")
        #match = False
        for book in self.collection:
            if book.title == title:
                self.collection.remove(book)
                print("Book removed successfully\n")
                #match = True
                return
        #if match == False:
        print("Title not found\n")        

    def load_from_csv(self, filename):
        filename = filename or "Library.csv"
        if Path(filename).is_file():
            print(f"{filename} detected \nReading...\n")
            with open(filename, "r") as libr:
                reader = csv.reader(libr)
                for row in reader:
                    if len(row) == 4:  # Check if the row has exactly 4 fields
                        title, author, year, isbn = row
                        self.add_book(title, author, year, isbn)
                    else:
                        print("Skipping malformed row:", row)
        else:
            print("No file detected! \n Creating new library file...")
            with open("Library.csv", "w") as libw:
                pass       

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as libw:
            writer = csv.writer(libw)
            for book in self.collection:
                writer.writerow([book.title, book.author, book.year, book.isbn])
        print(f"Library saved to '{filename}'.")


library = Lib([])

filename = input("Filename? (Press enter if default or to create new)")
library.load_from_csv(filename)
main = True    
while main == True:    
    menu = input("Welcome to the Library Management System! \n1. Add a Book \n2. View All Books \n3. Search for a Book \n4. Remove a Book \n5. Quit \n")
    if menu == "1":
        title = input ("Enter book title: ")
        author = input ("Enter author: ")
        year = input ("Enter year of publication: ")
        isbn = input ("Enter ISBN: ")
        library.add_book(title,author,year,isbn)
    elif menu == "2":
        library.view_books()
    elif menu == "3":
        query = input("Enter title or author to search:")
        library.search_books(query)
    elif menu == "4":
        remove = input("Enter the title of the book to remove:")
        library.remove_books(remove)
    elif menu == "5":
        print("Closing...\n")
        closing = input("Save changes? Y/N")
        if closing.lower() == "y":
            file = input("Save file as? (Default: Library.csv)")
            if file:
                library.save_to_csv(file)
            else:
                library.save_to_csv("Library.csv")
            print("Saving changes and exiting... Goodbye!")
            main = False
        elif closing.lower() == "n":
            print("Discarding changes and exiting... Goodbye!")
            main = False
        else:
            print("Invalid choice")
    else: 
        print("Invalid choice")
