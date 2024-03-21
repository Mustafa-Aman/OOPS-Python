while(True):
    print("Press q to quit")   
    a=input("Enter a number")

    if a== 'q':
        break

    try:
        a=int(a)
        if a>6:
            print("You entered a number greater then six")

    except Exception as e :
        print(f"Your input resulted in an error {e}")
        
print("Thanks for playing this game")