a=45
if(a>3):
    print("The value of a is greater then 3")
elif(a>13):
    print("The value of a is greater then 13")
elif(a>15):
    print("The value of a is greater then 15")
else:
    print("The value of a is greater then 3 or 13")

# if-elif-else are three thing but if you start the program with "if" it becoms a leader
# you can write if saprate

a=22
if(a>30):
    print("Greater")
else:
    print("less")

# if-else qise
age=int(input("Enter your age"))
if age>18:
    print("Yes")
else:
    print("No")
    
# logical op

age=int(input("Enter your age:"))
if(age>34 and age<56):
    print("You can work with us")

else:
    print("You canot wrok with us")

    # there are 2 more thing "in" and "is"


# Doing a Practic set
numb1=int(input("Enter Number 1: "))
numb2=int(input("Enter Number 2: "))
numb3=int(input("Enter Number 3: "))
numb4=int(input("Enter Number 4: "))

if(numb1>numb4):
    f1=numb1
else:
    f1=numb4

if(numb2>numb3):
    f2=numb2
else:
    f2=numb3

if(f1>f2):
    print(str(f1)+"is greater")
else:
    print(str(f2)+"is greater")

# heres another problem yeheh
sub1=int(input("Enter First Subject Marks \n"))
sub2=int(input("Enter Second Subject Marks \n"))
sub3=int(input("Enter Third Subject Marks \n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You have fail this Exam because you have less marks then 33% in one of the subjects")
elif(sub1+sub2+sub3)/3<40:
    print("You have fail this Exam because you have less percentage then 44%")    
else:
    print("Congratulations you have pass this Exam")