class OperandoInvalido(Exception):
    def __init__(self, mensagem='Operando Inválido'):
        self.mensagem = mensagem


class ValoresIncorretos(Exception):
    def __init__(self, mensagem='Valores Incorretos'):
        self.mensagem = mensagem
