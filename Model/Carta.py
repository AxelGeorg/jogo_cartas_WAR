class Carta:

    def __init__(self, naipe, simboloCarta):
        self.__naipe = naipe
        self.__simboloCarta = simboloCarta

    @property
    def naipe(self):
        return self.__naipe

    @property
    def simboloCarta(self):
        return self.__simboloCarta

    def MostraCarta(self):
        print(f"\nNaipe {self.naipe} - Simbolo {self.simboloCarta}")
