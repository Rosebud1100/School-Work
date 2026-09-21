myQueue = []
def pushbook():

def popbook():

def display():

while 1:
    choice = int(input("Enter your choice number: "))
    if choice == 1:
        pushbook()
    elif choice == 2:
        popbook()
    elif choice == 3:
        display()
    else:
        exit()