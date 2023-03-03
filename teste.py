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
driver = uc.Chrome(user_data_dir=profile, use_subprocess=True)
driver.get('https://www.facebook.com/')

for index, row in df.iterrows():
    sigla = row[Sigla]
    conteudo = ' '.join(row[dados])
    locationArray = [str (item) for item in row[localizacao] ]
    loc = ' '.join(locationArray)




time.sleep(1000)