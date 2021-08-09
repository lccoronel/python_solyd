import requests
import json

# Cotacao
requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL') 

cotacao = json.loads(requisicao.text)

print('### COTAÇÃO ###')
print(cotacao['USDBRL']['bid'])

# Tempo
cidade = input('Escreva sua cidade: ')

response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=4f0302c8e731a3a878e7033adf44457b')

json_response = json.loads(response.text)
print(json_response)
