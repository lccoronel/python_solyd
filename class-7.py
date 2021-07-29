def soma(numero1, numero2):
  resp = numero1 + numero2
  return resp

print(soma(2, 2))

def tem_sete_letras(termo):
  if len(termo) == 7:
    return True
  else:
    return False

print(tem_sete_letras("extremo"))

# exercicio

colecao = [1, 20, 3, 4, 5]

def maior_numero(colecao):
  maior = 0
  for numero in colecao:
    if maior < numero:
      maior = numero
  
  return maior


print(maior_numero(colecao))
