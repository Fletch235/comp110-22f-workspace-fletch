__author__ = "730613482"

"""Create an adventure game."""

import random

points: int = 0
player: str = ""
orb: bool = False


def main() -> None:
    """Main function."""
    global points, player, orb
    greet()
    while(True ):
        inp: int = int(input("1: Take the LEFT path\n2: Talk to the Wizard\n3: Take the RIGHT path\n"))
        if(inp == 1):
            left()
        elif(inp == 2):
            talk_to_wizzard()
            if(orb):
                return
        elif(inp == 3):
            points = right(points)
        

def greet() -> None:
    """Intro to game."""
    print("Hi! Welcome to Adventure Quest...")
    player = input("Enter your name: ")
    print("Welcome " + player + "!")
    print("your goal is to find the wizard and give him his orb...\nGood luck!")


def talk_to_wizzard() -> None:
    """Talk to the wizard."""
    global points
    global player
    global orb
    THUMBS_UP: str = "\U0001F44D"
    if(orb):
        print(f"Oh cool thanks for finding my orb, {player}")
        print(f"You finished with {points} Points!")
        return
    else:
        print(f"Hi {player}, want to play a game for some points?...")
        if(input("y/n: ") == "y"):
            print(f"Awesome, i'll roll a dice and you guess the number...\n{THUMBS_UP}")
            looping: bool = True
            inp: int = int(input("Enter number 1-6:"))
            while(looping):
                if(inp <= 6 and inp >= 1):
                    if(inp == random.randint(1, 6)):
                        print("You got it!...\nI'll give you 2 points")
                        points += 2
                        print(f"Points: {points}")
                        looping = False
                    else:
                        print("Not Quite...")
                        print(f"Points: {points}")
                        looping = False
                else:
                    inp = int(input("Enter valid number 1-6:"))


def left() -> None:
    """Function describing left path."""
    global points
    print("You find a water fountain in an otherwise empty room with some cobwebs in the corner...\nYou turn your head down and see some coins...")
    inp: int = int(input("1: Keep the coins\n2: Throw them in the fountain for good luck\n"))
    if(inp == 1):
        points += 2
        print(f"Points: {points}")
    else:
        print("You threw them in...\nMaybe that'll help later...")
    return
    
def right(level: int) -> int:
    """Function describing actions after taking right path."""
    global orb
    if(level < 10):
        print("You get robbed...")
        fight: int = int(input("1: Fight back\n2: Run away\n"))
        beat: bool = random.randint(1,10) < 7
        if(fight == 1 and beat):
            print("You lose and get your points stolen")
            level = 0
            print(f"Points: {level}")
            return 0
        elif(fight == 2):
            print("You run and drop some points...")
            print(f"Points: {level}")
            return level - 2
        elif(fight == 1):
            print("You beat the robber and steal one of his points")
            print(f"Points: {level}")
            return level + 1
        
    print("There is a feeble man offering an orb for points...")
    accept: int = int(input("1. Accept\n2. Decline\n"))
    if(accept == 1):
        orb = True
        print("You should bring this to the Wizard...")
        return level
                    
if __name__ == "__main__":
  main()