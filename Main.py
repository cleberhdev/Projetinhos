from Jogador import Jogador
from Partida import Partida
import os
import datetime as dt
def menu():
    os.system('cls')
    jogadores = []
    partidas_agendadas = []

    def verificar_disponibilidade(data_hora, quadra):
        for partida in partidas_agendadas:
            if partida.data_hora == data_hora and partida.quadra == quadra:
                return False
        return True

    while True:
        print("\nMenu de Agendamento de Partidas de Tênis")
        print("1. Cadastrar Jogador")
        print("2. Agendar Partida")
        print("3. Realizar Partida")
        print("4. Ver Jogadores Cadastrados")
        print("5. Ver Partidas Agendadas")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("\nNome do jogador: ")
            endereco = input("Endereço do jogador: ")
            telefone = input("Telefone do jogador: ")
            data_nascimento = input("Data de nascimento (DD/MM/YYYY): ")
            nivel_abilidade = int(input("Nível de habilidade (1-3): "))

            try:
                jogador = Jogador(nome, endereco, telefone, data_nascimento, nivel_abilidade)
                jogadores.append(jogador)
                print(f"Jogador {nome} cadastrado com sucesso!")
            except (TypeError, ValueError) as e:
                print(f"Erro ao cadastrar jogador: {e}")

        elif opcao == '2':
            if len(jogadores) < 2:
                print("É necessário ter pelo menos 2 jogadores cadastrados para agendar uma partida.")
                continue
            
            print("\nEscolha os jogadores:")
            for index, jogador in enumerate(jogadores):
                print(f"{index + 1}. {jogador.nome}")

            escolha_jogador1 = int(input("Escolha o primeiro jogador (número): ")) - 1
            escolha_jogador2 = int(input("Escolha o segundo jogador (número): ")) - 1
            
            if escolha_jogador1 == escolha_jogador2:
                print("Você deve escolher dois jogadores diferentes.")
                continue
            
            data_hora = input("Data e hora da partida (DD/MM/YYYY HH:MM): ")
            quant_partidas = int(input("Quantidade de partidas (1-6): "))
            quadra = int(input("Número da quadra: "))
            
            try:
                data_hora_formatada = dt.datetime.strptime(data_hora, "%d/%m/%Y %H:%M")
                if not verificar_disponibilidade(data_hora_formatada, quadra):
                    print("Erro: já existe uma partida agendada para essa quadra e horário.")
                    continue
                
                partida = Partida(jogadores[escolha_jogador1], jogadores[escolha_jogador2], data_hora, quant_partidas, quadra)
                partidas_agendadas.append(partida)
                print(f"Partida agendada entre {partida.jogador01.nome} e {partida.jogador02.nome} em {partida.data_hora} na quadra {partida.quadra}.")
            except (TypeError, ValueError) as e:
                print(f"Erro ao agendar partida: {e}")

        elif opcao == '3':
            if not partidas_agendadas:
                print("Não há partidas agendadas para serem realizadas.")
                continue
            
            print("\nEscolha a partida a ser realizada:")
            for index, partida in enumerate(partidas_agendadas):
                print(f"{index + 1}. {partida.jogador01.nome} vs {partida.jogador02.nome} em {partida.data_hora}, Quadra {partida.quadra}")
            
            escolha_partida = int(input("Escolha a partida (número): ")) - 1
            try:
                partida = partidas_agendadas[escolha_partida]
                partida.realizar_partida()
                partidas_agendadas.pop(escolha_partida)  # Remove a partida após realizá-la
            except IndexError:
                print("Escolha inválida!")

        elif opcao == '4':
            print()
            if not jogadores:
                print("Nenhum jogador cadastrado.")
            else:
                for jogador in jogadores:
                    print(f"Nome: {jogador.nome}, Endereço: {jogador.endereco}, Telefone: {jogador.telefone}, Data de Nascimento: {jogador.data_nascimento.tm_mday}/{jogador.data_nascimento.tm_mon}/{jogador.data_nascimento.tm_year},Idade: {jogador.idade}, Habilidade: {jogador.nivel_abilidade}, Vitórias: {jogador.numeroVitorias}, Derrotas: {jogador.numeroDerrotas}")

        elif opcao == '5':
            if not partidas_agendadas:
                print("Não há partidas agendadas.")
            else:
                print("\nPartidas Agendadas:")
                for partida in partidas_agendadas:
                    print(f"- {partida.jogador01.nome} vs {partida.jogador02.nome} em {partida.data_hora}, Quadra: {partida.quadra}, Quantidade de Partidas: {partida.quant_partidas}")

        elif opcao == '6':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Executando o menu
menu()