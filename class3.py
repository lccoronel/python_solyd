# var_verdadeiro = True
# var_falso = False

# if var_verdadeiro == True and var_falso == False:
#   print('verdadeiro')
# else:
#   print('falso')

# if var_verdadeiro == False or var_falso == False:
#   print('verdadeiro')
# else:
#   print('falso')

print('options: \n 1 - Escreve Guilherme \n 2 - Escreve Lucas \n 3 - Escreve Joao')

option = input('Escolha uma opcao:')

#elif = else if
if option == '1':
  print('Guilherme')
elif option == '2':
  print('Lucas')
elif option == '3':
  print('joao')
else:
  print(not True)