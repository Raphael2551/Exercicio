# crie uma classe chamada ContaBancaria com atributo saldo e com métodos para depositar, sacar e exibir saldo da conta

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

conta = ContaBancaria(1000)
conta.exibir_saldo()
conta.depositar(500)
conta.sacar(200)
conta.exibir_saldo()
