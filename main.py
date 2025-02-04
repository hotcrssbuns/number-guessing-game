import random
import os


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main():
    chances = None
    guesses = None
    easy_hs = []
    medium_hs = []
    hard_hs = []
    timer = None

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

    # Begin Game Loop
    clear_screen()
    number = random.randint(1, 100)
    guesses = chances

    while guesses > 0:
        guess = int(input("Guess: "))
        guesses -= 1

        if guess > number:
            print(f"Lower!")
        elif guess < number:
            print(f"Higher!")
        else:
            clear_screen()
            print("You got it correct!")
            total_guesses = chances - guesses
            print(f"It took you {total_guesses} guesses to get it right!")
            break

    if guesses <= 0:
        print()


main()
