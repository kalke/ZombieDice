import time

from exceptions import NumeroDeJogadoresExcedido, NumeroDeJogadoresMenorQueOPermitido

class ZombieDice:

    def __init__(self):
        print("Iniciando o Zombie Dice v1.0.0")
        time.sleep(2)
        # Instanciando todas as variaveis que serao usadas ao longo dos metodos.
        self.C = "Cerébro"
        self.P = "Passos"
        self.T = "Tiro"

        self.pontuacao = []
        self.pontuacao_atual = 0
        self.cerebro = 0
        self.cerebro_atual = 0
        self.tiro = 0 
        self.tiro_atual = 0
        self.passos = 0

        self.jogadores = []
        self.numero_jogadores = 0
        self.jogador_atual = 0

        self.dado_verde = [self.C,self.P,self.T,self.C,self.P,self.C]
        self.dado_amarelo = [self.P,self.C,self.P,self.C,self.P,self.T]
        self.dado_vermelho = [self.T,self.C,self.P,self.T,self.P,self.T]

        self.jogadas = 0
        self.dados_totais = [self.dado_verde,self.dado_verde,self.dado_verde,self.dado_verde,self.dado_verde,self.dado_verde,self.dado_amarelo,self.dado_amarelo,self.dado_amarelo,self.dado_amarelo,self.dado_vermelho,self.dado_vermelho,self.dado_vermelho]

        print("Bem vindos ao Zombie Dice! - Por Henrique Kalke")
        time.sleep(2)

    def definir_jogadores(self):
        try:
            while self.numero_jogadores < 2:
                self.numero_jogadores = int(input("Informe a quantidade de jogadores (de 2 a 5):\n"))
                if self.numero_jogadores < 2:
                    raise NumeroDeJogadoresMenorQueOPermitido(self.numero_jogadores)
                if self.numero_jogadores > 5:
                    raise NumeroDeJogadoresExcedido(self.numero_jogadores)
                else:
                    time.sleep(1)
                    print("A quantidade de jogadores selecionada foi: %s. Continuando..." % self.numero_jogadores)
                    time.sleep(2)
        except Exception as error:
            print(str(error))
            time.sleep(1)
            print("Defina a quantidade de jogadores novamente.")
            time.sleep(1)
            self.numero_jogadores = 0
            self.definir_jogadores()


        