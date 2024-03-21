try:
    i=int(input("Enter a number: "))
    c=1/i
except Exception as e:
    print(f"Enter a proper number {e}")
else:
    print("We were successful")


# in here there is one more example of try-except-finally

try:
    i=int(input("Enter a number: "))
    c=1/i
except Exception as e:
    print(f"Enter a proper number {e}")
    exit()
finally:
    print("We were done")

# what ever you do in except you cant stop finally to stop printing
# global /local

list1 =[3,53,2,False,6.2,"Mustafa"]

index=0
for item in list1:
    print(item,index)
    index +=1

for index,item in enumerate(list1):
    print(item,index)
# add counter to an iterable and return it 