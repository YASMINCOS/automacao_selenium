from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

sleep(3)

Nome=driver.find_elements(By.TAG_NAME,'h1')[0].text 

ValorAtual=driver.find_elements(By.TAG_NAME,'strong')[0].text

Tabelarendimentos=driver.find_elements(By.TAG_NAME,'table')[0].text

TabelaResultados=driver.find_elements(By.TAG_NAME,'table')[1].text



print(Nome)
print(ValorAtual)
print(Tabelarendimentos)
print(TabelaResultados)