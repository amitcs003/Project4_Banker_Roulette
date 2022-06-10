
## Banker Roulette - Who will pay the bill?
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

## Could be done in 2 ways:

# Approach 1. Using lists in python
Count = len(names)
random_position = random.randint(0, Count-1)

print(f"Approach 1: {names[random_position]} is going to buy the meal today!")

# Approach 2. Using random.choice() function
person_who_will_pay = random.choice(names)
print(f" Approach 2: {person_who_will_pay} is going to buy the meal today!")




