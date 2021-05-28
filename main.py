from src.calculadora import Calculadora
from src.pessoa import Pessoa
from src.telas.usuario import solicita_nome, solicita_operacao, solicita_operando_x, solicita_operando_y


def UsuarioInteracoes():
    resultado = None
    pessoa = Pessoa(nome=solicita_nome())
    nome = pessoa.nome
    operacao = solicita_operacao()
    operando_x = solicita_operando_x()
    operando_y = solicita_operando_y()

    calculadora = Calculadora(operando_x, operando_y)

    if operacao == '+':
        resultado = calculadora.somar()
    elif operacao == '-':
        resultado = calculadora.subtrair()
    elif operacao == '*':
        resultado = calculadora.multiplicar()
    elif operacao == '/':
        resultado = calculadora.dividir()
    print(f'{nome}, o resultado da operação é: {resultado}')


UsuarioInteracoes()
