def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

retorno = soma(2, 2)

print(retorno)

def tem_sete_letras(palavra):
  if len(palavra) == 7:
    return True
  else:
    return False

palavra = 'lucasca'

if tem_sete_letras(palavra):  
  print(palavra, 'tem sete letras')



# atividade 

def maior_valor(colecao):
  maior_numero = 0

  for numero in colecao:
    if numero > maior_numero:
      maior_numero = numero
  
  return maior_numero

print(maior_valor([3, 5, 1]))
