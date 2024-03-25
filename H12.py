def FindString(s):
    i=0
    rev=""
    while(i<len(s)-1):
        x=s[i]+s[i+1]
        if x=="32":
            rev+=" "
        elif int(x) in range(65,91) or int(x) in range (97, 123):
            rev+=chr(int(x))
        elif i+2<len(s):
            x+=s[i+2]
            rev+=chr(int(x))
            i+=1
        i+2
    return rev

s=input("Enter a string")
temp=s[::-1]
print(f"Reserve of a String is {temp}")
FindString(s)



