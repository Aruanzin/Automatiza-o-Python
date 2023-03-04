import tkinter as tk
from tkinter import filedialog
from Principal import principal

def fileFinder():
    filePath = filedialog.askopenfilename(
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    return filePath



window = tk.Tk()
window.title("MapMarker - MM")
window.configure(bg="#FFFFFF")

label = tk.Label(window, text="Por favor, selecione o arquivo que você quer ler")
label.pack()


entry = tk.Entry(window, width=90)
entry.pack()

file = tk.Button(window, text="Arquivo", bg='white')
file.pack()
file.config(command=fileFinder)

run = tk.Button(window, text="Rodas", bg='white')
run.pack()
run.config(command=lambda: principal(fileName=fileFinder(), map=str(entry.get())))
print(map)

window.mainloop()

