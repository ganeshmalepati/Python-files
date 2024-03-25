#Sets in Python and its methods 
#Sets are unordered and it doesn't have indexs, Duplicates are not allowed in sets

mySet={1, 2, 45, 65}
print(mySet)
print(len(mySet))  #Length of the set

mySet.add(31)      #Add the items to the set
print(mySet)

mySet.add("45")   #"45" stores as a string in the set
print(len(mySet))

print(mySet)
mySet.remove(45)  # Removes the item from the set
print(mySet)

mySet.pop()       # Removes the random item from the set
print(mySet)

mySet.clear()     # Clear the entire set
print(len(mySet))
