import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("800x250")
window.configure(bg="white")


entry1=tk.Entry(window, width=20)
entry2=tk.Entry(window, width=20)
entry3=tk.Entry(window, width=20)
entry4=tk.Entry(window, width=20)
entry5=tk.Entry(window, width=20)
entry6=tk.Entry(window, width=20)


label1=tk.Label(window, text="Client Database", bg="white")
label2=tk.Label(window, text="Name", bg="white")
label3=tk.Label(window, text="Type",bg="white")
label4=tk.Label(window, text="Breed", bg="white")
label5=tk.Label(window, text="Owner",bg="white")
label6=tk.Label(window, text="Birthdate", bg="white")
dogphoto=tk.PhotoImage(file="dog.png")
label7 = tk.Label(window, image=dogphoto)


button1=tk.Button(window, text="Search by Name")
button2=tk.Button(window, text="< Previous")
button3=tk.Button(window, text="Next >")
button4=tk.Button(window, text="Save Entry")


label7.grid(row=1, column=1, rowspan=2)
button1.grid(row=1, column=10)
entry1.grid(row=1, column=12, columnspan=2)
label1.grid(row=3, column=8)
label2.grid(row=4, column=1)
label3.grid(row=4, column=6)
label4.grid(row=4, column=8)
label5.grid(row=4, column=10)
label6.grid(row=4, column=13)


entry2.grid(row=5, column=1)
entry3.grid(row=5, column=6)
entry4.grid(row=5, column=8)
entry5.grid(row=5, column=10)
entry6.grid(row=5, column=13)


button2.grid(row=7, column=1)
button4.grid(row=7, column=8)
button3.grid(row=7, column=14)


window.mainloop()
