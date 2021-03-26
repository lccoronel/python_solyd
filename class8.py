import sys

argumentos = sys.argv

def soma(n1, n2):
  return float(n1) + float(n2)

def sub(n1, n2):
  return float(n1) - float(n2)

if argumentos[1] == "soma":
  response = soma(argumentos[2], argumentos[3])
elif argumentos [1] == "sub":
  response = sub(argumentos[2], argumentos[3]) 

print(response)