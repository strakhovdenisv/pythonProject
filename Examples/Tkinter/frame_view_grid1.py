import tkinter as tk

window = tk.Tk()

for i in range(3):
    """ столбцы и стрки реагируют на изменение размера окна"""
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0,3):
        frame = tk.Frame(master=window,relief=tk.RAISED,borderwidth=3)
        frame.grid(row=i, column=j, padx=5, pady=5)#отступ между рамками
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=3, pady=3)#отступ между ярлыка

window.mainloop()

    

