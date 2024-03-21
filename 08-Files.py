f=open('sample.txt','a')
data=f.read()
print(data)
f.close()


f=open('sample.txt')

data=f.readline()
print(data)

data=f.readline()
print(data)

data=f.readline()
print(data)

data=f.readline()
print(data)

f.close()

f=open('another.txt','a')
f.write("Add this program  ")
f.close()

f=open('another.txt','w')
f.write("Add this sentance to the File  ")
f.close()

with open ('another.txt','r')as f:
    a=f.read()
with open ('another.txt','w')as f:
   a=f.write("me")
print(a)


# Practice set

f= open('poem.txt')
t=f.read()
if 'twinkle' in t :
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close
 
#  second problem

def game():
    return 9842

score = game()
with open ("hiscore.txt") as f:
    hiScoreStr = f.read()

if hiScoreStr=='':
    with open("hiscore.txt","w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score:
    with open("hiscore.txt","w") as f:
        f.write(str(score))


# TABLES
# ----------------------------
# problem 4

with open("sample.txt") as f:
    content =f.read()

content = content.replace("donkey","$$^%#")


with open("sample.txt",'w') as f:
        f.write(content)

# problem 5 ( This is how u can block or replace peoples harsh comments)

words =["donkey","pagal","mote"]

with open("sample.txt") as f:
    content =f.read()
for words in words:
  content = content.replace(words,"$$^%#")
with open("sample.txt",'w') as f:
        f.write(content)
        
# problem 6

with open ("log-file.txt")as f:
    content =  f.read()
if "Python" in content:
   print("Yes python is present")
else:
    print("NO python is not present")

# problem 7

content= True
i=1
with open ("log-file.txt")as f:
    while content:
        content =  f.readline()
        if "Python" in content:
             print(content)
             print(f"Yes python is present on line number {i}")
        i+=1

# problem 8


oldname= "renamed_by_python.txt"
newname="sample2.txt"
with open(oldname)as f:
    content=f.read
with open(newname,"w")as f:
    content=f.write

# END 