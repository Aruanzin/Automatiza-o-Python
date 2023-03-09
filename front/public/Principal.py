import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def principal(listaSigla, listaDesc, listaLoc, map):
    # Iterate over each group and concatenate the row values
    
    print(map)
    options = uc.ChromeOptions()
    profile = "C:\\Users\\Usuario\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
    options.user_data_dir = profile
    driver = uc.Chrome(options=options, use_subprocess=True)
    driver.get(map)
    
    try:
        driver.find_element(By.XPATH, '//*[@id="gb_70"]')
        driver.execute_script('alert("Por favor, logue no MyMaps")')
    except NoSuchElementException:
        print('logado')
    finally:
        wait = WebDriverWait(driver,10)

        barraPesquisa = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-field"]')))
        barraPesquisa = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-field"]')))
        botaoPesquisar = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mapsprosearch-button"]/div')))


        for sigla, conteudo, loc in zip(listaSigla, listaDesc, listaLoc):
            barraPesquisa.send_keys(loc)
            botaoPesquisar.click()

            try:
                greenPoint = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchresultsview"]/div/div/div[2]/div/div/div[3]')))
                driver.execute_script("arguments[0].click()",greenPoint)
                edit = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-edit-button"]')))
                driver.execute_script("arguments[0].click()",edit)

                espacoSigla = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-attr-nome-value"]')))
                try:
                    espacoSigla.clear()
                except Exception as e:
                    print(sigla, e)
                espacoSigla.send_keys(sigla)
                espacoDesc = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-attr-descrição-value"]')))
                espacoDesc.send_keys(conteudo + " " + loc)
                salvar = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-infowindow-done-editing-button"]/div')))
                driver.execute_script("arguments[0].click()",salvar)
            except TimeoutException:
                driver.close()
    
    #//*[@id="map-title-desc-bar"]/div[3]/div[2]/div[4]/div

    while True:
        elemento =  wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="map-title-desc-bar"]/div[3]/div[2]/div[3]/div')))
        if elemento.is_displayed():
            # o elemento está visível na página
            driver.quit()
            break
        else:
            print('elemento não está visivel')
            time.sleep(3)
            continue
        # o elemento não está visível na página

    # fechar o navegador
    
    # time.sleep(1000)