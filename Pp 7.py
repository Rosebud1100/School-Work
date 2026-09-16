#List, Sets, Tupples self learn.

myDictionary = {"name" : "Emma", "name1" : "Lana"} #Dictionary
myDictionary.update({"name2" : "James", "name3" : "Melissa", "name4" : "Samuel", "name5" : "Samantha", "name6" : "Julia"}) #adding
del myDictionary["name3"] #removing
myDictionary["name4"] = "Tanner" #replacing

fullname = input("Enter your full name: ")
myDictionary.update({"name7" : fullname})
print(myDictionary)

