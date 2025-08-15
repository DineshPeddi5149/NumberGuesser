import random

# Welcome Message
print()
print("[Welcome to the Number Guessing Game!]")
print("[I'm thinking of a number from 1 to 100.]")
print("[Guess what it is!] \n")


# Function to get a valid guess from player
def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("[Out of range! Please enter a number between 1 and 100.]\n")
            else:
                return guess
        except ValueError:
            print("[Invalid input! Please enter an integer between 1 and 100.]\n")

# Function to get a valid play again response from player
def get_valid_play_again():
    response = input("Play again? (y/n): ").lower()
    while (response != "y") and (response != "n"):
        print("[Invalid Input! Please enter 'y' or 'n'.]\n")
        response = input("Play again? (y/n): ").lower()
    return response

def play_round(number):
    attempts = 0
    guess = 0

    while guess != number:
        guess = get_valid_guess()
        attempts = attempts + 1

        if guess < number:
            print("[Too low]")
            print()
        elif guess > number:
            print("[Too high]")
            print()
        else:
            if attempts ==1:
                print("[Correct! You guessed it in just 1 try. Amazing!!]")
            else:
                print("[Correct! You guessed it in", attempts, "tries.]")
            print()



# Generate a random number between 1 and 100
number = random.randint(1, 100)
play_round(number)
play_again = get_valid_play_again()

# Loop more rounds
while play_again == "y":
    number = random.randint(1, 100)
    print()
    play_round(number)
    play_again = get_valid_play_again()

print("[Thanks for playing!]")
print()