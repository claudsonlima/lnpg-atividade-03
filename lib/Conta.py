class Conta:

    def __init__(self, banco, agencia, titular, saldo):
        self.banco = banco
        self.agencia = agencia
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if(self.saldo > 0 and valor <= self.saldo):
            self.saldo -= valor

    def transferir(self, destinatario, valor):
        if(self.saldo > 0 and valor <= self.saldo):
            self.saldo -= valor
            destinatario.depositar(valor)