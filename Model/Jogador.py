
class Jogador:

    def __ini__(self):
        self._nome
        self._qtdJogadas
        self.__listaCartas = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def quantidadeJogadas(self):
        return self._qtdJogadas

    @quantidadeJogadas.setter
    def quantidadeJogadas(self, qtdJogadas):
        self._qtdJogadas = qtdJogadas

    @property
    def listaCartas(self):
        return self.__listaCartas

    @listaCartas.setter
    def listaCartas(self, listaCartas):
        self.__listaCartas = listaCartas

    def inserirCarta(self, carta):
        self.__listaCartas.append(carta)

    def buscarTodasCartas(self):
        return self.__listaCartas

    def buscarQuantidadeCartas(self):
        return len(self.__listaCartas)
