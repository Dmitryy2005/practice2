from tkinter import Tk, Button, Entry, StringVar
from operations import *
from memory import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        self.input_text = StringVar()
        self.entry = Entry(master, textvariable=self.input_text, width=25, font=('Arial', 20), bd=5, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('M+', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('MC', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('MR', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('floor', 5, 2), ('ceil', 5, 3), ('^', 5, 4)
        ]

        for (text, row, col) in buttons:
            Button(master, text=text, width=5, height=2, font=('Arial', 15),
                   command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)

    def on_button_click(self, char):
        try:
            if char == "C":
                self.input_text.set("")
            elif char == "=":
                self.calculate()
            elif char == "M+":
                memory_add(eval(self.input_text.get()))
            elif char == "MC":
                memory_clear()
            elif char == "MR":
                self.input_text.set(str(memory_recall()))
            elif char in ["sin", "cos", "floor", "ceil"]:
                value = float(self.input_text.get())
                if char == "sin":
                    self.input_text.set(str(sin_deg(value)))
                elif char == "cos":
                    self.input_text.set(str(cos_deg(value)))
                elif char == "floor":
                    self.input_text.set(str(floor_num(value)))
                elif char == "ceil":
                    self.input_text.set(str(ceil_num(value)))
            else:
                self.input_text.set(self.input_text.get() + char)
        except Exception:
            self.input_text.set("Ошибка")

    def calculate(self):
        try:
            expr = self.input_text.get().replace("^", "**")
            result = eval(expr, {"__builtins__": None}, globals())
            self.input_text.set(str(result))
        except Exception:
            self.input_text.set("Ошибка")

if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()
