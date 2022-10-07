# Conditional
# Method evaluate data
import random

high_range = 100
middle_number = int(high_range / 2)
my_guess = middle_number
guesses_count = 0
random_number = random.randint(1, high_range)
comparison = "equal to"

#evaluate the random number and compare it to the middle number
if my_guess > random_number:
    comparison = "higher than"
elif my_guess < random_number:
    comparison = "lower than"

print("{} is {} {}".format(my_guess, comparison, random_number))