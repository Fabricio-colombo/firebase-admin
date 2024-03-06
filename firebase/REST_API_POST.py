import requests
import json

link = 'https://fir-with-python-84d06-default-rtdb.firebaseio.com/'

def venda():
    # Criar uma venda (POST)
    cliente = 'robertinho'
    preco = 150
    produto = 'SSD SATA'
    
    dados = {'cliente': cliente,
            'preco': preco,
            'produto': produto}
    
    requisicao = requests.post(f'{link}/Vendas/{produto}/.json', data=json.dumps(dados))
    print(requisicao)
    print(requisicao.text)


def produto():
    # Criar um novo produto (POST)
    
    nome_produto = 'CPU i5 IntelCore'
    preco = 660
    quantidade = 30
    
    dados = {'nome': nome_produto,
            'preco': preco,
            'quantidade': quantidade}
    
    requisicao = requests.post(f'{link}/Produtos/{nome_produto}/.json', data=json.dumps(dados))
    print(requisicao)
    print(requisicao.text)
    
    
#venda()
#produto()