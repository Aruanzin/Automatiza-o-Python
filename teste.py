import time
import pandas as pd
import undetected_chromedriver as uc


a = 301
b = 302
# Read the Excel file into a pandas dataframe
df = pd.read_excel('data.xlsx')

# Group the data by the first four columns
Sigla = 'Endereço-ID'
dados = ['Cidade', 'Logradouro', 'FORNECEDOR', 'TIPO']
localizacao = ['Latitude', 'Longitude']
# Iterate over each group and concatenate the row values
options = uc.ChromeOptions()
profile = "C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.user_data_dir = profile
driver = uc.Chrome(options=options, use_subprocess=True)
driver.get('https://www.google.com/maps/d/u/0/edit?mid=19Af8BUv6WDvFGncBjN45gxDzWUKGeKI&usp=sharing')


barraPesquisa = driver.find_element("id", "mapsprosearch-field")
botaoPesquisar = driver.find_element("id", "mapsprosearch-button")


for index, row in df.iterrows():
    sigla = row[Sigla]
    conteudo = ' '.join(row[dados])
    locationArray = [str (item) for item in row[localizacao] ]
    loc = ' '.join(locationArray)
    barraPesquisa.send_keys(loc + "\n")
    time.sleep(0.3)
    greenPoint = driver.find_element("class", "un1lmc-pbTTYe-ibnC6b JIbV8-pbTTYe-ibnC6b-G0jgYd JIbV8-pbTTYe-ibnC6b-gk6SMd")
    greenPoint.click()
    time.sleep(0.5)
    addToMap = driver.find_element("id", "addtomap-button")
    addToMap.click()

    #edit = driver.find_element("id", "map-infowindow-edit-button")
    #espacoSigla = driver.find_element("id", "map-infowindow-attr-nome-value")
    #espacoDesc = driver.find_element("id", "map-infowindow-attr-descrição-value")



    
    




time.sleep(1000)