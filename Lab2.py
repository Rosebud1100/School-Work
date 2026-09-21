def add():
    a = int(input("Enter a number: "))
    b = int(input("Enter number: "))
    c=a+b
    print(c)
def subtract():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c=a-b
    print(c)
def multiply():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c=a*b
    print(c)
def divide():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c=a/b
    print(c)

while 1:
    choice = int(input("Enter a choice: "))
    if choice == 1:
        add()
    if choice === 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    else:
        exit()

