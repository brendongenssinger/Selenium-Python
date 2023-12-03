import re
import requests


import requests



def extrair_urls(resposta_pagina_destino):
    # Regex para encontrar URLs em uma string HTML
    regex_url = r'https?://[^\s<>"]+|www\.[^\s<>"]+'

    # Encontrar todas as correspondências usando a regex
    urls = re.findall(regex_url, resposta_pagina_destino.text)
    nome_arquivo = 'urls_encontradas.txt'
    with open(nome_arquivo, 'w') as arquivo:
        for url in urls:
            arquivo.write(url + '\n')    



url = "https://anclivepa.blackboard.com/"
url_pagina_destino = "https://anclivepa.blackboard.com/ultra/courses/_25_1/outline"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "AWSELB=87F363D308BA5B4E4D473B7FF97E031F4C5818550317237A5674AB2A0A11CBD00FFFB25B19E2F601A1E20EAE677957C1443DC2BD0FDECE8EAA93248DD3FBC186CA48417C1F; AWSELBCORS=87F363D308BA5B4E4D473B7FF97E031F4C5818550317237A5674AB2A0A11CBD00FFFB25B19E2F601A1E20EAE677957C1443DC2BD0FDECE8EAA93248DD3FBC186CA48417C1F; BbClientCalenderTimeZone=America/Sao_Paulo; JSESSIONID=123A62B4BF0CFD67AA03F756675E6485; COOKIE_CONSENT_ACCEPTED=true; BbRouter=expires:1701553585,id:EC8596F36971D0EDB81C3BD6B29AD0FA,signature:b1626d5019c6afb5722d59e30b7e6a4a2da307c96b1c81127a47a22852fdc541,site:053a4967-7711-406c-ad4e-ddc59c95a8e3,v:2,xsrf:c6bb8d3d-ac73-4639-b3b8-0261cec50b2c",
    "Origin": "https://anclivepa.blackboard.com",
    "Referer": "https://anclivepa.blackboard.com/?new_loc=%2Fultra%2Fcourse",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}

# Dados de login
login_data = {
    "user_id": "7861",
    "password": "01234637189",
    "login": "Fazer login",
    "action": "login",
    "new_loc": "%2Fultra%2Fcourse",
    "blackboard.platform.security.NonceUtil.nonce.ajax": "c6bb8d3d-ac73-4639-b3b8-0261cec50b2c"
}

# Criar uma sessão
sessao = requests.Session()

# Realizar a requisição POST
resposta_login = sessao.post(url, headers=headers, data=login_data)

# Verificar a resposta
if resposta_login.status_code == 200:    
    resposta_pagina_destino = sessao.get("https://anclivepa.blackboard.com/telemetry/api/v1/browser/interactionshttps://anclivepa.blackboard.com/telemetry/api/v1/browser/interactions")
    resposta_pagina_destino = sessao.get("https://anclivepa.blackboard.com/ultra/courses/_25_1/outline")
    if(resposta_pagina_destino.status_code==200):
        extrair_urls(resposta_pagina_destino)
    else:
        print(f"Não foi possível acessar o login")    
    print("Login bem-sucedido!")        
    # Você pode continuar a interagir com a sessão autenticada aqui
else:
    print(f"Falha no login. Código de status: {resposta_login.status_code}")




