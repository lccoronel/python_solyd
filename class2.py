nome = input('Escreva seu nome: ') #string
idade = input('Escreva sua idade: ') #numero
altura = input('Escreva sua altura: ')  #float
print(nome, 'tem', idade, 'ano(s) e', altura, 'de altura')

#print(type(altura))

frase = nome + ' tem ' + str(idade) + ' ano(s) e ' + str(altura) + ' de altura'
print(frase)