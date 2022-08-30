from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)
#codigo padrao
driver.get("https://imdb.com/title/tt0120338/?ref_=fn_alt_tt_1")

#desamixar a tela
driver.maximize_window()

driver.implicitly_wait(3)
#maximizar a tela
driver.minimize_window()
driver.implicitly_wait(3)
#seta de voltar
driver.get("https://empresas.americanas.com.br/")
driver.back()

#seta direita
driver.forward()

#atualizar
driver.refresh()

#fechar
driver.close()