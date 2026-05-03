# dice rolling game by mosh hamedani

# Ask : roll the dice
# if user enters y
# .    generate two random numbers
# .    print the numbers
# if user enters n
# .     print thank u message
#     terminate the program-exit the game
# if user enters anything else
# .print invalid input/choice

import random
# loop until user enters valid input

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"({dice1}, {dice2})")
    elif choice == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
