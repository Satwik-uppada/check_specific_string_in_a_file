import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("*** Binary search ***")
window.geometry("500x150")
window.configure(bg="coral")
def Binary_search(array,key):
    first=0
    last=len(array)-1
    while first<=last:
        mid_value=(first+last)//2
        if array[mid_value]==key:
            return "Found {0} at index {1}".format(key,mid_value)
        elif array[mid_value]<key:
            first=mid_value+1
        else:
            last=mid_value-1
    return "Sorry..! {0} is not found in this array.".format(key)

def search_func():
 try:
    array=[]
    values_list=array_values.get().split(",")
    for i in values_list:
        array.append(int(i))
    target=int(key.get())

    result=Binary_search(array,target)
    search_result.config(text=result)
    messagebox.showinfo("Result",result)
 except:
      search_result.config(text="Error May be u gave extra comma ,check once")
      messagebox.showerror("Error","Check the input once,may be you gave wrong...")

input_values=tk.Label(window,text="Enter the array elements by separating with comma(ex:1,2,3,4):",bg="coral").pack()
array_values=tk.Entry(window,width=50,bg="sky blue",fg="black")
array_values.pack()

target_key=tk.Label(window, text="Enter the key value: ",bg="coral").pack()
key=tk.Entry(window,width=20,bg="sky blue",fg="black")
key.pack()

search_result=tk.Label(window,text="",bg="coral")
search_result.pack()
search_button=tk.Button(window,text="Search",command=search_func,font="Bold,5",fg="white" ,bg="black")
search_button.pack()

window.mainloop()





