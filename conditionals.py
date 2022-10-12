# Conditional
# Method evaluate data
import random

# ask the user what the upper bound is and what their guess is

invalid_upper_bound = True
while invalid_upper_bound:
    upper_bound = input("What is the upper bound? ")
    
    if upper_bound.isdigit():
        invalid_upper_bound = False
        upper_bound = int(upper_bound)
    else:
        print("Please enter a whole number")

random_number = random.randint(1, upper_bound)
guess_count = 1
guess = input("Guess a number between 1 and {} inclusive: " \
    .format(upper_bound))

if guess.isdigit():
    guess = int(guess)

while guess != random_number:
    print("Nope, try again")
    guess = input("Guess a number between 1 and {} inclusive: " \
        .format(upper_bound))
    
    if guess.isdigit():
        guess = int(guess)

print("Correct, you won with {} guesses".format(guess_count))