minha_lista = ['gui', 'joao']
minha_tupla = ('gui', 'joao')
meu_dicionario = {'nome': 'Lucas', 'idade': 27}
meu_conjunto = {'gui', 'biel'}

for valores in meu_dicionario.keys(): 
  print(valores)

for valores in meu_dicionario.values(): 
  print(valores)

meu_dicionario['telefone'] = '11979569018'
print(meu_dicionario)



meu_conjunto.add('Maria')
print(meu_conjunto)

if 'Maria' in meu_conjunto:
  print('Maria esta no conjunto agora')