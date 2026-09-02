number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 > number2 and number1 > number3:
    print("Number 1 is greater than Number 2 and Number 3.")
elif number2 > number3 and number2 > number1:
    print("Number 2 is greater than Number 3 and Number 1.")
elif number3 > number1 and number3 > number2:
    print("Number 3 is greater than Number 1 and Number 2.")
else:
    print("Invalid input.")
if number1 < number2 and number1 < number3:
    print("Number 1 is less than Number 2 and Number 3.")
elif number2 < number3 and number2 < number1:
    print("Number 2 is less than Number 1 and Number 3.")
elif number3 < number1 and number3 < number2:
    print("Number 3 is less than Number 1 and Number 2.")
else:
    print("Invalid input.")