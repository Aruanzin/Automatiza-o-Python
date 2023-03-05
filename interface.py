import tkinter as tk
from tkinter import END, filedialog
from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSessionIdException
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


entry = tk.Entry(window, width=90, relief='flat')
entry.pack(padx=20, pady=50)

entry.insert(0, 'Link do mapa')
entry.bind('<FocusIn>', on_focus_in)
entry.bind('<FocusOut>', on_focus_out)

# fra
run = tk.Button(window, text="Rodar", bg='brown', fg='white', font=('helvetica', 12, 'bold'),width=10, relief="flat")
run.pack() 
# run.config(command=lambda: principal(fileName=fileFinder(), map=str(entry.get())))

try:
    run.config(command=lambda: principal(fileName=fileFinder(), map=str(entry.get())))
except TimeoutException:
    label.config(text="Site não encontrado")
except InvalidArgumentException:
    label.config(text="O link está incorreto")  
except InvalidSessionIdException:
    label.config(text="O link está incorreto")  
print(map)

window.mainloop()

