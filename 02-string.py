story =  "once upone a time there was a programmer name Mustafa he was trying to learn python"

# String function
print(len(story))
print(story.endswith("python"))
print(story.count("a"))
print(story.capitalize())
print(story.find("Mustafa"))
print(story.replace("python","css"))


# # Here we are solving the practice problem
name = input("Enter your name\n")
print("Good Afternoon,"+name)

letter='''' Dear <[NAME]>,
I am happy to inform you that our company TECNATIC have selected you for the job 
Congratulations!!
Best Regards, 
Jon 
date:<[DATE]>
'''
name=input("Enter your name\n")
date=input("Enter date\n")
letter=letter.replace("<[NAME]>", name)
letter=letter.replace("<[DATE]>", date)
print(letter)

# HERE WE ARE APPLING DOUBLE SPACE PLANING 
st="Can you find the double space in   this line "
doubleSpace=st.find("  ")
print(doubleSpace)
# HERE WE ARE REPLACING DOUBLE SPACE BY SINGLE SPACE
st="Can you find the double space in   this line "
st=st.replace("   "," ")
print(st)


# HERE WE ARE MAKING A FORMATEED_LETTER
letter="Dear Harry, This python course is nice! Thanks! "
print(letter)

formatted_letter="Dear Harry,\n\t This python course is nice!\n Thanks!"
print(formatted_letter)