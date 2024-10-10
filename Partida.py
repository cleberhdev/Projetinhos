import datetime as tm
from Jogador import Jogador

class Partida:
    def __init__(self, jogador01: Jogador, jogador02: Jogador, data_hora: str, quant_partidas: int, quadra: int):
        # Verificação dos jogadores
        if not isinstance(jogador01, Jogador):
            raise TypeError(f"O jogador01 deve ser uma instância de Jogador, mas recebeu {type(jogador01).__name__}")
        if not isinstance(jogador02, Jogador):
            raise TypeError(f"O jogador02 deve ser uma instância de Jogador, mas recebeu {type(jogador02).__name__}")

        # Validação da quantidade de partidas
        if not isinstance(quant_partidas, int):
            raise TypeError(f"A quantidade de partidas deve ser um inteiro, mas recebeu {type(quant_partidas).__name__}")
        if quant_partidas < 1 or quant_partidas > 6:
            raise Exception("A quantidade de partidas deve ser entre 1 e 6")

        # Verificação da data e hora
        try:
            self.data_hora = tm.datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
            if self.data_hora < tm.datetime.now():
                raise ValueError("A data e hora agendadas não podem estar no passado.")
        except ValueError as e:
            raise ValueError(f"Formato de data/hora inválido. Esperado: 'DD/MM/YYYY HH:MM', erro: {e}")

        # Validação do tipo de quadra
        if not isinstance(quadra, int):
            raise TypeError(f"O número da quadra deve ser do tipo inteiro, mas recebeu {type(quadra).__name__}")

        # Atribuições
        self.jogador01 = jogador01
        self.jogador02 = jogador02
        self.quant_partidas = quant_partidas
        self.quadra = quadra  # Armazena o número da quadra
        self.placar = {jogador01.nome: 0, jogador02.nome: 0}  # Inicializa o placar

    # Realizar partida:
    def realizar_partida(self):
        for i in range(1, self.quant_partidas + 1):
            while True:  # Loop para garantir que a entrada seja válida
                try:
                    vitorias = int(input(f"Digite qual jogador venceu na partida {i} [1 para {self.jogador01.nome}/ 2 para {self.jogador02.nome}] - Placar[{self.jogador01.nome} - {self.placar[self.jogador01.nome]} | {self.jogador02.nome} - {self.placar[self.jogador02.nome]}]: "))
                    if vitorias == 1:
                        self.jogador01.numeroVitorias += 1
                        self.jogador02.numeroDerrotas += 1
                        self.placar[self.jogador01.nome] += 1  # Incrementa o placar do jogador01
                    elif vitorias == 2:
                        self.jogador02.numeroVitorias += 1
                        self.jogador01.numeroDerrotas += 1
                        self.placar[self.jogador02.nome] += 1  # Incrementa o placar do jogador02
                    else:
                        print("Entrada inválida! Por favor, digite 1 ou 2.")
                        continue  # Volta para o início do loop para solicitar novamente a entrada
                    break  # Sai do loop de entrada após uma entrada válida
                except ValueError:
                    print("Por favor, insira um número válido.")

        # Exibe o placar final após todas as partidas
        print("Placar final:")
        for jogador, pontos in self.placar.items():
            print(f"{jogador}: {pontos} pontos")


