myQueue = []
def enqeue():
    myQueue.append(int(input("Enter a number: ")))
def deqeue():
    myQueue.pop(int(input("Enter a number: ")))
def display_queue():
    print(myQueue)

while 1:
    choice1 = int(input("Enter a choice: "))
    if choice1 == 1:
        enqeue()
    elif choice1 == 2:
        deqeue()
    elif choice1 == 3:
        display_queue()
    else:
        exit()
