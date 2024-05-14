# criei uma classe chamada Retangulo com um método __init__ que inicialize a largura e a altura do retangulo. Crie um método chamado "area" que retorne a área do retanggulo. Crie uma instancia de classe Retangulo e chame o métodoo area

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura

retangulo1 = Retangulo(5, 10)

area_retangulo1 = retangulo1.area()
print("Área do retângulo:", area_retangulo1)
