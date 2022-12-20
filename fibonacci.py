# -*- coding: utf-8 -*-
from tkinter import *

root=Tk()
root.title("Fibonacci Sum")

root.geometry("400x400")

user_input = Entry(root)

label_series = Label(root, text="Fibonacci Series: ")
label_spiral = Label(root)

def generateSeries():
    user_value = int(user_input.get())
    
    num1 = 0
    num2 = 1
    sum = 0
    counter = 1
    sum2 = 0
    
    while (counter <= user_value):
        sum2 = sum2 + sum
        counter += 1
        num1 = num2
        num2 = sum
        sum = num1 + num2
        label_series["text"] += str(sum2) + " "
        label_spiral["text"] = "Fibonacci Sum: " + str(sum2)
        
btn = Button(root, text="Show Fibonacci Series", command=generateSeries, bg="azure")

user_input.pack()
btn.pack()
label_series.pack()
label_spiral.pack()

root.mainloop()