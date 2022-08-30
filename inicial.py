from lib2to3.pgen2 import driver
from selenium import webdriver 


driver = webdriver.Chrome(executable_path=r"C:\Users\tiyas\Documents\chromedriver.exe")
driver= webdriver.Chrome()


driver.get("https://www.google.com.br")