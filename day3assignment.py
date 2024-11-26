#Day 3 Assignment
#Create a function named sortName(firstname, lastname, sortorder = "firstlast")
#that has an optional parameter sortorder.
#This will be defaulted at "firstlast" but the user can also input "lastfirst".
#If it is left at default, print out the name as "First Last".
#If they select "lastfirst" print out the name as "Last, First".

#Write a program that will ask the user for their first and last name,
#then supply these to the sortName function for both default and lastfirst sortorder.

#Function Definition

def sortName(firstname, lastname, sortorder = "firstlast"):
    if sortorder == "firstlast":
        #instead of printing directly from the function
        #we can return the value and use it that way
        #print(firstname + " " + lastname)
        return firstname + " " + lastname
    elif sortorder == "lastfirst":
        #print(lastname + " " + firstname)
        return lastname + " " +  firstname
    else:
        #another response can be for validation.
        return "Invalid sortorder."


#Program

#loop added to make sure first name and last name are filled out
#basic validation.
#Validation is a first line security measure and very important.

firstname = input("Please input your firstname: ")
lastname = input("Please input your lastname: ")

result = sortName(firstname, lastname)
result2 = sortName(firstname, lastname, "lastfirst")

print(result)
print()
print(result2)
