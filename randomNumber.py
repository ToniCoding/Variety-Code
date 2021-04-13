# This code will modify the variable number depending on the randomized number that random.randint(a,b) gives.


# Imports.
import random


# Variables.
number = 100

operation = random.randint(10,20) # In this range, both limits are included in the possible numbers.


# Actions.
print(number + operation) # Addition.

print(number - operation) # Subtract.

print(number * operation) # Multiplication.

print(number / operation) # Division --- This one will give decimals most of the times.