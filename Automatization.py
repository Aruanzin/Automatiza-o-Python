import time
import pyautogui as py
import pandas as pd

py.sleep(0.8)
a = 298
b = 300
py.hotkey("alt", "tab")

# Read the Excel file into a pandas dataframe
df = pd.read_excel('data2.xlsx')

# Group the data by the first four columns
Sigla = 'Endereço-ID'
dados = ['Cidade', 'Logradouro', 'FORNECEDOR', 'TIPO']
localizacao = ['Latitude', 'Longitude']
# Iterate over each group and concatenate the row values
for index, row in df.iterrows():
    sigla = row[Sigla]
    conteudo = ' '.join(row[dados])
    locationArray = [str (item) for item in row[localizacao] ]
    loc = ' '.join(locationArray)

    time.sleep(0.4)
    py.click(x = 405, y = 112)
    time.sleep(0.4)
    py.write(loc)
    time.sleep(0.4)
    py.press('enter')
    time.sleep(0.4)
    py.click(x = a, y = b)
    py.press('enter')
    py.write(sigla)
    time.sleep(0.4)
    py.press('tab')
    py.write(conteudo)
    py.write(loc)
    py.press('enter')
    time.sleep(0.4)
    py.scroll(30000, 183, 403)
    time.sleep(0.4)

