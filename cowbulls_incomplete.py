import random
from cowbulls import compare_numbers  # Import the compare_numbers function

playing = True  # Start playing the game
number = random.randint(0, 9999)  # Random 4-digit number
guesses = 0
print("Let's play a game of Cowbull!")  # Game explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow.")
print("For every number in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type 'exit' at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")  # Use input for Python 3.x
    if user_guess.lower() == "exit":
        break
    cowbullcount = compare_numbers(number, user_guess)  # Call the imported function
    guesses += 1

    print(f"You have {cowbullcount[0]} cows, and {cowbullcount[1]} bulls.")

    if cowbullcount[1] == 4:
        playing = False
        print(f"You win the game after {guesses} guesses! The number was {number}.")
        break  # End the game
    else:
        print("Your guess isn't quite right, try again.")


