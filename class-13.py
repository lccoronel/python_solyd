import requests
import json

def get_user(user_selected):
  try:
    response = requests.get('https://api.github.com/users/' + user_selected)
    user = json.loads(response.text)
    return user
  except:
    print('Erro na requisicao')
    return None

left = False
while left == False:
  user = input('Digite um usuario: ')
  response = get_user(user)

  if user != '0':
    print(response['url'])
  elif user == '0':
    left = True
  else:
    print('usuario nao encontrado')

if left == True:
  print('Saindo...')
  exit()
