from lib2to3.pgen2 import driver
from time import sleep
from typing import KeysView
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico)

options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\tiyas\Documents\dadosDownload",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(chrome_options=options,executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.opera.com/pt-br/download")

spanBotao = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[1]/div/span")
linkBotao = spanBotao.find_element_by_tag_name("a")
linkBotao.click()



