import sys

argumentos = sys.argv

print(argumentos)

def soma(n1, n2):
  return n1 + n2


resultado = soma(float(argumentos[1]), float(argumentos[2]))

print(resultado)