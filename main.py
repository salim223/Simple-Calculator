from tkinter import *


screen = Tk()
screen.title("Simple Calculator")

entry = Entry(screen, width = 60, borderwidth=10)
entry.grid(row= 0, column= 0, columnspan = 4, padx = 20,)


    
def click_button(self):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0,(str(current) +str(self)))
    return

def clear_button():
    entry.delete(0, END)
        

def add_button():
    global first_number 
    first_number = float(entry.get())
    global math
    math = "addition"
    entry.delete(0, END)
        
def substract_button():
    global first_number
    first_number = float(entry.get())
    global math
    math = "substraction"
    entry.delete(0, END)
    
def multiply_button():
    global first_number
    first_number = float(entry.get())
    global math
    math = "multiplication"
    entry.delete(0, END)

def divide_button():
    global first_number
    first_number = float(entry.get())
    global math
    math = "division"
    entry.delete(0, END)
        
def equal_button():
    second_number = entry.get()
    entry.delete(0, END)

    if math == "addition" :
        entry.insert(0, first_number + float(second_number))
    if math == "substraction" :
        entry.insert(0, first_number - float(second_number))
    if math == "multiplication" :
        entry.insert(0, first_number * float(second_number))
    if math == "division" :
        entry.insert(0, first_number / float(second_number))


# Define number Buttons
button_9 = Button(text = "9", padx= 40, pady=10, command = lambda: click_button(9))
button_8 = Button(text = "8", padx= 40, pady=10, command = lambda: click_button(8))
button_7 = Button(text = "7", padx= 40, pady=10, command = lambda: click_button(7))
button_6 = Button(text = "6", padx= 40, pady=10, command = lambda: click_button(6))
button_5 = Button(text = "5", padx= 40, pady=10, command = lambda: click_button(5))
button_4 = Button(text = "4", padx= 40, pady=10, command = lambda: click_button(4))
button_3 = Button(text = "3", padx= 40, pady=10, command = lambda: click_button(3))
button_2 = Button(text = "2", padx= 40, pady=10, command = lambda: click_button(2))
button_1 = Button(text = "1", padx= 40, pady=10, command = lambda: click_button(1))
button_0 = Button(text = "0", padx= 40, pady=10, command = lambda: click_button(0))

# Define other Buttons
button_divide = Button(text = "/", padx= 40, pady=5, command = divide_button, bg= "pink")
button_Plus = Button(text = "+", padx= 40, pady=5, command = add_button, bg= "pink")
button_Minus = Button(text = "-", padx= 40, pady=5, command = substract_button, bg= "pink")
button_Multiply = Button(text = "x", padx= 40, pady=5, command = multiply_button, bg= "pink")
button_Equal= Button(text = "=", padx= 40, pady=15, command = equal_button, bg= "orange")
button_Dot= Button(text = ".", padx= 40, pady=5, command = lambda: click_button("."), bg= "pink")
button_clear= Button(text = "clear", padx= 30, pady=15, bg= "pink", command = clear_button)



# Put in the screen
button_clear.grid(column= 0, row=   1)

button_7.grid(column= 0 , row= 2)
button_8.grid(column= 1 , row= 2)
button_9.grid(column= 2 , row= 2)
button_divide.grid(column= 3 , row= 2)

button_4.grid(column= 0 , row= 3)
button_5.grid(column= 1 , row= 3)
button_6.grid(column= 2, row= 3)
button_Multiply.grid(column= 3 , row= 3)

button_1.grid(column= 0 , row= 4)
button_2.grid(column= 1 , row= 4)
button_3.grid(column= 2 , row= 4)
button_Minus.grid(column= 3, row = 4)

button_0.grid(column= 0, row= 5)
button_Dot.grid(column= 1 , row= 5)
button_Plus.grid(column= 2 , row= 5)
button_Equal.grid(column= 3, row= 5)






















screen.mainloop()