import tkinter as tk
from tkinter import END, filedialog
from manipulaçãoExcel import leArquivo
from ttkthemes import ThemedTk
import json

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

def create_widget(frame, type, value):
    newFrame = tk.Frame(frame )
    newFrame.pack(fill='both')
    newEntry = tk.Entry(newFrame)
    newEntry.insert(tk.END, value)
    newEntry.pack(side =tk.LEFT ,fill='both', expand=True)
    button = tk.Button(newFrame, text="Remove Value", command=lambda: remove_widget(newFrame,type=type, value=value))
    button.pack(side=tk.LEFT)

def remove_widget(widget,type, value):
    info[type].remove(value)
    widget.destroy()

def add_value(frame,type,entry):
    value = entry.get()
    if value:
        create_widget(frame,type,value)
        info[type].append(value)
        entry.delete(0, tk.END)
        print("Values:", info)

def recover_data(frame, type, value):
    create_widget(frame,type,value)
    print("Values:", info)


def write_data(data):
    with open('_data.json', 'w') as f:
    # Write the dictionary as a JSON object to the file
        json.dump(data, f)
    f.close()

def read_data():
    with open('_data.json', 'r') as f:
    # Load the data from the file
        data = json.load(f)
    if not data:
        data = {
            'localizacoes': [],
            'titulos': [],
            'descricao': []
        }
        write_data(data)
    f.close()
    return data

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        write_data(info)
        root.destroy()




root = tk.Tk()
root.title('MapMaker - MM', )

frame =tk.Frame(root,bg='red')
frame.pack(fill='both', expand=True)

canvas = tk.Canvas(frame, bg='black')
canvas.pack(side=tk.LEFT, fill='both', expand=True)

scrollbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

window = tk.Frame(canvas, bg='green')
canvas.create_window((0,0), window=window,anchor='nw')

info = read_data()


label = tk.Label(window, text="Por favor, selecione o arquivo que você quer ler", font=('helvetica', 10, 'bold'), bg='white', pady=20)
label.pack()

localizacaoLabel = tk.Label(window,bg='white', text="Localização:")
localizacaoLabel.pack(pady=20)

localizacoesFrame = tk.Frame(window)
localizacoesFrame.pack()


localizacoesAdd = tk.Frame(localizacoesFrame)
localizacoesAdd.pack(expand=True,fill='both')
localizacoesEntry = tk.Entry(localizacoesAdd, width=50)
localizacoesEntry.pack(side=tk.LEFT,fill='both',expand=True)
localizacoesButton = tk.Button(localizacoesAdd, text="Add Value", command=lambda: add_value(localizacoesFrame,'localizacoes', localizacoesEntry))
localizacoesButton.pack(side=tk.LEFT)

for loc in info['localizacoes']:
    recover_data(localizacoesFrame,'localizacoes', loc)

tituloLabel = tk.Label(window,bg='white',width=90 ,text="Titulo da localização:")
tituloLabel.pack(pady=20)
tituloFrame = tk.Frame(window)
tituloFrame.pack()

tituloAdd = tk.Frame(tituloFrame)
tituloAdd.pack()
tituloEntry = tk.Entry(tituloAdd,width=50)
tituloEntry.pack(side=tk.LEFT, expand=True, fill='both')
tituloButton = tk.Button(tituloAdd, text="Add Value", command=lambda: add_value(tituloFrame,'titulos', tituloEntry))
tituloButton.pack(side=tk.RIGHT)
print(info['titulos'])

for loc in info['titulos']:
    print(loc)
    recover_data(tituloFrame,'titulos', loc)

descricaoLabel = tk.Label(window,bg='white', text="Descrição:")
descricaoLabel.pack(pady=20)

descricaoFrame = tk.Frame(window)
descricaoFrame.pack()
descricaoAdd = tk.Frame(descricaoFrame)
descricaoAdd.pack()

descricaoEntry = tk.Entry(descricaoAdd,width=50)
descricaoEntry.pack(side=tk.LEFT, fill='both', expand=True)
descricaoButton = tk.Button(descricaoAdd, text="Add Value", command=lambda: add_value(descricaoFrame,'descricao', descricaoEntry))
descricaoButton.pack(side=tk.RIGHT)
for loc in info['descricao']:
    recover_data(descricaoFrame,'descricao', loc)
# Create an entry widget for the name input
linkLabel = tk.Label(window,bg='white', text="Link da mapa:")
linkLabel.pack(pady=20)
linkFrame = tk.Frame(window)
linkFrame.pack()

linkAdd = tk.Frame(linkFrame)
linkAdd.pack()
# Create an entry widget for the name input
linkEntry = tk.Entry(linkAdd,width=50 )
linkEntry.pack(expand=True, fill='both')

run = tk.Button(window, text="Rodar", bg='brown', fg='white', font=('helvetica', 12, 'bold'),width=42, relief="flat")
run.pack(pady=30, padx=25)



try:
    run.config(command=lambda: get_map_link(fileName=fileFinder(), map=str(linkEntry.get())))
except ValueError as e:
    label.config(text=str(e))

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
