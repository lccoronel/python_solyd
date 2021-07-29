from cliente import Cliente

class Conta(Cliente):
  def __init__(self, nome, cpf, idade, saldo):
    self.saldo = saldo
    super().__init__(nome, cpf, idade)

  def depositar(self, quantidade):
    self.saldo += quantidade

  def sacar(self, quantidade):
    if quantidade > self.saldo:
      print("Saldo insuficiente")
    else:
      self.saldo -= quantidade

  def consulta_saldo(self):
    return print("Saldo:", self.saldo)