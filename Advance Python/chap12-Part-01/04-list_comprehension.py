a=[22,34,56,7,88,66,4,9009,21]

b=[]
for item in a:
    if item%2==0:
        b.append(item)
print(b)

# the below coding is the shortcut of above coding 

b=[i for i in a if i%3==0]  
print(b)

# list comprehemsion and set comprehension the above is the example of list and the below one is for set

t=[1,2,2,3,1,4,3,1,2,4]
s={i for i in t}
print(s)