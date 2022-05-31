from lib.Conta import Conta

c1 = Conta('Inter', '001', 'Fulano', 500)
c2 = Conta('Caixa', '002', 'Cicrano', 800)

print(c1.saldo)
print(c2.saldo)

c1.transferir(c2, 200)
c1.depositar(600)

print(c2.saldo)
print(c1.saldo)