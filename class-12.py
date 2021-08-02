import requests

status = None
texto = None

# GET

# try: 
#   requisicao = requests.get('https://putsreq.com/ig5noMH0kL6O2Hi2mxjq')
#   status = requisicao.status_code
#   texto = requisicao.text
# except:
#   print("Deu ruim")

# POST

cabecalho = { 'User-agent': 'Windows 12', 'CF_IPcountry': 'US' }
body = { 'ultima-visita': '10-10-2020' }

try: 
  requisicao = requests.post('https://putsreq.com/ig5noMH0kL6O2Hi2mxjq', headers=cabecalho, data=body)
  status = requisicao.status_code
  texto = requisicao.text
except:
  print("Deu ruim")

print (texto)
print (status)
