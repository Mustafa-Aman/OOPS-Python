import random
# Snake water gun or Rock Paper Scissor 
def gameWin(comp , you ):
    if comp== you :
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you =='g':
            return True
    elif comp == 'w':
        if you=='g':
            return False
        elif you =='s':
            return True
    elif comp == 's':
        if you=='g':
            return False
        elif you =='w':
            return True
                  
print("Comp turn Ture: Snake(s) Water(w) or Gun(g)?")
randNO = random.randint(1,3)
print(randNO)
if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

you= input("Your Ture: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)
print(f"Computer chose {comp}")
print(f"Computer chose {you}")
if a== None:
    print("The game is Tie!")
elif a :
    print("You Win!")
else :
    print("You lose!")
