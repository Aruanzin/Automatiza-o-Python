import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

wait = WebDriverWait(driver,10)
#barraPesquisa = driver.find_element("id", "mapsprosearch-field")
#botaoPesquisar = driver.find_element("id", "mapsprosearch-button")

barraPesquisa = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-field"]')))
botaoPesquisar = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-button"]/div')))


for index, row in df.iterrows():
    sigla = row[Sigla]
    conteudo = ' '.join(row[dados])
    locationArray = [str (item) for item in row[localizacao] ]
    loc = ' '.join(locationArray)
    barraPesquisa.send_keys(loc)
    botaoPesquisar.click()

    greenPoint = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchresultsview"]/div/div/div[2]/div/div/div[3]')))
    driver.execute_script("arguments[0].click()",greenPoint)
    edit = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-edit-button"]')))
    driver.execute_script("arguments[0].click()",edit)
    espacoSigla = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-attr-nome-value"]')))
    espacoSigla.send_keys(sigla)
    espacoDesc = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-attr-descrição-value"]')))
    espacoDesc.send_keys(conteudo + " " + loc)
    salvar = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-done-editing-button"]/div')))
    driver.execute_script("arguments[0].click()",salvar)



    
time.sleep(1000)