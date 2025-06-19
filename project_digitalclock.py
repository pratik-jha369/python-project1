import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital clock")

def time():
    string =strftime("%H:%M:%S %p\n%d-%m-%Y")
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root,font=('calibri', 50, 'bold'), background='yellow',foreground ='black')
label.pack(anchor='center')

time()

root.mainloop()
    