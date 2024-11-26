#Week 2 Python Assignment

import sqlite3

#ask the user to continue
continueBool = True
askContinue = input("Would you like to submit your favourite color? (Y)es or (N)o: ")

while askContinue.upper() != "Y" and askContinue.upper() != "N":
    print("Invalid input")
    askContinue = input("Would you like to submit your favourite color? (Y)es or (N)o: ")

if askContinue.upper() == "Y":
    continueBool = True
elif askContinue.upper() == "N":
    continueBool = False

while continueBool:
    #input color
    favColor = input("Select one: \n1 - Black\n2 - White\n3 - Red\n4 - Blue\n5 - Green\n9 - Quit\n\n")

    while favColor != "1" and favColor != "2" and favColor != "3" and favColor != "4" and favColor != "5" and favColor != "9":
        print("Invalid Selection\n")
        favColor = input("Select one: \n1 - Black\n2 - White\n3 - Red\n4 - Blue\n5 - Green\n9 - Quit\n\n")

    favColor = int(favColor)
    outputColor = "" #to be used for database insert

    if favColor == 1:
        outputColor = "1 - Black"
    elif favColor == 2:
        outputColor = "2 - White"
    elif favColor == 3:
        outputColor = "3 - Red"
    elif favColor == 4:
        outputColor = "4 - Blue"
    elif favColor == 5:
        outputColor = "5 - Green"
    elif favColor == 9:
        break #using a break statement will make us leave the loop
    #submit to db
    db = sqlite3.connect("yourname.db")    

    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("INSERT INTO users VALUES (NULL, '" + outputColor + "');") #execute our sql statement
    #close the connection
    cursor.close()

    #start again
    #ask user again to continue
    askContinue = ""
    askContinue = input("Would you like to submit your favourite color? (Y)es or (N)o: ")

    while askContinue.upper() != "Y" and askContinue.upper() != "N":
        print("Invalid input")
        askContinue = input("Would you like to submit your favourite color? (Y)es or (N)o: ")

    if askContinue.upper() == "Y":
        continueBool = True
    elif askContinue.upper() == "N":
        continueBool = False
#end of loop    

#output results
print("Thank you for participating.")

totalBlack = 0
totalWhite = 0
totalRed = 0
totalBlue = 0
totalGreen = 0

cursor = db.cursor()
cursor.execute("SELECT * FROM survey WHERE choice = '1 - Black'") #execute our sql statement
rows = cursor.fetchall() #store all rows in a variable

for each_row in rows:
    totalBlack += 1
    
cursor.close()

cursor = db.cursor()
cursor.execute("SELECT * FROM survey WHERE choice = '2 - White'") #execute our sql statement
rows = cursor.fetchall() #store all rows in a variable

for each_row in rows:
    totalWhite += 1
    
cursor.close()

cursor = db.cursor()
cursor.execute("SELECT * FROM survey WHERE choice = '3 - Red'") #execute our sql statement
rows = cursor.fetchall() #store all rows in a variable

for each_row in rows:
    totalRed += 1
    
cursor.close()

cursor = db.cursor()
cursor.execute("SELECT * FROM survey WHERE choice = '4 - Blue'") #execute our sql statement
rows = cursor.fetchall() #store all rows in a variable

for each_row in rows:
    totalBlue += 1
    
cursor.close()

cursor = db.cursor()
cursor.execute("SELECT * FROM survey WHERE choice = '5 - Green'") #execute our sql statement
rows = cursor.fetchall() #store all rows in a variable

for each_row in rows:
    totalGreen += 1
    
cursor.close()

print("\nTotal Black: " + str(totalBlack))
print("Total White: " + str(totalWhite))
print("Total Red: " + str(totalRed))
print("Total Blue: " + str(totalBlue))
print("Total Green: " + str(totalGreen))
