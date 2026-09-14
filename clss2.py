list1 = [1,2,3,4,5]

print(list1)
print("1: Add element")
print("2: Remove an element")
print("3: Replace an element")
print("4: Sort the elements")
print("5: Exit")


while 1:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list1.append(int(input("Enter a number to add: ")))
        print(list1)
    elif choice == 2:
        list1.remove(int(input("Enter a number to remove: ")))
        print(list1)
    elif choice == 3:
        index = list1.index(int(input("Enter a number to replace: ")))
        list1[index] = int(input("Enter another number to add: "))
        print(list1)
    elif choice == 4:
        list1.sort()
        print(list1)
    else:
        break