import math

class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def get_raio(self):
        return self.__raio

    def set_raio(self, novo_raio):
        if novo_raio > 0:
            self.__raio = novo_raio
        else:
            print('O raio deve ser positivo.')

    def calcular_area(self):
        return math.pi * (self.__raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.__raio

raio_util = float(input('Digite o raio do círculo: '))

c = Circulo(raio_util)

print('\n--- RESULTADOS ---\n')
print('Raio:', c.get_raio())
print('Área:', c.calcular_area())
print('Perímetro:', c.calcular_perimetro())