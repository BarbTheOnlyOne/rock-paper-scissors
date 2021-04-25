import sys
from os import system, name

def main():
    intro()
    while True:
        player_1, player_2 = ask_for_plays()
        comparison(player_1, player_2)
        ask_for_continue()


def intro():
    """Prints the introduction to the game."""
    print("ROCK,PAPER & SCISSORS")
    print("Welcome to this 2 player game!")
    print("\nYour options are: rock, paper and scissors.\n")

def ask_for_plays():
    """Asks the players what do they play."""
    player_1 = valid_choice('one')
    clear()

    player_2 = valid_choice('two')
    return player_1, player_2

def clear():
    """Clears the terminal window."""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def valid_choice(player_num):
    """Asks for choice and validates it.""" 
    choice = input(f"Player {player_num.lower()}, what do you play? ").lower()

    if choice == 'rock' or choice == 'paper' or choice == 'scissors':
        return choice
    else:
        while True:
            print("That's not a valid option.")
            choice = input(f"Player {player_num}, what do you play? ").lower()
            if choice == 'rock' or choice == 'paper' or choice == 'scissors':
                return choice
            else:
                pass

def comparison(player_1, player_2):
    """Compares the plays and states the winner."""
    if player_1 == 'rock':
        if player_2 == 'rock':
            print("It's a draw!")
        elif player_2 == 'paper':
            print("Player two wins!")
        elif player_2 == 'scissors':
            print("Player one wins!")
    
    elif player_1 == 'scissors':
        if player_2 == 'rock':
            print("Player two wins!")
        elif player_2 == 'paper':
            print("Player one wins!")
        elif player_2 == 'scissors':
            print("It's a draw!")

    elif player_1 == 'paper':
        if player_2 == 'rock':
            print("Player one wins!")
        elif player_2 == 'paper':
            print("It's a draw!")
        elif player_2 == 'scissors':
            print("Player two wins!")

def ask_for_continue():
    """Ends the loop of the program."""
    answer = input("Do you want to play again?(yes/no) ")
    if answer.lower() == 'no':
        sys.exit()
    else:
        pass

while __name__ == '__main__':
    main()