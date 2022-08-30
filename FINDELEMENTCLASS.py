from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)
#codigo padrao
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

sleep(3)

dados0=driver.find_element(By.CLASS_NAME,'value').text 

dados1=driver.find_elements(By.CLASS_NAME,'value')[0].text

dados2=driver.find_elements(By.CLASS_NAME,'value')[3].text

dados3=driver.find_elements(By.CLASS_NAME,'value')[4].text



print(dados0)
print(dados1)
print(dados2)
print(dados3)