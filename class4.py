lista_nomes = ['Joao', 'Lucas', 'Teste']

lista_nomes.append('Guilherme')
lista_nomes.append('Joao')

lista_nomes.remove('Teste')

lista_nomes.insert(1, 'Lilian')

lista_nomes[2] = 'Lucas Coronel'

contador_joao = lista_nomes.count('Joao')

print(lista_nomes[0:4])
print(lista_nomes[2][::-1]) #escrever string ao contrario
print(contador_joao)
print(len(lista_nomes))

