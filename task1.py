#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("600x40")
window.resizable(False,False)






entry1 = tk.Entry(window,text="Num 1", width=20)

label1 = tk.Label(window,text="X")

entry2 = tk.Entry(window,text="Num 2", width=20)

label2 = tk.Button(window,text="=")

entry3 = tk.Label(window,text="", width=20)





label1.grid(row = 1, column = 2)
label2.grid(row = 1, column = 4)

entry1.grid(row=1, column = 1)
entry2.grid(row=1, column = 3)
entry3.grid(row=1, column = 5)


def f1(e):
    num1 = entry1.get()
    num2 = entry2.get()

    
    answer = float(num2)*float(num1)
    print(answer)
    entry3.config(text=answer)

def f2(e):
    print(e)



label2.bind('<Button-1>',f1)
label2.bind('<Button-2>',f2)

















window.mainloop()