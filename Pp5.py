for i in range(1, 3):
    print(i * 3)

age = 20
while age > 18:
    print(age)
    age = age - 1

while 1:
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiply")
    print("4 Division")
    print("5 Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        exit()

    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if choice == 1:
        print("The sum of",a, "and", b, "is: ", a + b)
    elif choice == 2:
        print("The difference of ", a, "and", b, "is: ", a - b)
    elif choice == 3:
        print("The product of ", a, "and", b, "is: ", a * b)
    elif choice == 4:
        print("The quotient of ", a, "and", b, "is: ", a // b)
