#Menu driven program for add, del, replace
myCourse = {}
i=1
while 1:
    print("1. Add Course")
    print("2. Remove Course")
    print("3. Replace Course")
    print("4. Print courses")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        course_name = input("Enter your course: ")
        myCourse.update({"c"+str(i):course_name})
        i=i+1

    elif choice == 2:
        del myCourse[input("Enter the course you want to delete: ")]

    elif choice == 3:
        myCourse.pop(input("Enter the course you want to delete: "))
        course_replace = input("Enter your course: ")
        myCourse.update({"c"+str(i):course_replace})

    elif choice == 4:
        print(myCourse)

    else:
        break
