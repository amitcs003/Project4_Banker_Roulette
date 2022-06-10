
## Banker Roulette - Who will pay the bill?
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

Count = len(names)

random_position = random.randint(0, Count-1)

print(f"{names[random_position]} is going to buy the meal today!")
