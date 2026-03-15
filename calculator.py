from tkinter import *

# Create window
root = Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field
entry = Entry(root, width=20, borderwidth=5, font=("Arial",18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Buttons
Button(root, text="7", padx=20, pady=20, command=lambda: click(7)).grid(row=1,column=0)
Button(root, text="8", padx=20, pady=20, command=lambda: click(8)).grid(row=1,column=1)
Button(root, text="9", padx=20, pady=20, command=lambda: click(9)).grid(row=1,column=2)
Button(root, text="/", padx=20, pady=20, command=lambda: click("/")).grid(row=1,column=3)

Button(root, text="4", padx=20, pady=20, command=lambda: click(4)).grid(row=2,column=0)
Button(root, text="5", padx=20, pady=20, command=lambda: click(5)).grid(row=2,column=1)
Button(root, text="6", padx=20, pady=20, command=lambda: click(6)).grid(row=2,column=2)
Button(root, text="*", padx=20, pady=20, command=lambda: click("*")).grid(row=2,column=3)

Button(root, text="1", padx=20, pady=20, command=lambda: click(1)).grid(row=3,column=0)
Button(root, text="2", padx=20, pady=20, command=lambda: click(2)).grid(row=3,column=1)
Button(root, text="3", padx=20, pady=20, command=lambda: click(3)).grid(row=3,column=2)
Button(root, text="-", padx=20, pady=20, command=lambda: click("-")).grid(row=3,column=3)

Button(root, text="0", padx=20, pady=20, command=lambda: click(0)).grid(row=4,column=0)
Button(root, text="C", padx=20, pady=20, command=clear).grid(row=4,column=1)
Button(root, text="=", padx=20, pady=20, command=calculate).grid(row=4,column=2)
Button(root, text="+", padx=20, pady=20, command=lambda: click("+")).grid(row=4,column=3)

# Run program
root.mainloop()