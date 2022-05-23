from enum import Enum


class Naipe(Enum):
    Ouro = 0
    Paus = 1
    Copas = 2
    Espadas = 3

    def GetQuantidadeNaipes():
        return 4

    def descricao(self):
        return self.nome
