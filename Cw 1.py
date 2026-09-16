#Menu driven program for add, del, replace
while 1:
    myCourse = {}
    print("1. Add Course")
    print("2. Remove Course")
    print("3. Replace Course")
    print("4. Print courses")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        course1 = input("Enter your course: ")
        course2 = input("Enter your course: ")
        course3 = input("Enter your course: ")
        myCourse.update({"course1":course1, "course2":course2, "course3":course3})

