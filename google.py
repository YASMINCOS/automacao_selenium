from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)
#codigo padrao
driver.get("https://google.com")

driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Imersao Alura")