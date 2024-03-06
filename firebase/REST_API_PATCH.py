import requests
import json

link = 'https://fir-with-python-84d06-default-rtdb.firebaseio.com/'

def venda():
    # Editar a venda (PATCH)
    dados = {'cliente': 'lira'}
    requisicao = requests.patch(f'{link}/Vendas/-MyJSm_N0S8KhCc3nAku/.json', data=json.dumps(dados))
    print(requisicao)
    print(requisicao.text)