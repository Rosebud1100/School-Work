number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
operator = input("Enter operator: ")

if operator == "+":
    print (number1 + number2)
elif operator == "-":
    print (number1 - number2)
elif operator == "*":
    print (number1 * number2)
elif operator == "/":
    print (number1 / number2)
else:
    print ("Invalid operator.")

