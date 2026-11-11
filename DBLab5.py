import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="databaseSD")
mycursor = mydb.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS Student (StudentID INT PRIMARY KEY, Name VARCHAR(50), Department VARCHAR(50))""")
print("Student table created successfully!")
mycursor.execute("""CREATE TABLE IF NOT EXISTS Faculty (FacultyID INT PRIMARY KEY, Name VARCHAR(50), Department VARCHAR(50))""")
print("Faculty table created successfully!")
def insert_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter Name: ")
    major = input("Enter Major: ")
    courses = input("Enter Courses: ")
    department = input("Enter Department: ")
    sql = "INSERT INTO Student VALUES (%s, %s, %s)"
    val = (sid, name, major, courses, department)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Record inserted successfully!")
def insert_faculty():
    fid = int(input("Enter Faculty ID: "))
    name = input("Enter Faculty Name: ")
    dept = input("Enter Faculty Department: ")
    fac_courses = input("Enter Faculty Courses: ")
    fac_wages = int(input("Enter Faculty Wages: "))
    sql = "INSERT INTO Faculty VALUES (%s, %s, %s, %s)"
    val = (fid, name, dept, fac_courses, fac_wages)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Record inserted successfully!")
def display_faculty():
    cursor.execute("SELECT * FROM Faculty")
    for row in cursor.fetchall():
        print(row)
mydb.close()