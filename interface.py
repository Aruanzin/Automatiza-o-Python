import tkinter as tk
from tkinter import filedialog


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
    print("Selected file:", file_path)


button.config(command=button_click)

window.mainloop()
