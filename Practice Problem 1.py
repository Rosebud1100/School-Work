print("Enter your name: ")
name = input()
print("Enter your pay: ")
pay = int(input())
print("Enter you deductions: ")
deductions = int(input())

total = pay - deductions

print("Employee: ", name)
print("Total pay: ", total)