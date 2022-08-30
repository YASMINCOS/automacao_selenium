from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)
driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

valoTabela=driver.find_elements (By.XPATH,'/html/body/main/div[2]/div[8]/div/div[6]/div/div[2]/table/tbody/tr[3]/td[2]')[0].text

proventos=driver.find_elements(By.XPATH,'/html/body/main/div[2]/div[8]/div/div[6]/div/div[1]/div[1]')[0].text


print(valoTabela)
print(proventos)