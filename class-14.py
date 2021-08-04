import re

string_de_teste = 'O gato é bonito e a gata tambem, incluindo os gatinhos'

#padrao = re.search(r'gat.', string_de_teste) # qualquer caracter
#padrao = re.search(r'gat\w', string_de_teste) # uma letra
#padrao = re.findall(r'gat\w+', string_de_teste) # uma letra ou mais
#padrao = re.findall(r'[gat]', string_de_teste) # vai procurar por cada letra que esta dentro de colchetes
#padrao = re.findall(r'\w{3,4}', string_de_teste) # procura por palavras que tenham de 3 a 4 letras
padrao = re.findall(r'gat[ao]{1}', string_de_teste) 

if padrao:
  print(padrao)
else:
  print('nao achou nada')

  re.search() #acha apena uma expressao
  re.findall() #acha varias expressoes