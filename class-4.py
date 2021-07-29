frase = "Oi, tudo bem?"
print(len(frase))
print("Frase com minuscula:", frase.lower())
lista = ['Joao', 'Maria', 'Lucas', 'Joao']

print(lista[0:2]) # substring dentro da lista
print(lista[0:3:2]) # o ultimo numero server para pular uma posicao 


lista.append('Bruno')
lista.remove('Maria')
lista.insert(0 ,'Aline')

lista[2] = 'Lucas Coronel'

print(lista)
print(lista.count('Joao'))
print("Tamanho da lista de nomes:", len(lista))