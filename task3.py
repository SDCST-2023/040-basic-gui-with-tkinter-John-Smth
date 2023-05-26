import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("300x150")
window.resizable(False,False)



dogphoto = PhotoImage(file="dog.png")
labelDOG = tk.Label(window, image=dogphoto)

labelpl = tk.Label(window,text="",width = 10)

label1 = tk.Label(window,text="Pochacco!",width = 10)

label2 =tk.Label(window,text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero",width = 45, bg = "#77ffdf")





labelDOG.grid(row=1,column=1)
label1.grid(row=1,column = 2)
label2.grid(row=2, columnspan = 3)





window.mainloop()