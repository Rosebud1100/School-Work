#storage into text file
file1 = open("mytext.txt", "a")
file1.writelines (input("Enter your name:  "))
file1.writelines ("Hello World, ")
file1.writelines (" How are you?")
file1.close()

file2 = open("mytext.txt", "r")
for line in file2:
    print(line)
file2.close()
