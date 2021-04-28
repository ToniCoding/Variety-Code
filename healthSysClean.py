# Health system, with a maximum and a minimum. This is a test focused code, if you want to implement this in your code, you'll have to change a few details, but you can copy most of the code
# to avoid making it by yourself.

# Variables
health = 10

# Functions
def healthFunction(question,validInputs=("ADD","REM","KILL")):
    while (answer := input(question)) and answer not in validInputs:
        print(f"Please, choose between {validInputs}.") 
    return answer

# Code
print(f"Health is now {health}")
healthAction = healthFunction("ADD will ad one HP, REM will remove one HP and KILL will kill the player.\n")

# Actions taken
if healthAction == "ADD":
    health += 1
    if health > 10:
        health -= 1
        print(f"Health has been reduced by one because of the maximum being reached. Health is now {health}.") # This can be "print(health)" instead, so the player won't see this line.
    else:
        print(health)
elif healthAction == "REM":
    health -=1
    print(health)
elif healthAction == "KILL":
    health -=10
    exit("You died.")


# Coded by ToniCoding and created for SGE.