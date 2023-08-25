# Exercicio com classes
# 1. Criar uma classe carro (nome)
# 2. Criar uma classe motor (nome)
# 3. Criar uma classe fabricante (nome)
# 4. Fazer uma ligação entre carro e motor
# Um motor pode ser de vários carros
# 5. Fazer uma ligação entre carro e fabricante
# um fabricante pode fazer varios carros
# exiba o nome do carro, do motor e do fabricante

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


palio = Carro('palio')
fiat = Fabricante('Fiat')
palio.fabricante = fiat
motor_1_0 = Motor('1.0')
palio.motor = motor_1_0
print(palio.nome, palio.motor.nome, palio.fabricante.nome)

uno = Carro('Uno')
uno.fabricante = fiat
uno.motor = motor_1_0
print(uno.nome, uno.motor.nome, uno.fabricante.nome)
