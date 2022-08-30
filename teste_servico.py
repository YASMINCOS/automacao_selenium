##entrar no vscode
##instalar o python, isso pode ser feito na microsoft store. Procure a versão mais recente
# instale o selenium dessa maneira, no proprio terminal no vscode:
#pip install selenium#
#nao sera necessario instalar o webdriver, pois foi automatizado para buscra a versao mais recente.

#essa importacoes sao da biblioteca do selenium, nao se preocupem. Pode apenas copiar e colar o codigo agora e realizar as alteracoes, como seu e-mail e senha.
from dataclasses import dataclass
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome
 
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
 
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)
 
 
 
driver.get("https://digiteam.zendesk.com/access/unauthenticated?return_to=https%3A%2F%2Fdigiteam.zendesk.com%2Fagent%2Fdashboard")
 
sleep(3)
driver.maximize_window()
 
tagiframes = driver.find_element(By.TAG_NAME, "iframe")
 
driver.switch_to.frame(tagiframes)
 
Logar=driver.find_element(By.ID,"user_email")
 #insira o seu email no campo "send_keys, dentro das aspas"
Logar.send_keys("")
 
sleep(4)
 
 #insira a senha no campo "send_keys, dentro das aspas"
InserirSenha=driver.find_element(By.ID,"user_password").send_keys("")
 
driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[3]/div[1]/form/input[9]").click()



clicar_online=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/header/div[2]/div/div/div[2]/div[3]/div[1]").click
online=driver.find_element(By.CLASS_NAME,"StyledButton-sc-qe3ace-0 LRal LRbs LRbt LRbu LRdn LRdo LRdp LRbv LRdq LRdr StyledIconButton-sc-1t0ughp-0 mFLpu").click

 