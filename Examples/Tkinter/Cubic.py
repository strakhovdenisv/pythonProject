import tkinter as tk
import random 

def rand():
    lbl_value["text"] = str(random.randint(1,6))
     

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="Drope", command = rand)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window)
lbl_value.grid(row=0, column=1)


window.mainloop()
