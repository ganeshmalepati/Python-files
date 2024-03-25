# Dictonary in python
dict = {
    "gift": "Something special that is surprise",
    "this": "It is a keyword in C++ and Java",
    "myList": [21, 32, 45],
    "instagram": "A social media platform where you can share a pic",
    "Youtube": "A content sharing platform",
    "Ganesh": "How are you now?"
}

# Methods in dict 

print(dict["this"])   #We can directly access the key values using the stmt like this.
print(dict.items())   #It will give the entire items in a tuple format, dict_items([('gift', 'Something special that is surprise'), ('this', 'It is a keyword in C++ and Java'), ('myList', [21, 32, 45]), ('instagram', 'A social media platform where you can share a pic'), ('Youtube', 'A content sharing platform')])
dict.update({"Ganesh":"He is feeling well now", "myList": [31, 41, 51]})  # It will Update the values in the dict
for a, b in dict.items():   # Print the items in a key value format like "a" as a key and "b" as a value
    print(a, ":-", b)
print(dict.keys())       # It will print all the keys present in the dict 
print(dict.get("Hey"))   # If the key is not present in dict it will doesn't throwns an error rather it will displays "None" in the output


# Hindi to English Dictonary by using user input
oxford={
    "Chiku": "Knife",
    "BankHoliday": "Behen ki Lowde",
    "Lakdi": "Wood"
}
key=input("Enter the key: ")
if oxford.get(key)==None:
    print("Value not found in the dict")
else:
    print("The Value for the corresponding key is:", oxford.get(key))



