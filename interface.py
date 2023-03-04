import tkinter as tk

window = tk.Tk()
window.title("MapMarker - MM")
window.attributes('-zoomed', True)

label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

button = tk.Button(window, text="Click me!")
button.pack()

def button_click():
    label.config(text="Button was clicked!")

button.config(command=button_click)

window.mainloop()
