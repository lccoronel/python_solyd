# Variáveis, tipos, entrada, saída e operadores matemáticos

print('primeiro print \nsegundo print \t terceiro print')

nome = input('Escreve seu nome: ')
print(type(nome))

sobrenome = 'Coronel '
print(nome, sobrenome)

idade = 24

print(nome, sobrenome + str(idade))

numero1 = 10
numero2 = 10
numero3 = 2

conta = numero2 + numero1 / 2
print(conta)

# exercicio

nome_exercicio = input('Escreva seu nome: ')
cpf = input('Escreva seu cpf: ')
idade_exercicio = input('Escreva sua idade: ')
altura = input('Escreva sua altura: ')
telefone = input('Escreva seu telefone: ')

print("Nome: ", nome_exercicio, "\nCpf: ", cpf, "\nIdade: ", idade_exercicio, "\nAltura: ", altura, "\nTelefone: ", telefone)
