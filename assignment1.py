name = input("Please enter your name") #input variable
age = input("Please enter your age") #input variable

print("Welcome, " + name) #print welcome message with inpputed name by user

age = int(age) #convert the age value inputed by user to integer

"""if else conditions to print the particular message 
according to the age inputed by the user """

if age < 5: #condition will be true if age is less then 5
    print("You are very young")
elif age >= 5 and age < 15: #condition will be true if age is between 5-15
    print("You are young")
elif age >= 15 and age < 30: #condition will be true if age is between 15-30
    print("You are a young adult")
elif age >= 30 and age < 50: #condition will be true if age is between 30-50
    print("You are an adult")
elif age >= 50 and age < 65: #condition will be true if age is between 50-65
    print("You are middle aged")
else:                       #condition will be true if age above 65
    print("You are a senior citizen")
