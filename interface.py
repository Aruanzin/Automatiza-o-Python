import tkinter as tk
from tkinter import END, filedialog
from manipulaçãoExcel import leArquivo
from ttkthemes import ThemedTk


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
        # leArquivo(fileName=fileName, map=map)
        try:
            print(fileName)
            leArquivo(fileName=fileName, map=map)
            label.config(text='Loading')
            animate_dot(label=label)
        except Exception as e:
            label.config(text=e)
    else:
        label.config(text="Link incorreto: o link do mapa deve começar com https://www.google.com/maps/")
def add_value(frame,values,entry):
    value = entry.get()
    if value:
        newFrame = tk.Frame(frame)
        newFrame.pack()
        
        newEntry = tk.Entry(newFrame,width=50)
        newEntry.insert(tk.END, value)
        newEntry.pack(side=tk.LEFT)
        button = tk.Button(newFrame, text="Remove Value")
        button.pack(side=tk.RIGHT)
        values.append(value)
        entry.delete(0, tk.END)
        print("Values:", values)

window = ThemedTk(theme="arc")
window.title("MapMarker - MM")
window.configure(bg="#FFFFFF")

row = 0

label = tk.Label(window, text="Por favor, selecione o arquivo que você quer ler", font=('helvetica', 10, 'bold'), bg='white', pady=20)
label.pack()
row +=1

localizacaoLabel = tk.Label(window,bg='white',width=90, text="Localização:")
localizacaoLabel.pack(pady=20)
row +=1

# Create an entry widget for the name input
localizacaoEntry = tk.Entry(window,width=50)
localizacaoEntry.pack()
row +=1


tituloLabel = tk.Label(window,bg='white',width=90, text="Titulo da localização:")
tituloLabel.pack(pady=20)
row +=1

# Create an entry widget for the name input
titulos=[]
tituloFrame = tk.Frame(window)
tituloFrame.pack()

tituloAdd = tk.Frame(tituloFrame)
tituloAdd.pack()
tituloEntry = tk.Entry(tituloAdd,width=50)
tituloEntry.pack(side=tk.LEFT)
button = tk.Button(tituloAdd, text="Add Value", command=lambda: add_value(tituloFrame,titulos, tituloEntry))
button.pack(side=tk.RIGHT)
row+=1


descricaoLabel = tk.Label(window,bg='white',width=90, text="Descricao da localização:")
descricaoLabel.pack(pady=20)
row+=1

# Create an entry widget for the name input
linkEntry = tk.Entry(window,width=50)
linkEntry.pack()
row+=1

linkLabel = tk.Label(window,bg='white',width=90, text="Link da mapa:")
linkLabel.pack(pady=20)
row+=1

# Create an entry widget for the name input
linkEntry = tk.Entry(window,width=50 )
linkEntry.pack()
row+=1

run = tk.Button(window, text="Rodar", bg='brown', fg='white', font=('helvetica', 12, 'bold'),width=42, relief="flat")
run.pack(pady=30, padx=25)
row+=1



try:
    run.config(command=lambda: get_map_link(fileName=fileFinder(), map=str(linkEntry.get())))
except ValueError as e:
    label.config(text=str(e))

window.mainloop()
