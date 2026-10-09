class Book:
    def __init__(self):
        self.ID = None
        self.title = None
        self.author = None
        self.genre = None
    def add_new_books(self):
        self.ID = input("Enter new book ID: ")
        self.title = input("Enter new book title: ")
        self.author = input("Enter new book author: ")
        self.genre = input("Enter new book genre: ")
    def display_books(self):
        print(self.ID)
        print(self.title)
        print(self.author)
        print(self.genre)
class Author:
    def __init__(self):
        self.ID = None
        self.name = None
        self.phone = None
        self.email = None
        self.country = None
    def add_new_author(self):
        self.ID = input("Enter new author ID: ")
        self.name = input("Enter authors name: ")
        self.phone = input("Enter authors phone: ")
        self.email = input("Enter authors email: ")
        self.country = input("Enter authors country: ")
    def display_authors(self):
        print(self.ID)
        print(self.name)
        print(self.phone)
        print(self.email)
        print(self.country)
class User:
    def __init__(self):
        self.ID = None
        self.name = None
        self.password = None
        self.address = None
        self.phone = None
        self.email = None
        self.books_borrowed = None
        self.book = None
    def add_new_user(self):
        self.ID = input("Enter new user ID: ")
        self.name = input("Enter new user name: ")
        self.password = input("Enter new user password: ")
        self.address = input("Enter new user address: ")
        self.phone = input("Enter new user phone: ")
        self.email = input("Enter new user email: ")
    def borrowed_book(self, books_borrowed):
        self.book = books_borrowed
    def display_users(self):
        print(self.ID)
        print(self.name)
        print(self.address)
        print(self.phone)
        print(self.email)
        print(self.book)

myBookList = []
myAuthorList = []
myUserList = []

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        bk = Book()
        bk.add_new_books()
        myBookList.append(bk)
        bk.display_books()
    elif choice == 2:
        author = Author()
        author.add_new_author()
        myAuthorList.append(author)
        author.display_authors()
    elif choice == 3:
        user = User()
        user.add_new_user()
        myUserList.append(user)
        get_book = input("Enter book ID:")
        for f in myBookList:
            if f.ID == get_book:
                user.borrowed_book(f)
        user.display_users()
    else:
        exit()
