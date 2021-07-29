from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 6, 'ford', 10)
carro_azul = Carro('azul', 'bmw', 30)

print("Tanque:", carro_azul.tanque)
carro_azul.abastecer(21)
print("Tanque:", carro_azul.tanque)

