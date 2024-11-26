def getNumbers():
    num1 = int(input("Input Num1: "))
    num2 = int(input("Input Num2: "))
    #first if statement
    if num1 > 0 and num2 > 0:
        print("2 positive numbers")
    elif num1 < 0 and num2 < 0:
        print("2 negative numbers")
    elif num1 > 0 and num2 < 0:
        print("num1 is positive, num2 is negative")
    elif num1 > 0 and num2 < 0:
        print("num1 is positive, num2 is negative")
    #second if statement
    if num1 > 0 or num2 > 0:
        print("One number is positive")
    elif num1 < 0 or num2 < 0:
        print("One number is negative")
    #output math
    print("Addition Result: " + str(num1 + num2))
    print("Subtraction Result: " + str(num1 - num2))
    print("Multiplcation Result: " + str(num1 * num2))
    print("Division Result: 0.3333" + str(num1 / num2))

getNumbers()
    
