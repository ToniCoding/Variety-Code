# Imports.
from random import choice

# Variables.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
specialCharacters = ['!', '_', '-', '@', '+', '%']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
numb = [1, 2, 3]
commandExample = "/generate safest 12"

# Password generator funciton ran by main.py.
def passwordGen():
    # Explanation, ask for command and variables that affect password generating and loop state.
    print("Welcome to password generator tool. Remember that the parameters for password generation are /generate [securityLevel] [passwordLenght]")
    try:
        pwdParameters = input(f"Input your parameters here. Parameters examples {commandExample}\n>>> ").lower()
    except KeyboardInterrupt:
        print("Keyboard interrupt detected")
    generating = True
    parametersListed = (pwdParameters.split())
    security = parametersListed[1] # Security parameter.
    lenght = parametersListed[2] # Lenght parameter.
    
    # Password generator loop.
    while generating == True:
        generatedPwd = ''
        lenghtGenerated = 0
        while len(generatedPwd) < int(lenght):
            rng = choice(numb)
            if security == 'safe': # Category SAFE security.
                if rng == 1:
                    randomgGen = choice(alphabet)
                if rng == 2:
                    randomgGen = choice(specialCharacters)
                if rng == 3:
                    randomgGen = choice(numbers)
            if security == 'medium': # Category MEDIUM security.
                if rng == 1:
                    randomgGen = choice(alphabet)
                if rng == 3:
                    randomgGen = choice(numbers)
            if security == 'low': # Category LOW security.
                randomgGen = choice(alphabet)
            generatedPwd = generatedPwd + randomgGen # Concat character or number generated with the password.
            lenghtGenerated += 1
            if lenghtGenerated == int(lenght): # Checker to get the password as long as parameter defined.
                print(generatedPwd)
        generating = False # Loop breaker.