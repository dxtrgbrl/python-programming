#Assignment 2
#Create a program that takes in a sentence from the user 

#and reverses all the characters using a loop.

sentence = input("Input a sentence to be reversed: ")
reversedSentence = ""

#when starting at the end of the string, we need to choose the length - 1
#since the first character is at character 0, so this shifts the whole
#list of characters down one number from what you would expect them to be.
counter = len(sentence) - 1

while counter >= 0:
    reversedSentence += sentence[counter]
    counter -= 1
#notice the "compound" operators += and -=
#using these is a short hand for keeping the value
#that is already present in the variable, and adding or subtracting
#the value from it. "num1 += 1" is the same as "num1 = num1 + 1"

print("Original Sentence: " + sentence)
print("Reversed Sentence: " + reversedSentence)


x = "this is the sentence that im reversing."
print(x)
y = x[::-1]
print (y)