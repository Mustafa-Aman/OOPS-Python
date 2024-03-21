i = 0
while i<=5:
    print("Yes"+str(i))
    i=i+1
    
i=1
while i<=50:
    print(i)
    i=i+1

# This is done by whileloop 
fruits=['Banana','Apple','Mango','Grapes']
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1

# This is done by Forloop
fruits=['Banana','Apple','Mango','Grapes']

for item in fruits:
    print(item)
      
# Rangeloop
for i in range(0,8):
    print(i)

# for or else loops
for i in range(10):
    print(i)
else:
    print("This is the end")

# Second Method
for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("This is the end")

# continueloops
for i in range(10):
    if i==5:
     continue
    print(i)
     
# pass sections 


# Practic set (part one )
# wirteing a table by(forloop)
numb=int(input("Enter the number"))
for i in range(1,11):
#    There are two type of way we can run the code
#    First
   print(str(numb)+ "X"+str(i)+ "=" + str(i*numb))
#    Second
   print(f"{numb}X{i}={i*numb}")

#    problem NUMB(2)
l1=["Mustafa","Saad","Hatim","Sarah"]
for name in l1:
   if name.startswith("S"):
      print("Hello"+name)


# Problem NUMB(3)
# writing a program form which user can have prim numbers
num=int(input("Enter the Number:"))
prime= True

for i in range(2,num):
    if(num%i==0):
        prime= False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")

