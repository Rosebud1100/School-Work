name = input("Enter your name: ")
grade1 = int(input("Enter your first grade: "))
grade2 = int(input("Enter your second grade: "))
grade3 = int(input("Enter you third grade: "))

total = (grade1 + grade2 + grade3)
percentile = (total/300)*100
print ("Percentile is: ", percentile)

if percentile <= 100 and percentile >= 90:
    print("Grade A")
elif percentile <= 89 and percentile >= 80:
    print("Grade B")
elif percentile <= 79 and percentile >= 70:
    print("Grade C")
elif percentile <= 69 and percentile >= 60:
    print("Grade D")
else:
    print("Grade F")