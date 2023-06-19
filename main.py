import time
import datetime
import os
import pyautogui as pg
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

datahora = datetime.now()
datahora1 = datahora.strftime('%H:%M:%S')

#pg.alert('Bot ira iniciar após pressionar OK!!!')
while True:
    datahora = datetime.now()
    datahora1 = datahora.strftime('%H:%M:%S')
    os.system('clear')
    #if datahora1 == str('13:53'):
    navegador.get('https://login.yahoo.com/account/create')
    #time.sleep(3)
    navegador.find_element('xpath', '//*[@id="usernamereg-firstName"]').send_keys('João')
    navegador.find_element('xpath', '//*[@id="usernamereg-lastName"]').send_keys('Plenário')
    #time.sleep(3)
    navegador.find_element('xpath', '//*[@id="usernamereg-userId"]').send_keys('joao.plenario171')
    #time.sleep(3)
    navegador.find_element('xpath', '//*[@id="usernamereg-password"]').send_keys('senhadefault1234')
    #time.sleep(3)
    navegador.find_element('xpath', '//*[@id="usernamereg-month"]').send_keys('Janeiro')
    navegador.find_element('xpath', '//*[@id="usernamereg-day"]').send_keys('01')
    navegador.find_element('xpath', '//*[@id="usernamereg-year"]').send_keys('1980')
    time.sleep(3)
    navegador.find_element('xpath', '//*[@id="reg-submit-button"]').click()
    time.sleep(10)
        #navegador.find_element('xpath', '//*[@id="marcarponto"]/div/div/div[2]/div/button[2]').click()
        #time.sleep(3)
#pg.alert('Bot finalizado')
