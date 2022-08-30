from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
 
driver = webdriver.Chrome(r"C:\Users\tiyas\Documents\Driver\chromedriver.exe")
 
driver.get("https://www.infomoney.com.br/")
 
sleep(2)
 
dados1 = driver.find_element(By.ID,"high").text
 
print(dados1)
dados2 = driver.find_elements(By.ID,"high")[0].text
print(dados2)
#print("-----")