from dataclasses import dataclass
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)


driver.get("https://oplab.app/login")
sleep(3)# seconds
 
formulario = driver.find_element(By.TAG_NAME,"form")
 
email = formulario.find_element(By.NAME,"email")

email.send_keys("teste")