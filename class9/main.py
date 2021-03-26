from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa', 'ford', 6, 10)

carro_azul = Carro('azul', 'bmw', 20)

caminhao_rosa.abastecer(35)

print(caminhao_rosa.tanque)
print(carro_azul.tanque)