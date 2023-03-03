import undetected_chromedriver as uc
import time

driver = uc.Chrome(version_main=94)

driver.get('https://nowsecure.nl')  # my own test test site with max anti-bot protection

time.sleep(300)