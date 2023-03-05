import tkinter as tk
from tkinter import END, filedialog
from Principal import principal

def fileFinder():
    filePath = filedialog.askopenfilename()
    return filePath

def on_focus_in(event):
    if entry.get() == 'Link do mapa':
        entry.delete(0, END)
        entry.config(fg='black')

def on_focus_out(event):
    if entry.get() == '':
        entry.insert(0, 'Link do mapa')
        entry.config(fg='gray')

def get_map_link(fileName, map):
    if map.startswith("https://www.google.com/maps/"):
        try:
            principal(fileName=fileName, map=map)
        except Exception as e:
            print(e)
    else:
        label.config(text="Link incorreto: o link do mapa deve começar com https://www.google.com/maps/")

window = tk.Tk()
window.title("MapMarker - MM")
window.configure(bg="#FFFFFF")

label = tk.Label(window, text="Por favor, selecione o arquivo que você quer ler", font=('helvetica', 10, 'bold'), bg='white', pady=20)
label.pack()

entry = tk.Entry(window, width=90, relief='flat')
entry.pack(padx=20, pady=50)

entry.insert(0, 'Link do mapa')
entry.bind('<FocusIn>', on_focus_in)
entry.bind('<FocusOut>', on_focus_out)

run = tk.Button(window, text="Rodar", bg='brown', fg='white', font=('helvetica', 12, 'bold'),width=10, relief="flat")
run.pack()

try:
    run.config(command=lambda: get_map_link(fileName=fileFinder(), map=str(entry.get())))
except ValueError as e:
    label.config(text=str(e))

window.mainloop()
