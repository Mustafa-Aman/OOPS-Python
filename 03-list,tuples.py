# Creating a list by []
a=[1,2,3,6,7]
print(a)

# # Finding the place of any numb in the list 
print(a[3])

# # Changing the value of the numb
a[2]=55
print(a)

# # We can make list having diffrent value
c=[20, "Mustafa" , 9.0]
print(c)

# # now we are sorting the list out
l1=[3,8,9,21,15,4]
print(l1)
# l1.sort()
# l1.reverse()
l1.append(45)
l1.append(69)
l1.insert(1,39)
print(l1)

# Creating tuples using ()
t=(32,1212,2,131,2,33,2,444,2)
# t[0]=66 Therefore you can not change the value of tuple that is the magure diffrince between taple and list

print(t.count(2))
print(t.index(2))


# # practis set
# printing a fruit list problem numb1
f1=input("Enter Fruit Number 1")
f2=input("Enter Fruit Number 2")
f3=input("Enter Fruit Number 3")
f4=input("Enter Fruit Number 4")
myFruitList=[f1,f2,f3,f4]
print(myFruitList)

# printing marks of student problem 2
m1=int(input("Enter Marks For Student Number 1"))
m2=int(input("Enter Marks For Student Number 2"))
m3=int(input("Enter Marks For Student Number 3"))
m4=int(input("Enter Marks For Student Number 4"))
mylist=[m1,m2,m3,m4]
mylist.sort()
print(mylist)

# suming up the list numbers
a=[2,56,7,80]
print(sum(a))

# finding the 0s in the tuple
a=(0,8,0,9,8,0)
print(a.count(0))

