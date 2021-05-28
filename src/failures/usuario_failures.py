class NomeInvalido(Exception):
    def __init__(self, mensagem='Digite um nome válido!'):
        self.mensagem = mensagem


class OperacaoInvalida(Exception):
    def __init__(self, mensagem='Digite uma operação válida!'):
        self.mensagem = mensagem