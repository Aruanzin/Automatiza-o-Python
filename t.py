import json
import tkinter as tk
from tkinter import filedialog as fd


win = tk.Tk()
win.geometry("500x500")

# main
main_frame = tk.Frame(win)
main_frame.pack(fill=tk.BOTH, expand=1)

# canvas
my_canvas = tk.Canvas(main_frame, bg='red')
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# scrollbar
my_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

btn1 = tk.Button(main_frame,
                  text="Browse...",
                  compound="left",
                  fg="blue", width=22,
                  font=("bold", 10),
                  height=1,
                  )

btn1.place(x=300, y=300)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = tk.Frame(my_canvas, bg='white')

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
win.mainloop()