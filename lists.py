mylist = [12,12,34,56,67,32,65,77,87,90]
print(mylist)

mylist.sort()
print(mylist)

mylist.append("Roman Reigns")
mylist.append("Brock Lesner")
print(mylist)

newlist=["Pikachu","Squirtle"]
mylist.extend(newlist)
print(mylist)

print(mylist.count(12))

print(mylist.pop(3))

mylist.remove(12)
print(mylist)

mylist.insert(7,"Ronaldo")
print(mylist)

print(mylist.index("Roman Reigns"))


