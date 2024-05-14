# crie uma classe chamada Animal com metodom__init__ QUE INICIALIZE o nome do animal. Crie u metodo chamado emitir_som que emita um som generico do animal. Crie uma classe chamada Cachorro que herrde da classe Animal e adicione um metodo chamado emitir_som que emita o som do latido do cachorro. Criei uma instancia Cachorro e chame o método emitir_som

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        print("shhsshhshshshs")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

meu_cachorro = Cachorro("Toby")

meu_cachorro.emitir_som()
