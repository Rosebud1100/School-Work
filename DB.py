import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor = mydb.cursor()
#Create database
mycursor.execute("CREATE DATABASE StudentDB")
print("Database Created Successfully")
mydb.close()
#Connect to MySQL
db = mysql.connector.connect(host="localhost",user="root",passwd="")
#Create Table
cursor.execute("""CREATE """)