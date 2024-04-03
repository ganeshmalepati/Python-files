#String Format This fomrat is used to print a string in formatted matter
name=input()
age=input()
print("Hey my name is", name, "My age is ", age)
print("Hey my name is {} and my age is {}".format(name, age)) #Here format method is used at the end using . and including the name and age
print(f"Hey bob my name is {name} and my age is {age}") #Here the formating is done and f is placed in front of the printing string
