import random
import os
import time
import sys

chances = None
guesses = None
easy_hs = None
medium_hs = None
hard_hs = None
timer = None


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def game_loop(chances):
    # Begin Game Loop
    clear_screen()
    start_time = time.time()
    number = random.randint(1, 100)
    guesses = chances
    while guesses > 0:
        while True:
            try:
                guess = int(input("Guess: "))
                break
            except ValueError:
                print("Try inputting a value!")
        guesses -= 1

        if guess > number:
            print(f"Incorrect! The number is less than {guess}")
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}")
        else:
            clear_screen()
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("You got it correct!")
            total_guesses = chances - guesses
            print(
                f"It took you {total_guesses} guesses and {elapsed_time:.2f} seconds to get it right!"
            )
            break

    if guesses <= 0:
        clear_screen()
        print("You lost!")
        print(f"The number is {number}")


def main():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("\nPlease select the difficulty level")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("\n> ")
        if choice == "easy":
            chances = 10
            break
        elif choice == "medium":
            chances = 5
            break
        elif choice == "hard":
            chances = 3
            break
        else:
            print("Wrong input! Try putting in a difficulty")

    clear_screen()
    print(f"You have chosen {choice} difficulty!")
    input("\nPress Enter to begin...")

    while True:
        print("\nWould you like to play another round? (y/n)")
        round_choice = input("\n> ").strip().lower()
        if round_choice == "y":
            game_loop(chances)
        if round_choice == "n":
            print("Thank you for playing!")
            sys.exit()
        else:
            print("Type Y or N")


main()
