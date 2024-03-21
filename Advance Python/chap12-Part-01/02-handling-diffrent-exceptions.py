while(True):

    print("Thankyou for using this code!")


    try:
        a= int(input("Enter a number: "))
        c=1/a
        print(c)

    # except Exception as e:
    #         print(e)

    except ValueError as e:
            print("Please Enter a valid value")

    except ZeroDivisionError as e:
            print("Make sure your are not dividing by zero ")

# print("Thankyou for using this code!")

# ValueError accures when there is something wrong in an Ingeter input