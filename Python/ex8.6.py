# crie uma classe chamada circulo com metodo __init__ inicialize o raio do circulo. Crir um metofo chamado area que retorne a area do circulo.

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return math.pi * self.raio**2

circulo1 = Circulo(5)

area_circulo1 = circulo1.area()
print("Área do círculo:", area_circulo1)
