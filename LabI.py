
while 1:
    print ("1 Area of a rectangle: ")
    print ("2 Volume of a cube: ")
    print ("3 Area of a circle: ")
    print ("4 Circumference of a circle: ")
    print ("5 Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        exit()
    pi = 3.14
    if choice == 1:
        a = int(input("Enter the length: "))
        b = int(input("Enter the width: "))
        print ("The area of the rectangle: ", a*b)
    elif choice == 2:
        c = int(input("Enter the length: "))
        d = int(input("Enter the width: "))
        e = int(input("Enter the height: "))
        print ("The volume of the cube: ", c*e*d)
    elif choice == 3:
        f = int(input("Enter the radius: "))
        print ("The area of the circle: ", pi*f*f)
    elif choice == 4:
        g = int(input("Enter the radius: "))
        print ("The circumference of the circle: ", 2*pi*g)
    else:
        print ("Invalid input")

