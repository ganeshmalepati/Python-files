names = {
    "Person_1":"Ganesh Malepati",
    "Person_2":"Sai Pallavi",
    "Person_3":"Kulayamma",
    "a": 200,
    "b": 35,
    "c": 45,
    0:"Ramana"
}

# Here Person_1, Person_2, Person_3 and so on are Keys...
# Ganesh Malepati, Sai Pallavi and so on are values 
# Both of this combination is called items
# If you want to access only values write .values(), 
# for only keys .keys(), 
# for both .items()

names["d"] = "Good Morning"
names["Person_3"] = "Malepati Kulayamma" # For updating the dict values

print(names.values(), type(names), end="\n")
# print(type(names))
print(names.copy())
print(names.get("Person_3"))
print(names.get("a"))
print(names.get(0))
print(names.update({"a":100}))
print(names.values())


for i in names.values():
    print(i)
for i in names.keys():
    print(i)
for i in names.items():
    print(i)

for k, v in names.items():
    print(k ,":", v)


