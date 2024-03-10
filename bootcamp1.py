# 1. Create a class named "Library"
class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")
#destructor method
    def __del__(self):
        if self.file:
            self.file.close()
# 2. Add the following methods to library
# a) list books
    def list_books(self): 
        self.file.seek(0)  
        books = self.file.read().splitlines()
        for book in books:
            info = book.split(',')
            print("Book Title: {}, Author: {}, Release Date: {}, Pages: {}".format(info[0], info[1], info[2], info[3]))
# b) add books
    def add_book(self):
        book_title = input("Book Title: ")
        author = input("Author: ")
        while True:
          try:
             release_date = input("Release Date: ")
             if int(release_date) > 2024:
              print("Error: The entered number cannot be greater than 2024.")
             else:
               break
          except ValueError:
              print("Invalid choice")
        page_no = input("Number of Pages: ")
        new_book = f"{book_title},{author},{release_date},{page_no}\n"
        self.file.write(new_book)
        print("Book added successfully.")   
# c) remove books
    def remove_book(self, book_title):
        self.file.seek(0)  
        books = self.file.read().splitlines()
        new_books = []
        for book in books:
            info = book.split(',')
            if info[0] != book_title:
                new_books.append(book)
        
        self.file.seek(0)
        self.file.truncate()  
        for book in new_books:
            self.file.write(book + '\n')
        
        print(f"{book_title} removed.")

# 3. Create an object named "lib" with "Library" class
lib = Library()

# 4. Create a menu to interact with the "lib" object
menu = """*** MENU ***
1) List Books
2) Add Book
3) Remove Book
"""

while True:
    print(menu)
    choice = input("Enter your choice 1-2-3 : ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        book_title = input("Enter the title of the book to remove: ")
        lib.remove_book(book_title)
    else:
        print("Invalid choice. Please enter 1-2-3.")

