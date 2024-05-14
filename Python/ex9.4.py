# crie uma classe chamada ContaBancaria com metodos depositar e sacar. tratametno de excessoes para ssaqe maior que saldo

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        try:
            if valor > 0:
                if self.saldo >= valor:
                    self.saldo -= valor
                    print(f"Saque de R${valor:.2f} realizado com sucesso.")
                else:
                    raise ValueError("Saldo insuficiente para o saque.")
            else:
                raise ValueError("Valor inválido para saque.")
        except ValueError as e:
            print(e)

minha_conta = ContaBancaria(1000)
minha_conta.depositar(500)
minha_conta.sacar(3000)
minha_conta.sacar(-100)
minha_conta.sacar(700)
