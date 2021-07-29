nomes = ['Guilherme', 'Marcelo', 'Joao', 'Julia']

for nome in nomes:
  print(nome)

# criar 5 numeros

lista_de_numeros = range(5, 10) # vai de 5 a 10
lista_de_numeros = range(5, 100, 2) #vai de 5 a 100 pulando de 2 em 2 numeros
lista_de_numeros = range(5)

for numero in lista_de_numeros:
  print(numero)

# loop em string

meu_nome = "Lucas"

for letra in meu_nome:
  print(letra)


# while 
i = 0

while i < 10:
  print("I ainda e menor que 10: ", i)
  i += 1

# exercicio

convidados = []
i = 0

while i < 5:
  nome = input("Nome de um convidado: ")  
  convidados.append(nome)
  i += 1

print(convidados)
