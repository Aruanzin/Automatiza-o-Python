import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Firefox()
navegador.get('https://www.google.com/maps/d/u/0/edit?hl=pt-BR&mid=11Ur-K6OTHZEoa9i3-PO7P3mgQgMT3Lk&ll=-13.453169271686487%2C-51.925279499999995&z=4')

loginButton = navegador.find_element("id", "gb_70")

loginButton.click()


google_popup =  navegador.window_handles[1]
navegador.switch_to.window(google_popup)

Login = navegador.find_element("id", "identifierId")
Login.send_keys("AruanBretas15@gmail.com")
Login.send_keys(Keys.RETURN)



time.sleep(1000)