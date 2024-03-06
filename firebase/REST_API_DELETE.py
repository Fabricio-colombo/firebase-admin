import requests
import json

link = 'https://fir-with-python-84d06-default-rtdb.firebaseio.com/'

def delete():
    # Deletar uma venda (DELETE)
    requisicao = requests.delete(f'{link}/Vendas/{id_alon}/.json')
    print(requisicao)
    print(requisicao.text)