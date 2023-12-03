from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time
import re
from vimeo_downloader import Vimeo


# def extrair_urls(resposta_pagina_destino):
#     # Regex para encontrar URLs em uma string HTML
#     regex_url = r'https?://[^\s<>"]+|www\.[^\s<>"]+'

#     # Encontrar todas as correspondências usando a regex
#     urls = re.findall(regex_url, resposta_pagina_destino)
#     nome_arquivo = 'urls_encontradas.txt'
#     with open(nome_arquivo, 'w') as arquivo:
#         for url in urls:
#             arquivo.write(url + '\n')   
# # URL de login
# url_login = "https://anclivepa.blackboard.com/webapps/login/"

# # URL da página após o login
# url_pagina_destino = "https://anclivepa.blackboard.com/ultra/courses/_25_1/outline"

# # Dados de login
# usuario = "7861"
# senha = "01234637189"

# # Configurando o Chrome WebDriver
# chrome_options = webdriver.ChromeOptions()
# # Você pode adicionar opções específicas do Chrome aqui, se necessário

# # Criando uma instância do navegador Chrome
# driver = webdriver.Chrome(options=chrome_options)

# # Fazendo login
# driver.get(url_login)
# time.sleep(2)  # Espere um pouco para garantir que a página tenha carregado completamente

# # Encontrar os campos de login e senha e preenchê-los
# campo_usuario = driver.find_element("name", "user_id")
# campo_senha = driver.find_element("name", "password")

# campo_usuario.send_keys(usuario)
# campo_senha.send_keys(senha)

# # Enviar o formulário de login
# campo_senha.send_keys(Keys.RETURN)

# # Aguarde o redirecionamento ou carregamento após o login
# time.sleep(10)  # Ajuste conforme necessário

# driver.get(url_pagina_destino)


def downloadVideo(driver, xpath1:str,xpath2:str,xpathIframe:str):

    botaoExpandirbotaoExpandir = driver.find_element(By.XPATH,xpath1)
        #"//*[@id=\"learning-module-title-_9163_1\"]")
    botaoExpandirbotaoExpandir.click()
    
    time.sleep(2)

    botaoExpandirbotaoExpandir = driver.find_element(By.XPATH,xpath2)
        #"//*[@id=\"learning-module-contents-_9163_1\"]/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/a")
    botaoExpandirbotaoExpandir.click()

    time.sleep(2)
    
    iframe_src  = driver.find_element(By.XPATH,xpathIframe).get_attribute("src")
        #"//*[@id=\"bbml-editor-id_af22dded-b55f-4dfa-8a57-498e321cd5fe-rte\"]/div/div/iframe").get_attribute("src")


    print(f"Src do iframe: {iframe_src}")

    # url: https://vimeo.com/79761619
    # video ID: '79761619'
    ultimo_numero = re.search(r'/(\d+)$', iframe_src).group(1)

    v = Vimeo.from_video_id(video_id=ultimo_numero)# url: https://vimeo.com/79761619
    v.best_stream.download('D:\\VideosRodrigo\\')

    # Fechar o navegador
    driver.quit()
