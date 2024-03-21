import random

name=input("What is your name? " )
print("Good Luck! " , name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=random.choice(words)
print("Guess the character")
gussess=""
turns=12

while turns > 0:
    failed=0
    for char in word:
        if char in gussess:
            print(char,end =" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print=("You Win")
        # print("The wordsd is", word )d
        break
    print()
    guess=input("guess a character:")
    gussess += guess
    if guess not in word:
        turns -= 1
        print("Alphbet does not exit")
        print("You have", + turns ,"more guessess")
        if turns ==0 :
            print("You lose")


