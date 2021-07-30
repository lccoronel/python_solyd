import time

try:
  # divisao = 1200 / 0
  funcao()
except ZeroDivisionError: # tratando erros de deivisao
  print("nao deu pra faze essa divisao")
except NameError: # tratando erros de nomes digtados errados
  print("Voce digitou alguma coisa errada")
except Exception as erro: # tratando qualquer tipo de erro e coloando dentro da variavel erro
  print("Error:", erro)

def abre_arquivo():
  try: 
    open('arquivo.txt')
    return True
  except Exception as erro:
    print("aconteceu algum erro:", erro)
    return False

while not abre_arquivo():
  print('Tentando abrir o arquivo')
  time.sleep(5) # vai sair dessa linha depois de 5 segundos

print('consegui abri o arquivo')

