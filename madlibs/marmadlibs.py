""" I created a MadLibs game, the user is asked to input words of a certain type such as an adjective, noun or past tense verb. Then, a story is printed to the screen with the input from the user."""

# Madlib Story:

# Parts of Speech Mad Libs from Everyday Speech
""" Tina and John walked deep into the _(adjective)_ woods. They came upon a _(adjective)_ old house. The house looked so _(adjective)_ and creepy. On the front porch sat an old large _(noun)_. Tina thought she heard a _(adjective)_ sound coming from the house. John _(past tense verb)_ so high he touched a tree branch!"""

# Properties
# firstAdj
# secondAdj
# thirdAdj
# noun
# fourthAdj
# pastTenseVerb

# Create a list
wordsInputStory = list()

# Create append function
def create(item):
    wordsInputStory.append(item)

# User Input Functions
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# Testing code
def test():
    user_value = user_input("Please eneter a value: ")
    print(user_value)

# Run Test
# test()

# Madlibs Function
def madLibs():
    # Start the game
    print("Hello! This is a MadLibs game. ")
    print("The Story:")
    # Display story with blanks
    print("Tina and John walked deep into the ___ woods. They came upon a ___ old house. The house looked so ___ and creepy. On the front porch sat an old large ___. Tina thought she heard a ___ sound coming from the house. John __ so high he touched a tree branch!")
    # Ask user to input words to fill in blanks
    firstAdj = user_input("Give me an adjective: ")
    # Everytime the user gives you a word append that word to the list by calling the create function
    create(firstAdj)
    secondAdj = user_input("Give me an adjective: ")
    create(secondAdj)
    thirdAdj = user_input("Give me an adjective: ")
    create(thirdAdj)
    noun = user_input("Give me noun: ")
    create(noun)
    fourthAdj = user_input("Give me an adjective: ")
    create(fourthAdj)
    pastTenseVerb = user_input("Give me a past tense action verb: ")
    create(pastTenseVerb)
    # Output story with blanks filled in
    print("Tina and John walked deep into the %s woods. They came upon a %s old house. The house looked so %s and creepy. On the front porch sat an old large %s. Tina thought she heard a %s sound coming from the house. John %s so high he touched a tree branch!" % (wordsInputStory[0], wordsInputStory[1], wordsInputStory[2], wordsInputStory[3], wordsInputStory[4], wordsInputStory[5]))

madLibs()
