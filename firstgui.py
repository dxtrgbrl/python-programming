#First GUI
from tkinter import *

def button1Click():
    print("You Clicked Button 1")

def button2Click():
    print("You Clicked Button 2")

app = Tk()
app.title("Application TITLE")
app.geometry('450x100+200+100')

b1 = Button(app, text = "Button1", width = 10, command = button1Click)
b1.pack(side = "left", padx = 10, pady = 10)

b2 = Button(app, text = "Button2", width = 10, command = button2Click)
b2.pack(side = "left", padx = 10, pady = 10)

#This should be at the end 
app.mainloop()


