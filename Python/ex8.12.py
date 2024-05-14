# crie uma classe chamada Veiculo com método para acelerar, freae e exibir a velocidade do veiculo. Crie uma classe chamada Carro que herde da classe Veiculo e adicione um atributo chamado marca. Crie uma instancia da classse Carro e teste os métodoscriados

class Veiculo:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
    
    def frear(self, valor):
        self.velocidade -= valor
    
    def exibir_velocidade(self):
        print(f"Velocidade atual: {self.velocidade} km/h")


class Carro(Veiculo):
    def __init__(self, marca):
        super().__init__()
        self.marca = marca


meu_carro = Carro("Fiat")
meu_carro.acelerar(50)
meu_carro.exibir_velocidade()
meu_carro.frear(20)
meu_carro.exibir_velocidade()
print("Marca do carro:", meu_carro.marca)
