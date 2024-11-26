#Bank Account Exercise
#Create a program loop that asks the user if they want to continue.
#If they do, ask them what kind of transaction, deposit or withdrawal
#Otherwise thank the user and end the program.
#They must first deposit money to withdrawal because there
#is no money in the bank. If they try to withdrawal and
#they have insufficient funds, tell them and restart
#only allow amounts > 0 to be withdrawn.
#only allow Y or N as input for continuing the program, if they give the wrong
#input, tell them and ask again.
#Ask for Deposit (D), Withdrawal (W) or Balance(B)

#Start the program
continueProgram = True
questionContinue = ""
balance = 0.0
numOfTransactions = 0

questionContinue = input("Would you like to do more banking? Y or N?")
if questionContinue.upper() == "Y":
    continueProgram = True
elif questionContinue.upper() == "N":
    continueProgram = False

while continueProgram:
    action = ""
    amount = 0
    while action.upper() != "D" and action.upper() != "W" and action.upper() != "B" and action.upper() != "Q":
        action = input("Deposit(D), Withdrawal(W) or Balance(B) (Q to Quit)?")
       
    if action.upper() == "W":
        while amount <= 0:
            amount = input("Amount: ")
            amount = int(amount)
            if amount > balance:
                amount = 0
                print("Amount more than balance of $" + str(balance))
            
        #outside the loop
        balance -= amount
    elif action.upper() == "D":
        while amount <= 0:
            amount = input("Amount: ")
            amount = int(amount)
        balance += amount
    elif action.upper() == "B":
        print("Balance: $" + str(balance))
    elif action.upper() == "Q":
        break
    numOfTransactions += 1

    #ask the question again from the loop to keep it going.
    while questionContinue.upper() != "Y" and questionContinue.upper() != "N":
        questionContinue = input("Would you like to do more banking? Y or N?")

    if questionContinue.upper() == "Y":
        continueProgram = True
    elif questionContinue.upper() == "N":
        continueProgram = False

print("Total Transactions: " + numOfTransActions)
    

    
