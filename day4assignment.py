#Assignment 4
#Part 1.
#Create an array to hold names.
#Allow the user to put in 5 guesses at a secret name
#Create a variable secretname that holds a secret name

#Create a function that uses a loop to go through each 

#name. Check to see if the element in the array matches the 

#secret name value. if it does, break out of the loop. 

#return true if the secret name was found, false if not 

#found. Name the function "checkNameGuesses(guesses, 

#secretname)"

#Part 2.
#Create a function that uses a loop to output each name in 

#the list in reverse order from last element to first.
#write these results to a file.
#Call this function "reverseNamesAndWriteToFile(names)"

#Function Definitions
def checkNameGuesses(guesses, secretname):
    for name in guesses:
        if name == secretname:
            return True

    return False

def reverseNamesAndWriteToFile(names):
    reverseNames = []
    #reverseNames = names.reverse()
    counter = len(names) - 1
    while counter >= 0:
        reverseNames.append(names[counter])
        counter -= 1
    #write results to file
    file = open("result.txt", "r+")
    for name in reverseNames:
        file.write(name + "\n")
    file.close()

#The Program
guesses = []
secretname = "Mike"

counter = 1
while counter <= 5:
    guesses.append(input("Input guess number " + str(counter) + ": "))
    counter += 1
    result = checkNameGuesses(guesses, secretname)
    if result == True:
        break

if result == True:
    print("You got it, the secret name was: " + secretname)
else:
    print("Sorry, please try again.")

reverseNamesAndWriteToFile(guesses)







