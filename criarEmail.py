from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from br_nome_gen import pessoa_random
from unidecode import unidecode

p = pessoa_random()
senha = 'SENHA'

pessoa = p.nome
pessoa2 = unidecode(pessoa.replace(' ',''))
email = pessoa2.lower()


option = Options()
option.headless = False
navegador = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))

navegador.get("https://mail.tutanota.com/login?noAutoLogin=true")

time.sleep(5)

navegador.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[3]/div/button/small').click()
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="login-view"]/div[2]/div/div[4]/div/div/div/button[1]/div/div').click()
time.sleep(5)


#Escolha do plano
navegador.execute_script("document.getElementsByClassName('button-content flex items-center login plr-button justify-center')[0].click()")
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[1]/div/input').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[2]/div/input').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[3]/button[2]/div/div').click()


#Nome e sobrenome
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[1]/div/div/div/div[1]/input').send_keys(email)
time.sleep(5)

navegador.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[2]/div[1]/div/div/div/div[1]/input').send_keys(senha)
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[3]/div/input').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[4]/div/input').click()
time.sleep(2)
navegador.execute_script("document.getElementsByClassName('button-content flex items-center login plr-button justify-center')[0].click()")

print('Email criado\n Email: {}@tutanota.com\nSenha: {}'.format(email,senha))
time.sleep(60)





