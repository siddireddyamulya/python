def guessNumber(startRange , endRange):
    if startRange  >  endRange:
        return True
    
    # middle of the Range
    mid=(startRange + endRange) // 2

    # Asking user this is actual Number

    print(f" Is the Number{mid} ? (Y/N) :", end="" )
    user=input().strip()

    # guessed correctly
    if user in ("Y","y"):
        print(f"Congratulation! Successfully guessed Number")
        return False
    
    # guessed incorrectly
    elif user in ("N","n"):
        print(f" Is the Number greater than {mid} ? (Y/N):", end="")
        user=input().strip()

        if user in ("Y","y"):
            return guessNumber(mid+1,endRange)
        elif user in ("N","n"):
            return guessNumber(startRange,mid-1)
        else:
            print("invaild input. please enter Y or N")
            return guessNumber(startRange,endRange)
    else:
        print("invaild input. please enter Y or N")
        return guessNumber(startRange,endRange)    
    

if __name__=="__main__":
    print("Number guessing Game in python")

        # Taking input from user for the guessing range
    startRange=int(input("enter start Range:"))
    endRange=int(input("enter end Range:"))

    print(f"Think of a number between {startRange} and {endRange}. I will try to guess it!")

    out = guessNumber(startRange, endRange)


    if out:
        print("Couldn't guess it. Are you sure you answered correctly?")



    
