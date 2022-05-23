import random
from Model.Carta import Carta
from Model.Naipe import Naipe
from Model.SimboloCartas import SimboloCartas


class Baralho:

    def __init__(self):
        self._lista_cartas = []
        self._criar_cartas()

    @property
    def lista_cartas(self):
        return self._lista_cartas

    @lista_cartas.getter
    def GetListaCartas(self):
        return self._lista_cartas

    def GetItemListaCartas(self, index):
        return self._lista_cartas[index]

    def _criar_cartas(self):
        for idxNaipe in range(Naipe.GetQuantidadeNaipes()):
            for idxSimbolo in range(SimboloCartas.GetQuantidadeSimbolos()):
                self.adicionar_carta(Carta(idxNaipe, idxSimbolo))

    def adicionar_carta(self, c):
        self._lista_cartas.append(c)

    def retirar_carta(self):
        self._lista_cartas.pop(0)

    def embaralhar_cartas(self):
        random.shuffle(self._lista_cartas)

    def quantidade(self):
        return len(self._lista_cartas)
