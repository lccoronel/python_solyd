import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL') 

cotacao = json.loads(requisicao.text)

print('### COTAÇÃO ###')
print(cotacao['USDBRL']['bid'])
