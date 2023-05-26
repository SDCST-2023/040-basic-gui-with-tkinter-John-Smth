import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("300x150")
window.resizable(False,False)



dogphoto = PhotoImage(file="dog.png")
labelDOG = tk.Label(window, image=dogphoto)


label1 = tk.Label(window,text="Pochacco!",width = 10)

label2 =tk.Label(window,text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero",width = 45, bg = "#77ffdf")

labelDOG.place(x=60 , y=5)
label1.place(x=130,y=50)
label2.place(x=0,y=100)


window.mainloop()