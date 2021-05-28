from src.failures.calculadora_failures import OperandoInvalido, ValoresIncorretos


class Calculadora:
    def __init__(self, operando_x=0, operando_y=0):
        self.operando_x = operando_x
        self.operando_y = operando_y

    def somar(self):
        try:
            return self.operando_x + self.operando_y
        except ValueError:
            raise ValoresIncorretos()

    def subtrair(self):
        try:
            return self.operando_x - self.operando_y
        except ValueError:
            raise ValoresIncorretos()

    def dividir(self):
        try:
            return self.operando_x / self.operando_y
        except TypeError:
            raise OperandoInvalido()
        except ZeroDivisionError:
            raise OperandoInvalido(mensagem='Não é possível divisão por zero')

    def multiplicar(self):
        try:
            return self.operando_x * self.operando_y
        except ValueError:
            raise ValoresIncorretos()
