import pickle
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
    def add_new_user(self):
        self.ID = input("Enter new user ID: ")
        self.name = input("Enter new user name: ")
        self.password = input("Enter new user password: ")
        self.address = input("Enter new user address: ")
        self.phone = input("Enter new user phone: ")
        self.email = input("Enter new user email: ")
    def display_users(self):
        print(self.ID)
        print(self.name)
        print(self.password)
        print(self.address)
        print(self.phone)
        print(self.email)



while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        bk = Book()
        bk.add_new_books()
        file1 = open("books.dat", "ab")
        pickle.dump(bk, file1)
        file1.close()
    elif choice == 2:
        author = Author()
        author.add_new_author()
        file2 = open("authors.dat", "ab")
        pickle.dump(author, file2)
        file2.close()
        author.display_authors()
    elif choice == 3:
        user = User()
        user.add_new_user()
        file3 = open("user.dat", "ab")
        pickle.dump(user, file3)
        file3.close()
    elif choice == 4:
        file4 = open("books.dat", "rb")
        data = pickle.load(file4)
        print(data.title)
        print(data.ID)
        print(data.author)
        print(data.genre)
        file4.close()

        file5 = open("authors.dat", "rb")
        data1 = pickle.load(file5)
        print(data1.ID)
        print(data1.name)
        print(data1.phone)
        print(data1.email)
        print(data1.country)
        file5.close()

        file6 = open("user.dat", "rb")
        data2 = pickle.load(file6)
        print(data2.ID)
        print(data2.name)
        print(data2.password)
        print(data2.address)
        print(data2.phone)
        print(data2.email)
        file6.close()
    else:
        exit()
