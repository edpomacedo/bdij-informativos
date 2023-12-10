import requests
from requests_oauthlib import OAuth1
from config import MEDIAWIKI_CONFIG

def testar_conexao():
    # Utilizando as credenciais do arquivo de configuração
    consumer_key = MEDIAWIKI_CONFIG['consumer_key']
    consumer_secret = MEDIAWIKI_CONFIG['consumer_secret']
    access_token = MEDIAWIKI_CONFIG['access_token']
    access_token_secret = MEDIAWIKI_CONFIG['access_token_secret']

    # Configuração do cliente OAuth1
    oauth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    # URL para a API de consulta de usuário do MediaWiki
    api_user_info_url = MEDIAWIKI_CONFIG['api_edit_url'] + '?action=query&meta=userinfo&format=json'

    # Requisição para obter informações do usuário
    response = requests.get(url=api_user_info_url, auth=oauth)

    # Verificar o status da resposta
    if response.status_code == 200:
        print('Conexão bem-sucedida. Informações do usuário:')
        print(response.json())
    else:
        print(f'Erro na conexão: {response.text}')

if __name__ == "__main__":
    testar_conexao()