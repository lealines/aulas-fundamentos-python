class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, valor):
        self.__celsius = valor

    def para_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32

    def para_kelvin(self):
        return self.celsius + 273.15

temp = Temperatura(25)

print('Temperatura em Celsius:', temp.celsius)
print('Temperatura em Fahrenheit:', temp.para_fahrenheit())
print('Temperatura em Kelvin:', temp.para_kelvin())