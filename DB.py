import mysql.connector
#Connect to MySQL
db = mysql.connector.connect(host="localhost",user="root",passwd="", database="studentdb")
mycursor = db.cursor()
#Create Table
mycursor.execute( """
CREATE TABLE IF NOT EXISTS Student (
StudentID INT PRIMARY KEY,
Name VARCHAR(50),
Department VARCHAR(50)
)
""")
print("Student table created successfully!")
#CREATE - Insert a record
def insert_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sql = "INSERT INTO Student VALUES (%s, %s, %s)"
    val = (sid, name, dept)
    mycursor.execute(sql, val)
    db.commit()
    print("Student Inserted Successfully")
#READ - Display all records
def display_students():
    mycursor.execute("SELECT * FROM Student")
    for row in mycursor.fetchall():
        print(row)
#UPDATE - Modify a record
def update_student():
    sid = int(input("Enter Student ID: "))
    name = input("Enter New Name: ")
    dept = input("Enter Department: ")
    sql="""UPDATE Student SET Name = %s, Department = %s WHERE StudentID = %s"""
    mycursor.execute(sql,(name,dept,sid))
    db.commit()
    print("Record updated!" if mycursor.rowcount else "Student not found")
#DELETE - Remove a record
def delete_student():
    sid = int(input("Enter Student ID: "))
    sql = """DELETE FROM Student WHERE StudentID = %s"""
    mycursor.execute(sql,(sid,))
    db.commit()
    print("Record deleted!" if mycursor.rowcount else "Student not found!")
#Main menu
while True:
    print("\n1.Insert")
    print("\n2.Display")
    print("\n3.Update")
    print("\n4.Delete")
    print("\n5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insert_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    else:
        exit()
    mycursor.close()
    db.close()
    print("Database connection closed")
