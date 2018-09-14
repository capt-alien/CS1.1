
# Declare a list object

words = list()

#Create appendfunction

def add(item):
    words.append(item)

#Create User prompt Function

def uimput(prompt):
    uimput = input(prompt)
    return(uimput)

#Test Function:
def test():
    uimput = uimput("Enter a value Human! ")
    print(uimput)


# Starts the Madlibs sequance

print("Greetings Human! This is Space-Libs.... Got Game? ")


celest = uimput("Enter a type of celistal body: ")
add (celest)

	# Adjective
fstadj = uimput("Enter Adjative now: ")
add (fstadj)

    # Number
number = uimput("Enter Number now: ")
add (number)

	# Part of Body - Ends in ED
firstbp = uimput("Enter body part': ")
add (firstbp)

    # Part of Body - Ends in ED
secbp = uimput("Enter another body part: ")
add (secbp)

    # Part of Body - Ends in ED
trdbp = uimput("Enter a thrid body part: ")
add (trdbp)

    # Part of Body - Ends in ED
fobp = uimput("Enter a fourth body part: ")
add (fobp)

    # Animal (plural)
anmial = uimput("Enter an earth animal: ")
add (anmial)

#Food
food = uimput("Enter human food: ")
add (food)

    # Part of Body
lastbp = uimput("Enter one last human body part: ")
add (lastbp)


print("Captain Alien landed on a %s. The %s had lots of %s humanoids in it and they all had pet with %s %sed , %s %sed , %s %sed , %s %s %sed. In the next %s, everything was made out of %s! He came out with a %s ache." % (words[0], words[0], words[1], words[2], words[3], words[2], words[4], words[2], words[5], words[2], words[6], words[7], words[0], words[8], words[9]))
