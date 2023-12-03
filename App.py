## app.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time
import re
from vimeo_downloader import Vimeo
from seleniumPython import downloadVideo

print('Acess .... ')

# URL de login
url_login = "https://anclivepa.blackboard.com/webapps/login/"

# URL da página após o login
url_pagina_destino = "https://anclivepa.blackboard.com/ultra/courses/_25_1/outline"

# Dados de login
usuario = "7861"
senha = "01234637189"

# Configurando o Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
# Você pode adicionar opções específicas do Chrome aqui, se necessário

# Criando uma instância do navegador Chrome
driver = webdriver.Chrome(options=chrome_options)

# Fazendo login
driver.get(url_login)
time.sleep(2)  # Espere um pouco para garantir que a página tenha carregado completamente

# Encontrar os campos de login e senha e preenchê-los
campo_usuario = driver.find_element("name", "user_id")
campo_senha = driver.find_element("name", "password")

campo_usuario.send_keys(usuario)
campo_senha.send_keys(senha)

# Enviar o formulário de login
campo_senha.send_keys(Keys.RETURN)

# Aguarde o redirecionamento ou carregamento após o login
time.sleep(10)  # Ajuste conforme necessário

driver.get(url_pagina_destino)

#Acesso ao Abdome

downloadVideo(driver,"//*[@id=\"learning-module-title-_9163_1\"]"
              ,"//*[@id=\"learning-module-contents-_9163_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_af22dded-b55f-4dfa-8a57-498e321cd5fe-rte\"]/div/div/iframe")


downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_9163_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_0d202337-04f3-463a-b83a-894d1150aed0-rte\"]/div/div/iframe")

#Cirurgias Reconstrutivas

downloadVideo(driver,"//*[@id=\"learning-module-title-_2123_1\"]"
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_30914d20-70d5-4026-bfd1-71137cfd453d-rte\"]/div/div/iframe")

downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")

downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_35549d44-7eb7-469d-86b1-74d1948c0eeb-rte\"]/div/div/iframe")


downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_6d24f468-dc3d-4266-813b-bce1c91c89ff-rte\"]/div/div/iframe")


# Praticas- suturas, anatomia e paramentação
downloadVideo(driver,"//*[@id=\"learning-module-title-_2033_1\"]"
              ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_aa42f3db-4f29-4e84-8a4a-2bf402538140-rte\"]/div/div/iframe")

downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_e419e66f-ca86-4599-a7e4-3e8904d4fcfb-rte\"]/div/div/iframe")

downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_8263c6e1-ad1d-4cd3-b274-7e9511a4edad-rte\"]/div/div/iframe")

#Anatomia tórax
downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2033_1\"]/div/div[1]/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_beb429be-fe9b-46ad-9f21-095cb446a3c7-rte\"]/div/div/iframe")

#downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")
#downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")
#downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")
#downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")
#downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")
#downloadVideo(driver,""
              ,"//*[@id=\"learning-module-contents-_2123_1\"]/div/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/a"
              ,"//*[@id=\"bbml-editor-id_fd273e96-90aa-480d-83e1-17ab4261f001-rte\"]/div/div/iframe")



# Fechar o navegador
driver.quit()