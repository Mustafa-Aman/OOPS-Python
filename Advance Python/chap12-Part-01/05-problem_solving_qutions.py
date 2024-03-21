# problem number 01
def readFiles(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFiles("1.txt")
readFiles("2.txt")
readFiles("3.txt")

# problem number 02
# write a program to print thired, fifth and seventh element from a list using enumerate function

l =[1,2,3,4,5,6,7,8,9,10]
for index, item in enumerate(l):
    if index==2 or index==4 or index==6:
        # print(index,item)
        print(f"The {index+1}th element is {item}")
  