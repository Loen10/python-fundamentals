# Conditional
# Method evaluate data
import random

# ask the user what the upper bound is and what their guess is
upper_bound = int(input("What is the upper bound? "))
random_number = random.randint(1, upper_bound)
guess = int(input("Guess a number between 1 and {} inclusive: " \
    .format(upper_bound)))

while guess != random_number:
    print("Nope, try again")
    guess = int(input("Guess a number between 1 and {} inclusive: " \
        .format(upper_bound)))

print("Correct, you win!")