from cgi import print_form
from dataclasses import dataclass
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)

driver.get("https://br.investing.com/commodities/crude-oil-historical-data")
#fechar pop


try:
    driver.find_element(By.ID,"onetrust-accept-btn-handler").click
except:
    print_form("Não existe alerta")
    
    
sleep(2)

try:
    driver.find_element(By.CSS_SELECTOR,"#PromoteSignUpPopUp > div.right > i").click
except:
    print("Não existe alerta")


driver.find_element(By.ID,"widgetFieldDateRange")


datainicial=driver.find_element(By.ID,"starDate")
datafim=driver.find_element(By.ID,"endDate")

datainicial.clear()
datafim.clear()

datainicial.send_keys("10/01/2020")
datafim.send_keys("10/01/2021")

driver.find_element(By.ID,"applyBtn").click()


dados=[]
dadosTabela=driver.find_element(By.ID,"curr_table")

for linha in dadosTabela.find_element(By.ID,"tr"):
    linhaDados=[]
    for coluna in linha.find_elements(By.TAG_NAME,"td"):
        linhaDados.append(coluna.text)
        dados.append(linhaDados)
        
        
df=pd.DataFrame(dados)
df=df.iloc[1: , :]

df.columns=['Data','Ultimo','Abertura','Maxima','Minima','Vol','Var%']

print(df)


#salvar

df.to_csv("dadosOil.csv")