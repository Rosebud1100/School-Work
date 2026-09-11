mylist = [1, 2, 3, 4, 5]

print(mylist)
print(mylist[4])

for i in mylist:
    print(mylist)
mylist.append(66)  # adding an element to the list
print(mylist)
mylist.remove(2)  # remove an element
print(mylist)
mylist.pop(0)  # removes last element in the list add number, and it will remove that index
print(mylist)
mylist.sort()
print(mylist)
newlist = mylist.copy()  # copy's old list to newlist
newlist.append(1001)
print(newlist)

newvalue = int(input("Enter a number: "))
if newvalue in mylist:
    print("element is in the list.")
else:
    print("element is not in the list.")

odd = [1,3,5,7,9]
even = [2,4,6,8,10]
for i in range (0, len(odd)):
    onel = int(odd [i] + int(even[i]))
    print (onel)