import unittest
from unittest import TestCase

from src.failures.calculadora_failures import OperandoInvalido
from src.failures.usuario_failures import NomeInvalido, OperacaoInvalida
from src.telas.usuario import solicita_nome, solicita_operando_x, solicita_operacao, solicita_operando_y


class TestUsuario(TestCase):
    def test_nome_usuario(self):
        usuario = solicita_nome()
        self.assertIsNot(usuario, '', NomeInvalido)

    def test_solicita_operacao(self):
        operacao = solicita_operacao()
        self.assertIsNot(operacao, '', OperacaoInvalida)

    def test_solicita_operando_x(self):
        operando_x = solicita_operando_x()
        self.assertIsNot(operando_x, '', OperandoInvalido)

    def test_solicita_operando_y(self):
        operando_y = solicita_operando_y()
        self.assertIsNot(operando_y, '', OperandoInvalido)


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
