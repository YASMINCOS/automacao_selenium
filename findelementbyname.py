from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)

driver.get("https://www.imdb.com/")

sleep(8)

campoBusca=driver.find_elements(By.NAME,"q")[0]
campoBusca.send_keys("Titanic")
