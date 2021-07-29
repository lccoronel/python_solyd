minha_tupla = ('Gui', 'Joao') # imutavel
meu_dicionario = {'nome': 'Guilherme', 'idade': 27}
meu_conjunto = {'Gui', 'Joao'} # nao pode ter intens repetidos

meu_dicionario['nome'] = 'Lucas'

print(meu_dicionario['nome'])

if 'Guilherme' in meu_dicionario.values():
  print('Guilherme esta em meu dicionario')
else:
  print('Nao esta em meu dicionario')

# para iniciar um  conjunto zerado

iniciar_conjunto = set()

# pode misturar tudo

mix = [(1, 2), {'nome': 'Lucas'}, {'Lu', 'Leo', 'Lili'}]
print(mix)
