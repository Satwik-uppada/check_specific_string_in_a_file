import tkinter
from tkinter import messagebox
window=tkinter.Tk()
window.title("Grid code")
window.geometry("500x500")
tkinter.Label(window,text="Username").grid(column=265,row=0)
entry1=tkinter.Entry(window)
entry1.grid(column=270,row=0)
tkinter.Label(window,text="password").grid(column=265,row=1)
entry2=tkinter.Entry(window)
entry2.grid(column=270,row=1)
tkinter.Checkbutton(window,text="Keep me logged in ").grid(column=270,columnspan=2)

def clicked():
    messagebox.showinfo("Message","submitted")

def clear_entry(event):
    entry1.delete(0,'end')
    entry2.delete(0,'end')

entry1.bind('<Return>',clear_entry)
entry2.bind('<Return>',clear_entry)

#The bind() method is called on a widget and takes two arguments:
#the first argument is the event type or a sequence of event types to bind,
#and the second argument is the function to be called when the event occurs.

button=tkinter.Button(window,text="submit",command=lambda: (clicked(),clear_entry(None))).grid(column=270,row=5)
window.mainloop()