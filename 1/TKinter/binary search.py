import tkinter as tk

# Create a tkinter window
root = tk.Tk()

# Create a canvas with a circular button shape
canvas = tk.Canvas(root, width=50, height=50, bg='white', highlightthickness=0)
canvas.create_oval(0, 0, 50, 50, fill='red', outline='red')
canvas.create_text(25, 25, text='Click', fill='white', font=('Arial', 10, 'bold'))

# Create a button using the canvas
button = tk.Button(root, bd=0, bg='white', activebackground='white', command=lambda: print('Button clicked'))
button.pack()
button_window = canvas.create_window(0, 0, anchor='nw', window=button)

# Run the window
root.mainloop()
