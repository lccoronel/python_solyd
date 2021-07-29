var_verdade = True
var_mentira = False

if var_verdade == True:
  print('var_verdade é verdadeiro')

a = 10
b = 10

fruta = 'uva'

if a < b and fruta == 'uva':
  print(a, 'é menor que', b)
elif (a == b and fruta == 'uva') or (a < b and fruta != 'uva'):
  print('esquisito')
else:
  print(a, 'é maior que', b)

idade = 50

if not idade == 49:
  print('novo')
else:
  print('idoso')

# exercicio

idade = input('Qual sua idade?')
peso = input('Qual seu peso?')
altura = input('Qual sua altura?')

idade_validation = idade > '18'
peso_validation = peso >= '60'
altura_validation = altura >= '1.70'

if (idade_validation and peso_validation and altura_validation):
  print('Pode entrar no exercito')
else:
  print('Nao pode entrar no exercito')
