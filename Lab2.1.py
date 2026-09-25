#Develop a menu-driven Python program to manage employee payroll information using a Dictionary and functions.
myEmployee = {}

i=1
while True:
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Modify Employee")
    print("4. Display Employee")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        employee_name = input("Enter employee name: ")
        base = int(input("Enter base pay: "))
        allow = int(input("Enter allow pay: "))
        deduction = int(input("Enter deductions: "))
        tax = int(input("Enter tax: "))
        gross = base + allow
        net = gross - deduction - tax
        myEmployee.update({"c"+str(i):{"name":employee_name,"basic pay":base,"allowance":allow, "deductions": deduction, "taxes": tax, "grossPay": gross, "netPay": net}})
        i=i+1
    elif choice == 2:
        del myEmployee[input("Enter employee key: ")]
    elif choice == 3:
        emp=myEmployee[input("Enter employee key: ")]
        myEmployee[emp]["basic pay"]=int(input("Enter new base: "))
    elif choice == 4:
        print(myEmployee)
    else:
        exit()