import tkinter as tk
from tkinter import filedialog
from Principal import principal


window = tk.Tk()
window.title("MapMarker - MM")
window.attributes('-zoomed', True)
window.configure(bg="#FFFFFF")

label = tk.Label(window, text="Por favor, selecione o arquivo que você quer ler")
label.pack()

button = tk.Button(window, text="Arquivo", bg='white')
button.pack()

def button_click():
    file_path = filedialog.askopenfilename(
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    principal(fileName=file_path, maps='https://www.google.com/maps/d/u/0/edit?mid=19Af8BUv6WDvFGncBjN45gxDzWUKGeKI&usp=sharing')


button.config(command=button_click)

window.mainloop()
