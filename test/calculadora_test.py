import unittest
from unittest import TestCase

from src.calculadora import Calculadora

# print('Deve somar 2 e 2 com resultado 4')
# calculadora = Calculadora(operando_x=2, operando_y=2)
# assert calculadora.somar() == 4

# print('Deve somar 2.5 e 2.5 com resultado 5')
# calculadora_2 = Calculadora(operando_x=2.5, operando_y=2.5)
# assert calculadora_2.somar() == 5

# print('Deve retornar 0 caso utilize valores vazios')
# calculadora_3 = Calculadora(operando_x=None, operando_y=None)
# assert calculadora_3.somar() == 0

# print('Testes OK')
from src.failures.calculadora_failures import OperandoInvalido


class TestCalculadora(TestCase):
    def test_soma(self):
        calculadora = Calculadora(operando_x=2, operando_y=2)
        self.assertEqual(calculadora.somar(), 4)

    def test_soma_valor_float(self):
        calculadora = Calculadora(operando_x=2.5, operando_y=2.5)
        self.assertEqual(calculadora.somar(), 5)

    def test_soma_valor_vazio(self):
        calculadora = Calculadora(operando_x=None, operando_y=None)
        with self.assertRaises(OperandoInvalido):
            calculadora.somar()

    def test_subtracao(self):
        calculadora = Calculadora(operando_x=8, operando_y=2)
        self.assertEqual(calculadora.subtrair(), 6)

    def test_subtracao_valor_float(self):
        calculadora = Calculadora(operando_x=5.5, operando_y=2)
        self.assertEqual(calculadora.subtrair(), 3.5)

    def test_subtracao_valor_vazio(self):
        calculadora = Calculadora(operando_x=None, operando_y=None)
        with self.assertRaises(OperandoInvalido):
            calculadora.subtrair()

    def test_multiplicacao(self):
        calculadora = Calculadora(operando_x=2, operando_y=2)
        self.assertEqual(calculadora.multiplicar(), 4)

    def test_multiplicacao_valor_float(self):
        calculadora = Calculadora(operando_x=2, operando_y=2.5)
        self.assertEqual(calculadora.multiplicar(), 5)

    def test_multiplicacao_valor_vazio(self):
        calculadora = Calculadora(operando_x=None, operando_y=None)
        with self.assertRaises(OperandoInvalido):
            calculadora.multiplicar()

    def test_divisao(self):
        calculadora = Calculadora(operando_x=5, operando_y=2)
        self.assertEqual(calculadora.dividir(), 2.5)

    def test_divisao_valor_float(self):
        calculadora = Calculadora(operando_x=3.5, operando_y=2)
        self.assertEqual(calculadora.dividir(), 1.75)

    def test_divisao_valor_vazio(self):
        calculadora = Calculadora(operando_x=None, operando_y=None)
        with self.assertRaises(OperandoInvalido):
            calculadora.dividir()


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
