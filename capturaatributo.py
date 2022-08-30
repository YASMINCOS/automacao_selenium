from dataclasses import dataclass
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)

driver.get("https://statusinvest.com.br/fundos-imombiliarios/knri11")

elementoImagem=driver.find_elements(By.CLASS_NAME,'navbar-brand')[0]
elementoImg=elementoImagem.find_element(By.TAG_NAME,"img")
atributosrc=elementoImg.get_atribute("src")

print(atributosrc)
