from tkinter import *
from operations import *
from memory import *

current_input = ""
memory_value = 0

def button_click(value):
    global current_input
    current_input += str(value)
    input_text.set(current_input)

def button_clear():
    global current_input
    current_input = ""
    input_text.set(current_input)

def button_equals():
    global current_input
    try:
        # eval используется только для базовой математики (+,-,*,/)
        result = eval(current_input)
    except ZeroDivisionError:
        result = "Ошибка: деление на ноль"
    except Exception:
        result = "Ошибка"
    current_input = str(result)
    input_text.set(current_input)

def button_memory_add():
    global current_input
    try:
        memory_add(float(current_input))
    except:
        pass

def button_memory_clear():
    memory_clear()

def button_memory_recall():
    global current_input
    current_input = str(memory_recall())
    input_text.set(current_input)

root = Tk()
root.title("Калькулятор")
root.geometry("400x600")

input_text = StringVar()

input_frame = Frame(root, width=400, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, textvariable=input_text, width=25, font=('arial', 24, 'bold'), bd=5, relief=SUNKEN, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btns_frame = Frame(root, width=400, height=450)
btns_frame.pack()

# Кнопки
buttons = [
    ['7','8','9','/','MC'],
    ['4','5','6','*','M+'],
    ['1','2','3','-','MR'],
    ['0','.','=','+','C'],
    ['sin','cos','^','sqrt','%'],
    ['floor','ceil']
]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == "=":
            b = Button(btns_frame, text=btn, width=6, height=2, command=button_equals)
        elif btn == "C":
            b = Button(btns_frame, text=btn, width=6, height=2, command=button_clear)
        elif btn == "M+":
            b = Button(btns_frame, text=btn, width=6, height=2, command=button_memory_add)
        elif btn == "MC":
            b = Button(btns_frame, text=btn, width=6, height=2, command=button_memory_clear)
        elif btn == "MR":
            b = Button(btns_frame, text=btn, width=6, height=2, command=button_memory_recall)
        elif btn == "sin":
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda: button_click("sin_deg("))
        elif btn == "cos":
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda: button_click("cos_deg("))
        elif btn == "sqrt":
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda: button_click("sqrt_num("))
        elif btn == "^":
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda: button_click("**"))
        elif btn == "%":
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda: button_click("%"))
        elif btn == "floor":
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda: button_click("floor_num("))
        elif btn == "ceil":
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda: button_click("ceil_num("))
        else:
            b = Button(btns_frame, text=btn, width=6, height=2, command=lambda x=btn: button_click(x))
        b.grid(row=i, column=j, padx=5, pady=5)

root.mainloop()

