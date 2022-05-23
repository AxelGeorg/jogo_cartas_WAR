from Controller.GravaLogResultado import GravaLogResultado
from Model.Baralho import Baralho
from Model.Jogador import Jogador
from Model.Lista_Jogadores import ListaJogadores
from View.Tela import Tela


class Jogo:

    def __init__(self):
        self._lista_jogadores = []
        self._baralho = Baralho()
        self._programa = Tela()
        self._logGravacao = GravaLogResultado()

    def iniciar(self):
        self.adicionar_jogadores()
        self.iniciar_rodadas()
        self.analisar_resultado()

    def adicionar_jogadores(self):
        self._programa.DefineJogadoresTela()
        self._lista_jogadores = self._programa.GetJogadoresTela

    def iniciar_rodadas(self):
        self._baralho.embaralhar_cartas()
        self._programa.IniciaJogo(self._baralho, self._lista_jogadores)

    def analisar_resultado(self):
        self._programa.MostraResultado(self._programa.GetJogadoresTela)
