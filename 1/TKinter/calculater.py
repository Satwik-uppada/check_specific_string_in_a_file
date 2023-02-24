import tkinter as tk
from tkinter import *
from tkinter import messagebox
window=tk.Tk()
window.title("Simple calculations")
window.geometry("500x700")
l1=tk.Button(text="+",fg="black",bg="white",font=("Arial Bold",10))
l1.grid(column=4,row=4)
window.mainloop()