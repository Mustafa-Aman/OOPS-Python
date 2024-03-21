myDict={
"Fast": "To do something quickly",
"Mustafa": "Programmer",
"Marks": "[1,3,66]",
 "anotherdict":{'programmer':'Mustafa'} #this is how you can make nasly dictinory

}
print(myDict['Fast'])
print(myDict['Mustafa'])
print(myDict['Marks'])
print(myDict['anotherdict']['programmer'])

# # there is a gap of methodes in dictionary with ihavent done 


# # now starting set program
a={1,4,7,8,9}
print(type(a))
print(a)
# this is not the way you can make a emty set
a={}
print(type(a))

# # this is how you can make a emty set on while using set function
b = set()
print(type(b))
b.add(4)
b.add(5)
# you cannot add an unhashable function like list&dict
print(b)

# ## the gap is for the method for set 



# # now we will start the practics set Imy

myDict={
"phanka":"Fan",
"Dabba":"Box",
"Saman":"Items"
}
# By adding this step of option the user will get the option of with word they wont to pick
print("Options are", myDict.keys())
a=input("Enter the Urdu Word\n")
# # From this statment we can get a error if there isnt any word prasent 
print("The meaning of your word is:", myDict[a])
# # But from this we wont get an error the user will see "none"
print("The meaning of your word is:", myDict.get(a))


# This is the second problem
num1=int(input("Enter Number 1\n"))
num2=int(input("Enter Number 2\n"))
num3=int(input("Enter Number 3\n"))
num4=int(input("Enter Number 4\n"))
num5=int(input("Enter Number 5\n"))

s={num1,num2,num3,num4,num5}

print(s)



# Here another problem
FavLang={}
a=input("Enter your Favorite language Mustafa\n")
b=input("Enter your Favorite language Khadija\n")
c=input("Enter your Favorite language Insiya\n")
FavLang['Mustafa']=a  
FavLang['Khadija']=b  
FavLang['Insiya']=c  
print(FavLang)