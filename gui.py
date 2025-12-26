import tkinter as tk
from operations import *
from memory import *

def button_click(value):
    entry.insert(tk.END, str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_equals():
    expr = entry.get()
    try:
        expr = expr.replace("sin", "sin_deg")
        expr = expr.replace("cos", "cos_deg")
        expr = expr.replace("sqrt", "sqrt_num")
        expr = expr.replace("^", "**")
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def button_memory_add():
    try:
        memory_add(float(entry.get()))
        entry.delete(0, tk.END)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def button_memory_clear():
    memory_clear()
    entry.delete(0, tk.END)

def button_memory_recall():
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(memory_recall()))

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=25, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('%', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sqrt', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('C', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('floor', 5, 2), ('ceil', 5, 3),
    ('M+', 6, 0), ('MC', 6, 1), ('MR', 6, 2)
]

for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(root, text=text, width=5, height=2, command=button_equals)
    elif text == "C":
        b = tk.Button(root, text=text, width=5, height=2, command=button_clear)
    elif text == "M+":
        b = tk.Button(root, text=text, width=5, height=2, command=button_memory_add)
    elif text == "MC":
        b = tk.Button(root, text=text, width=5, height=2, command=button_memory_clear)
    elif text == "MR":
        b = tk.Button(root, text=text, width=5, height=2, command=button_memory_recall)
    else:
        b = tk.Button(root, text=text, width=5, height=2, command=lambda val=text: button_click(val))
    b.grid(row=row, column=col, padx=2, pady=2)

root.mainloop()
