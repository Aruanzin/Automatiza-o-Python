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
        entry.insert(0, 'Enter your text here')
        entry.config(fg='gray')


window = tk.Tk()
window.title("MapMarker - MM")
window.configure(bg="#FFFFFF")


label = tk.Label(window, text="Por favor, selecione o arquivo que você quer ler", font=('helvetica', 10, 'bold'), bg='white', pady=20)
label.pack()


entry = tk.Entry(window, width=90  )
entry.pack()
entry.insert(0, 'Link do mapa')
entry.bind('<FocusIn>', on_focus_in)
entry.bind('<FocusOut>', on_focus_out)

# frame
buttonContainer = tk.Frame(window, relief = 'sunken',
              bd = 1, bg = 'white')
buttonContainer.pack(fill = 'both', expand = True,
           padx = 10, pady = 10)

run = tk.Button(buttonContainer, text="Rodar", bg='brown', fg='white', font=('helvetica', 12, 'bold'),pady=20 )
run.pack()
run.config(command=lambda: principal(fileName=fileFinder(), map=str(entry.get())))
print(map)

window.mainloop()

