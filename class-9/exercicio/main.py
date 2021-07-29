from conta import Conta

lucas = Conta('Lucas Coronel', '45661572883', 24, 0)

print(lucas.saldo)

lucas.depositar(10)
print(lucas.saldo)

lucas.sacar(11)

lucas.sacar(5)
lucas.consulta_saldo()