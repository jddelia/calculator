#! /usr/bin/python3

""" This program creates a calculator, using tkinter.
    Guidance taken from https://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html"""

from tkinter import *

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, "%P"))

        self.add_button = Button(master, text="+", command=lambda : self.update("add"))
        self.sub_button = Button(master, text="-", command=lambda : self.update("subtract"))
        self.clear_button = Button(master, text="Clear", command=lambda : self.update("clear"))
        self.mult_button = Button(master, text="*", command=lambda : self.update("multiply"))
        self.div_button = Button(master, text="/", command=lambda : self.update("divide"))
        self.evaluate_button = Button(master, text="=", command=lambda : print(self.total))

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.sub_button.grid(row=2, column=1)
        self.clear_button.grid(row=2, column=2, sticky=W+E)
        self.mult_button.grid(row=3, column=0)
        self.div_button.grid(row=3, column=1)
        self.evaluate_button.grid(row=3, column=2, sticky=W+E)

    def validate(self, text):
        if not text:
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(text)
            return True
        except ValueError:
            return False

    def update(self, operation):
        if operation == "add":
            self.total += self.entered_number
        elif operation == "subtract":
            self.total -= self.entered_number
        elif operation == "multiply":
            self.total *= self.entered_number
        elif operation == "divide":
            self.total /= self.entered_number
        else:
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()

app = Calculator(root)

root.mainloop()
