# chrome -> chromedriver
# firefox -> geckdriver
# instale 1 desses 2 na pasta onde está o python.exe na IDE utilizada

from selenium import webdriver
import time

nav = webdriver.Firefox()
nav.get("https://login.live.com/")
time.sleep(2) # aguarda 1 seg ate fazer o prox comando

nav.find_element_by_xpath('//*[@id="i0116"]').send_keys("<seu email>")
nav.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(2)

nav.find_element_by_xpath('//*[@id="i0118"]').send_keys("<sua senha>")
nav.find_element_by_xpath('//*[@id="idSIButton9"]').click()
# login feito com sucesso