import random

# Welcome Message
print()
print("[Welcome to the Number Guessing Game!]")
print("[I'm thinking of a number. You choose the difficulty!]\n")

# Function to get a valid difficulty level
def get_difficulty():
    print("[Selected Difficulty]")
    print("> Easy (E): 1-10")
    print("> Medium (M): 1-50")
    print("> Hard (H): 1-100 \n")
    choice = input("Choose your difficulty (E/M/H): ").lower()

    while choice not in ['e','m','h']:
        print("[Invalid input! Please enter E, M, or H.]\n")
        choice = input("Choose your difficulty (E/M/H): ").lower()
    
    if choice == 'e':
        return 10
    elif choice == 'm':
        return 50
    else:
        return 100


# Function to get a valid guess from player
def get_valid_guess(range_max):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > range_max:
                print(f"[Out of range! Please enter a number between 1 and {range_max}.]\n")
            else:
                return guess
        except ValueError:
            print(f"[Invalid input! Please enter an integer between 1 and {range_max}.]\n")

# Function to get a valid play again response from player
def get_valid_play_again():
    response = input("Play again? (y/n): ").lower()
    while (response != "y") and (response != "n"):
        print("[Invalid Input! Please enter 'y' or 'n'.]\n")
        response = input("Play again? (y/n): ").lower()
        print()
    return response

# Function to play 1 round
def play_round(number, range_max):
    attempts = 0
    guess = 0

    while guess != number:
        guess = get_valid_guess(range_max)
        attempts += 1

        if guess < number:
            print("[Too low]\n")
        elif guess > number:
            print("[Too high]\n")
        else:
            if attempts ==1:
                print("[Correct! You guessed it in just 1 try. Amazing!!]")
            else:
                print(f"[Correct! You guessed it in {attempts} tries.]")
            print()



# Generate a random number between 1 and 100
range_max = get_difficulty()
number = random.randint(1, range_max)
play_round(number, range_max)
play_again = get_valid_play_again()

# Loop more rounds
while play_again == "y":
    range_max = get_difficulty()
    number = random.randint(1, range_max)
    print()
    play_round(number, range_max)
    play_again = get_valid_play_again()

print("[Thanks for playing!]\n")