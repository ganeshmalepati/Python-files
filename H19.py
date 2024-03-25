m1=int(input("Enter your marks for sub1: "))
m2=int(input("Enter your marks for sub2: "))
m3=int(input("Enter your marks for sub3: "))
overall=(m1+m2+m3)/3
if overall>=40:
    if m1 >= 33 and m2 >= 33 and m3 >= 33:
        print("You have passed the exam")
    else:
        print("You have failed the exam due to some subjects")
else:
    print("You have not passed the exam due to overall score")

#<section id="fa-bookmark"><i class="fa-solid fa-bookmark fa-rotate-270" style="color: #74C0FC;"></i></section>