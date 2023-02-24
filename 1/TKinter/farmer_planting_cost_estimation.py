import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("*** CROP COST CALCULATER ***")
window.geometry("400x250")
window.configure(bg="bisque")

size_of_field=tk.Label(window,text="Enter the size of field in acre: " ,bg="bisque").pack()
field_size=tk.Entry(window,width=30,bg="aqua",fg="black")
field_size.pack()

cost_of_seeds=tk.Label(window,text="Enter the cost of seeds per acre: ",bg="bisque").pack()
seeds_cost=tk.Entry(window,width=30,bg="aqua",fg="black")
seeds_cost.pack()

cost_of_fertilizers=tk.Label(window, text="Enter the cost of fertilizers per acre: ",bg="bisque").pack()
fertilizers_cost=tk.Entry(window,width=30,bg="aqua",fg="black")
fertilizers_cost.pack()

cost_of_labour=tk.Label(window, text="Enter the cost of labour per acre: ",bg="bisque").pack()
labour_cost=tk.Entry(window,width=30,bg="aqua",fg="black")
labour_cost.pack()

def Calculation_fun():
    result=(float(fertilizers_cost.get())+float(labour_cost.get())+float(seeds_cost.get()))*float((field_size.get()))
    search_result.config(text=result)

search_result=tk.Label(window,text="",bg="bisque")
search_result.pack()

search_button=tk.Button(window,text="Calculate",command=Calculation_fun,font="Bold,5",fg="white" ,bg="black")
search_button.pack()

window.mainloop()





