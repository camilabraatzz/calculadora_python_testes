from src.failures.calculadora_failures import OperandoInvalido
from src.failures.usuario_failures import NomeInvalido, OperacaoInvalida


def solicita_nome():
    try:
        nome = input('Digite seu nome ')
        return nome
    except Exception:
        raise NomeInvalido


def solicita_operacao():
    try:
        operacao = input('Digite a operação que deseja realizar ')
        return operacao
    except Exception:
        raise OperacaoInvalida


def solicita_operando_x():
    try:
        operando = int(input('Digite o primeiro número '))
        return operando
    except TypeError:
        raise OperandoInvalido


def solicita_operando_y():
    try:
        operando = int(input('Digite o segundo número '))
        return operando
    except TypeError:
        raise OperandoInvalido
