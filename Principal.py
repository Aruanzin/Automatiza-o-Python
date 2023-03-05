import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def principal(fileName, map):
    # Read the Excel file into a pandas dataframe
    print(map)
    df = pd.read_excel(fileName)

    # Group the data by the first four columns
    Sigla = 'Endereço-ID'
    dados = ['Cidade', 'Logradouro', 'FORNECEDOR', 'TIPO']
    localizacao = ['Latitude', 'Longitude']
    # Iterate over each group and concatenate the row values
    options = uc.ChromeOptions()
    profile = "C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
    options.user_data_dir = profile
    driver = uc.Chrome(options=options, use_subprocess=True)
    driver.get(map)
    try:
        driver.find_element(By.XPATH, '//*[@id="gb_70"]')
        driver.execute_script('alert("Por favor, logue no MyMaps")')
    except NoSuchElementException:
        try:
            print('logado')
            wait = WebDriverWait(driver,10)

            barraPesquisa = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-field"]')))
            barraPesquisa = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-field"]')))
            botaoPesquisar = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-button"]/div')))


            for row in df.iterrows():
                sigla = row[Sigla]
                conteudo = ' '.join(row[dados])
                locationArray = [str (item) for item in row[localizacao] ]
                loc = ' '.join(locationArray)

                barraPesquisa.send_keys(loc)
                botaoPesquisar.click()

                try:
                    greenPoint = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchresultsview"]/div/div/div[2]/div/div/div[3]')))
                    driver.execute_script("arguments[0].click()",greenPoint)
                    edit = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-edit-button"]')))
                    driver.execute_script("arguments[0].click()",edit)

                    espacoSigla = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-attr-nome-value"]')))
                    espacoSigla.clear()
                    espacoSigla.send_keys(sigla)
                    espacoDesc = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-attr-descrição-value"]')))
                    espacoDesc.send_keys(conteudo + " " + loc)
                    salvar = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-done-editing-button"]/div')))
                    driver.execute_script("arguments[0].click()",salvar)
                except Exception as e:
                    print( e)
        except TimeoutException:
            driver.close()
        
    
    time.sleep(1000)