import tkinter
from tkinter import *
from tkinter import messagebox
window=tkinter.Tk()
var=tkinter.IntVar()#

window.title("Radio buttons")
window.geometry("500x500")
tkinter.Label(window,text="First Name:").grid(column=1,row=2)
entry1=tkinter.Entry(window)
entry1.grid(column=3,row=2)
tkinter.Label(window,text="Last Name:").grid(column=1,row=3)
entry2=tkinter.Entry(window)
entry2.grid(column=3,row=3)
def check_content():
    content1=entry1.get()
    content2=entry2.get()
    if content1=="":
     messagebox.showerror("Error message","please provide firstname.")
    if content2=="":
     messagebox.showerror("Error message","please provide lastname.")

def clear_entry():
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    selected_option= var.get()
    b1.deselect()
    b2.deselect()
    b3.deselect()
    var.set(selected_option)

def validate():
    if entry1.get() and entry2.get():
        messagebox.showinfo("Submitted message","All fields are submitted")

    else:
        messagebox.showerror("Error","Please provide required information")

tkinter.Label(window,text="Gender:").grid(column=1,row=5)
b1=Radiobutton(window,text="Male",variable=var,value=1)
b1.grid(column=3,row=5)
b2=Radiobutton(window,text="Female",variable=var,value=2)
b2.grid(column=4,row=5)
b3=Radiobutton(window,text="Others",variable=var,value=3)
b3.grid(column=5,row=5)

clear_button=tkinter.Button(window,text="Submit",command=lambda:(check_content(),validate(),clear_entry()),fg="black",bg="orange")
clear_button.grid(column=3,row=7)
window.mainloop()