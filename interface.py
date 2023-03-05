import tkinter as tk
from tkinter import END, filedialog
from Principal import principal

def fileFinder():
    filePath = filedialog.askopenfilename()
    return filePath

def animate_dot(label):
    label['text'] += '.'
    if len(label['text']) > 3:
        label['text'] = 'Loading'
    label.after(500, animate_dot, label)

def get_map_link(fileName, map):
    if map.startswith("https://www.google.com/maps/"):
        try:
            print(fileName)
            principal(fileName=fileName, map=map)
            label.config(text='Loading')
            animate_dot(label=label)
        except Exception as e:
            print(e)
    else:
        label.config(text="Link incorreto: o link do mapa deve começar com https://www.google.com/maps/")

window = tk.Tk()
window.title("MapMarker - MM")
window.configure(bg="#FFFFFF")

label = tk.Label(window, text="Por favor, selecione o arquivo que você quer ler", font=('helvetica', 10, 'bold'), bg='white', pady=20)
label.pack()

localizacaoLabel = tk.Label(window,bg='white',width=90, text="Localização:")
localizacaoLabel.pack(pady=20)

# Create an entry widget for the name input
localizacaoEntry = tk.Entry(window,width=50)
localizacaoEntry.pack()


tituloLabel = tk.Label(window,bg='white',width=90, text="Titulo da localização:")
tituloLabel.pack(pady=20)

# Create an entry widget for the name input
tituloEntry = tk.Entry(window,width=50)
tituloEntry.pack()

descricaoLabel = tk.Label(window,bg='white',width=90, text="Descricao da localização:")
descricaoLabel.pack(pady=20)

# Create an entry widget for the name input
linkEntry = tk.Entry(window,width=50)
linkEntry.pack()

linkLabel = tk.Label(window,bg='white',width=90, text="Link da mapa:")
linkLabel.pack(pady=20)

# Create an entry widget for the name input
linkEntry = tk.Entry(window,width=50 )
linkEntry.pack()

run = tk.Button(window, text="Rodar", bg='brown', fg='white', font=('helvetica', 12, 'bold'),width=42, relief="flat")
run.pack(pady=30, padx=25)



try:
    run.config(command=lambda: get_map_link(fileName=fileFinder(), map=str(linkEntry.get())))
except ValueError as e:
    label.config(text=str(e))

window.mainloop()
