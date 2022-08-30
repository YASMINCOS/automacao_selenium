from dataclasses import dataclass
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)

#driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")

#sleep(3)
#driver.maximize_window()

#driver.find_element(By.ID,'btn-buy').click()


driver.get("https://www.imdb.com/")

driver.find_elements(By.NAME,"q")[0].send_keys("Titanic")

sleep(4)

driver.find_element(By.ID,"suggestion-search-button").click()