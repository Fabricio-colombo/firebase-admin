import requests
import json

link = 'https://fir-with-python-84d06-default-rtdb.firebaseio.com/'

def venda():
    nome_cliente = 'José tavares'
    preco = 150
    produto = 'TECLADO'

    dados_venda = {'cliente': nome_cliente,
                   'preco': preco,
                   'produto': produto}

    produtos_response = requests.get(f'{link}/Produtos/{produto}/.json')

    if produtos_response.status_code == 200:
        produto_info = produtos_response.json()
        if produto_info:
            quantidade_atual = produto_info.get('quantidade', 0)
            if quantidade_atual > 0:
                nova_quantidade = quantidade_atual - 1
                dados_atualizados = {'nome': produto_info.get('nome', ''),
                                     'preco': produto_info.get('preco', 0),
                                     'quantidade': nova_quantidade}
                requests.put(f'{link}/Produtos/{produto}/.json', data=json.dumps(dados_atualizados))
            else:
                print("Produto fora de estoque.")
                return
        else:
            print("Produto não encontrado.")
            return
    else:
        print(f"Erro ao obter produtos: {produtos_response.status_code} - {produtos_response.text}")
        return

    requisicao = requests.post(f'{link}/Vendas/{produto}/.json', data=json.dumps(dados_venda))
    print(requisicao)
    print(requisicao.text)

venda()
