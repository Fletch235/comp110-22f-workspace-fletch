__author__ = "730613482"

secret:str = "python"
guess:str = ""

working:bool=True
while(working):
    guess = input("What is your 6-letter guess?")
    if(len(guess)!=6):
        guess = input("That was not 6 letters! Try again:")
    else:
        if(secret==guess):
            print("Woo! You got it!")
            working = False
        else:
            print("Not quite. Play again soon!")
            working = False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i:int = 0
wordleString:str = ""
remainingLetters:str = guess
while(i<len(secret)):
    if(guess[i]==secret[i]):
        wordleString = wordleString + GREEN_BOX
    else:
        ii:int=0
        while(ii<len(secret)):
            if(guess[i]==secret[ii]):
                wordleString = wordleString + YELLOW_BOX
            else:
                wordleString = wordleString + WHITE_BOX
    i+=1
    
print(wordleString)