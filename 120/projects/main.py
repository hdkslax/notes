# Fortune Cookie Generator
# Author: XXX
# Date: Jan. 24, 2021
# Generates a random fortune

import random

# Create a list
fortunes = ["have great success.", "find love.", "become rich."]

# Select random
random_fortune = random.choice(fortunes)

# Output
print("You will " + random_fortune)