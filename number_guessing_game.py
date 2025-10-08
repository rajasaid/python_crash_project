from random import *

def main():
    number = randint(1, 100)
    guess = None
    tries = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number:
        if tries == 0:
            print("You have 7 tries to guess the number.")
        elif 7 > tries > 0:
            print(f"You have {7 - tries} tries left.")
        else:
            print("No tries left.")
            break
        guess = input("Make a guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        tries += 1
        
        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {tries} tries.")

if __name__ == "__main__":
    main()
