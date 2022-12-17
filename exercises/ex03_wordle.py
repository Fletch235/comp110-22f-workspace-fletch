__author__ = "730613482"

def contains_char(search: str, char: str) -> bool:
    """this function searches a string for a char."""
    assert len(char) == 1
    i:int = 0
    while(i<len(search)):
        if(search[i]==char):
            return True
        i+=1
    return False

def emojified(guess: str, secret: str) -> str:
    """make a word guess into a string of emojis."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emoji_string: str = ""
    while(i<len(secret)):
        if(secret[i] == guess[i]):
            emoji_string += GREEN_BOX
        elif(contains_char(secret, guess[i])):
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        i+=1
    return emoji_string

def input_guess(length: int) -> str:
    """ensures that the guess is a certain length."""
    guess: str = input(f"Enter a {length} character word: ")
    while(True):
        if(len(guess)==length):
            return guess
        else:
            guess = input(f"That wasn't {length} chars! Try again: ")


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    guess_main: str = ""
    turn: int = 1
    win: bool = False

    while(turn <= 6 and not win):
        print(f"=== Turn {turn}/6 ===")
        guess_main = input_guess(len(secret_word))
        print(emojified(guess_main, secret_word))
        if(guess_main == secret_word):
            win = True
        else:
            turn+=1
    
    if(win):
        print(f"You won in {turn}/6 turns!")
    else:
        print(" X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
