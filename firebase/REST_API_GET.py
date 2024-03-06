import requests
import json

link = 'https://fir-with-python-84d06-default-rtdb.firebaseio.com/'

def get():
    # Pegar uma venda específico ou todas as vendas (GET)
    requisicao = requests.get(f'{link}/Vendas/.json')
    print(requisicao)
    dic_requisicao = requisicao.json()
    id_alon = None
    for id_venda in dic_requisicao:
        cliente = dic_requisicao[id_venda]['cliente']
        if cliente == "alon":
            print(id_venda)
            id_alon = id_venda