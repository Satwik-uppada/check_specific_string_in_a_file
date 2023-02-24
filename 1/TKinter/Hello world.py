# import tkinter as t
# """ *** Hello world in tkinter *** """
#
# window=t.Tk()
# window.title("GUI of Hello World!")
# label1=t.Label(window,text="Hello World!").pack()
# window.mainloop()


""" *** Font style and size in tkinter *** """
import blue as blue

# import tkinter as t
# window=t.Tk()
# window.title("Label widget")
# l1=t.Label(window,text="Satwik",font=("Arial Bold",50))
# l1.grid(column=0,row=0)
# window.mainloop()

# """ *** Geometry function *** """
#
# import tkinter as t
# window=t.Tk()
# window.title("GGeometry function")
# l1=t.Label(window,text="Satwik",font=("Arial Bold",50))
# window.geometry('500x800')
# l1.grid(column=0,row=0)
# window.mainloop()


# """ *** Button widget ***"""
# import tkinter as t
# window=t.Tk()
# window.title("BUTTON WIDGET")
# l1=t.Label(window,text="Satwik",font=("Arial Bold",10))
# window.geometry('500x200')
# l1.grid(column=0,row=0)
# bt=t.Button(window,text="Enter",bg="orange",fg="black") # bg-background fg-foreground color
# bt.grid(column=1,row=0) # using gird to set the button position
# window.mainloop()


# """ *** Button widget click event ***"""
# import tkinter as t
# window=t.Tk()
# window.title("BUTTON WIDGET")
# l1=t.Label(window,text="Satwik",font=("Arial Bold",10))
# window.geometry('500x200')
# l1.grid(column=0,row=0)
#
# def clicked():
#     l1.configure(text="Button was clicked !!")
#
# bt=t.Button(window,text="Enter",bg="orange",fg="black",command=clicked) # bg-background fg-foreground color
# bt.grid(column=1,row=0) # using gird to set the button position
# window.mainloop()

# """ *** Entry widget *** """
# import tkinter
# window=tkinter.Tk()
# window.title("Entry widget")
# window.geometry('500x300')
# l1=tkinter.Label()
# l1.grid(column=0,row=0)
# txt=tkinter.Entry(window,width=20)
# txt.grid(column=1,row=0)
# def clicked():
#     res = "Hi ,I'm " + txt.get()
#     l1.configure(text= res)
# bt= tkinter.Button(window, text="Enter", bg="red", fg="black", command=clicked)
# bt.grid(column=3,row=0)
# window.mainloop()

""" *** Combobox *** """
# import tkinter
# from tkinter.ttk import *
# window=tkinter.Tk()
# window.title("Combobox widget")
# combo=Combobox(window)
# combo['values']=(1,2,3,4,5,"text")
# combo.current(3)
# combo.grid(column=0,row=0)
# window.mainloop()

# import tkinter
# from tkinter import *
# window=tkinter.Tk()
# window.title("Checkbutton widget")
# window.geometry("500x400")
# chk_state=BooleanVar()
# """Creating a variable of type Booleanvar
# which is not a standard python variable,
# it's a tkinter variable"""
# chk_state.set(True)
# chk=Checkbutton(window,text="Select",var=chk_state)
# chk.grid(column=0,row=0)
# rad1=Radiobutton(window,text="python" ,value=1)
# rad2=Radiobutton(window,text="java" ,value=2)
# rad3=Radiobutton(window,text="c++" ,value=3)
# rad1.grid(column=2,row=0)
# rad2.grid(column=3,row=0)
# rad3.grid(column=4,row=0)
# window.mainloop()


# import tkinter
# from tkinter import messagebox
# messagebox.showinfo('Message title','Message content')

# import tkinter
# from tkinter import *
# from tkinter import messagebox
# window=tkinter.Tk()
# def clicked():
#     messagebox.showinfo("Message title","Message content will display like this")
# btn=Button(window,text="Enter",command=clicked)
# btn.grid(column=0,row=0)
# window.mainloop()


import tkinter
from tkinter import *
window=tkinter.Tk()
spin=Spinbox(window,from_=0,to=100,width=5)# width is decided as per content in spin box
spin.grid(column=0,row=0)
window.mainloop()


# import tkinter
# from tkinter import *
# window=tkinter.Tk()
# window.geometry("500x400")
# window.title("Organizing layout and widgets")
# #creating 2 frames top and bottom
# top_frame=tkinter.Frame(window).pack()
# bottom_frame=tkinter.Frame(window).pack(side= "bottom")
#
# btn1 = tkinter.Button(top_frame,text="Button1" ,fg="red").pack()
# btn2 = tkinter.Button(top_frame,text="Button2" ,fg="red").pack()
# btn3 = tkinter.Button(bottom_frame,text="Button3" ,fg="blue").pack(side="left")
# btn4 = tkinter.Button(bottom_frame,text="Button4" ,fg="orange").pack(side="left")
# window.mainloop


# import tkinter
# window=tkinter.Tk()
# window.title("Pack function ")
# tkinter.Label(window ,text="suf. width", fg="white",bg="purple").pack()
# tkinter.Label(window,text="Taking all the available X width",fg="white",bg="green").pack(fill="x")
# tkinter.Label(window,text="Taking all available Y height",fg="white" ,bg="black").pack(side="left",fill="y")
# window.mainloop()




