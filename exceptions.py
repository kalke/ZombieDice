class NumeroDeJogadoresExcedido(Exception):
    def __init__(self, numero_jogadores):
        self.numero_jogadores = numero_jogadores

    def __str__(self):
        formated_message = "Numero de jogadores maior que o permitido: %s" % self.numero_jogadores
        return formated_message

    def __repr__(self):
        return self.__str__()

class NumeroDeJogadoresMenorQueOPermitido(Exception):
    def __init__(self, numero_jogadores):
        self.numero_jogadores = numero_jogadores

    def __str__(self):
        formated_message = "Numero de jogadores menor que o permitido: %s" % self.numero_jogadores
        return formated_message

    def __repr__(self):
        return self.__str__()