import random
from Controller.GravaLogResultado import GravaLogResultado
from Model.Jogador import Jogador
from Model.Lista_Jogadores import ListaJogadores
from Model.SimboloCartas import SimboloCartas


class Tela:

    def __init__(self):
        self._jogadoresTela = ListaJogadores()

    @property
    def jogadoresTela(self):
        return self._jogadoresTela

    @jogadoresTela.getter
    def GetJogadoresTela(self):
        return self._jogadoresTela.GetListaJogadores

    def DefineJogadoresTela(self):
        qtdJogadores = 0
        while qtdJogadores != 2 and qtdJogadores != 4:
            qtdJogadores = int(
                input('Digite quantidade de jogadores (2 ou 4): '))

        for idxJogador in range(qtdJogadores):
            jogadorRobo = Jogador()
            jogadorRobo.nome = input(
                'Digite nome do jogador {}: '.format(idxJogador + 1))
            jogadorRobo.quantidadeJogadas = 0
            jogadorRobo.listaCartas = []
            self._jogadoresTela.adicionar_jogador(jogadorRobo)

    def IniciaJogo(self, baralho, listaJogadores):

        jogadores = ListaJogadores()
        jogadores.SetListaJogadores = listaJogadores

        self.EmbaralhaEDistribuiCartas(jogadores, baralho)

        qtdMaxRodadas = int(input('Digite quantidade de rodadas: '))

        empatou = False
        idxRodada = 0
        idxEmpate = 0
        qtdCartasRodada = 0
        cartasRodada = []
        jogador = jogadores._lista_jogadores[0]
        while True:
            qtdJogadoresComCartas = jogadores.QuantidadeJogadoresComCartas()
            if qtdJogadoresComCartas <= 1:
                break

            if empatou == False:
                qtdCartasRodada = qtdJogadoresComCartas

            if len(jogador.listaCartas) == 0:
                continue

            if jogadores.GetPrimeiroJogador() == jogador and empatou == False:
                idxRodada += 1
                if idxRodada > qtdMaxRodadas:
                    break
                print(F"Rodade {str(idxRodada)}")
                GravaLogResultado.GravaLog(F"Rodade {str(idxRodada)}")

            elif jogadores.GetPrimeiroJogador() == jogador and empatou == True:
                idxEmpate = idxEmpate + 1
                qtdCartasRodada = len(cartasRodada) + qtdJogadoresComCartas

            cartaAtualJogador = jogador.listaCartas[0]
            del(jogador.listaCartas[0])
            cartasRodada.append(cartaAtualJogador)

            jogador._qtdJogadas = jogador._qtdJogadas + 1

            simbolo = SimboloCartas(int(cartaAtualJogador) + 1).name
            print(
                f"Jogador {jogador.nome} retirou a carta {simbolo}")
            GravaLogResultado.GravaLog(
                f"Jogador {jogador.nome} retirou a carta {simbolo}")

            jogador = jogadores.obter_proximo_jogador()
            while len(jogador.listaCartas) == 0:
                jogador = jogadores.obter_proximo_jogador()

            if qtdCartasRodada - len(cartasRodada) != 0:
                continue

            idxGanhador = self.VerificaGanhador(
                cartasRodada, jogadores.QuantidadeJogadoresComCartas())
            if idxGanhador == -1:
                empatou = True
                continue

            idxEmpate = 0
            qtdCartasRodada = 0
            empatou = False

            jogadorGanhou = jogadores.GetItemListaJogadores(idxGanhador)

            """random.shuffle(cartasRodada)"""
            for carta in cartasRodada:
                jogadorGanhou.listaCartas.append(carta)

            print(f"- Jogador {jogadorGanhou.nome} ganhou a rodada!\n")
            GravaLogResultado.GravaLog(
                f"- Jogador {jogadorGanhou.nome} ganhou a rodada!\n")
            cartasRodada.clear()

        print('\nFim do Jogo!')
        GravaLogResultado.GravaLog("Fim do Jogo!")

    def EmbaralhaEDistribuiCartas(self, jogadores, baralho):
        qtdDivisaoCartas = 0
        if len(jogadores._lista_jogadores) == 2:
            qtdDivisaoCartas = 26
        else:
            qtdDivisaoCartas = 13

        idxCarta = 0
        idxJogador = 0
        for jogador in jogadores._lista_jogadores:
            for idxCarta in range(qtdDivisaoCartas):
                jogador.inserirCarta(
                    baralho.GetItemListaCartas(idxCarta + idxJogador).simboloCarta)
            idxJogador = idxJogador + qtdDivisaoCartas

        """for jogador in jogadores._lista_jogadores:
            print(f"\nJogador {jogador.nome}")
            for carta in jogador.listaCartas:
                print(f"-- Carta {carta}")"""

    def VerificaGanhador(self, listaCartas, qtdJogadoresComCartas):

        cartasParaVerificar = []
        if qtdJogadoresComCartas != len(listaCartas):
            qtdEmpates = len(listaCartas) / qtdJogadoresComCartas

            qtdCartasRemover = (qtdEmpates - 1) * qtdJogadoresComCartas
            for carta in listaCartas:
                if qtdCartasRemover == 0:
                    cartasParaVerificar.append(carta)
                else:
                    qtdCartasRemover = qtdCartasRemover - 1
        else:
            cartasParaVerificar = listaCartas

        maiorCarta = -1
        idxGanhador = -2
        idxCarta = -1
        for carta in cartasParaVerificar:
            idxCarta = idxCarta + 1
            cartaAtual = int(carta)
            if cartaAtual > maiorCarta:
                idxGanhador = idxCarta
                maiorCarta = cartaAtual
            elif cartaAtual == maiorCarta:
                idxGanhador = -1

        return idxGanhador

    def MostraResultado(self, listaJogadores):
        listaResultado = ListaJogadores()
        listaResultado.SetListaJogadores = listaJogadores

        if listaResultado.QuantidadeJogadoresComCartas() > 1:
            print('Jogo Empatado!')
            GravaLogResultado.GravaLog('Jogo Empatado!')
        else:
            idxGanhador = listaResultado.GetIndexGanhador()
            jogador = listaResultado.GetItemListaJogadores(idxGanhador)
            print(
                f"Jogador {jogador.nome} ganhou com {jogador._qtdJogadas} jogadas!")
            GravaLogResultado.GravaLog(
                f"Jogador {jogador.nome} ganhou com {jogador._qtdJogadas} jogadas!")

        for jogador in listaResultado._lista_jogadores:
            print(
                f"Jogador {jogador.nome} possui {len(jogador.listaCartas)} cartas.")
            GravaLogResultado.GravaLog(
                f"Jogador {jogador.nome} possui {len(jogador.listaCartas)} cartas.")
