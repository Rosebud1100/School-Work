import pickle
class Student:
    def __init__ (self):
        self.ID = ""
        self.name = ""
        self.department = ""
        self.advisor = None
    def create_new_student(self):
        self.ID = input("Enter your ID: ")
        self.name = input("Enter your name: ")
        self.department = input("Enter your department: ")
    def display_students(self):
        print(self.ID)
        print(self.name)
        print(self.department)


stu = Student()
stu.create_new_student()
stu.display_students()

file1 = open("myStudents.dat", "ab")
pickle.dump(stu, file1)
file1.close()
file2 = open("myStudents.dat", "rb")

while True:
    try:
        data = pickle.load(file2)
        print(data.name)
        print(data.ID)
        print(data.department)
    except(EOFError):
        break
file2.close()