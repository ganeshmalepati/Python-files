a=56
b="56"
c=int(b)

print(a)
print(b)
print(c)

print(a==b)
print(a==c)
print(b==c)

print(type(a))    #checking the type of varible 
print(type(b))
print(type(c))

n=input("Enter the your age")
print("My age is :", n)

Give=input("Enter a num: ")
Given=input("Enter another num: ")
print("Sum of the two num: ", int(Give)+int(Given)) 
#Here the provided input is always as a string so when we enter a num it takes as a string and it will concatenate the string instead of 
#adding the two num. so we have to type cast the num into int

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("Average of two numbers", (a+b)//2)

Mystr=input("Enter a string")
print(Mystr[2:26:5])  #Slicing concept in String include strt point and exculde the last point [2:9] 2 included and 9 excluded it wil go upto 6.
