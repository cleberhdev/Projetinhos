import time as tm

class Jogador:
    def __init__(self, nome: str, endereco: str, telefone: str, data_nascimento: str, nivel_abilidade: int, numeroVitorias=0, numeroDerrotas=0):
        if not isinstance(nome, str):
            raise TypeError(f"O nome deve ser uma string, mas recebeu {type(nome).__name__}")

        if not isinstance(endereco, str):
            raise TypeError(f"O endereço deve ser uma string, mas recebeu {type(endereco).__name__}")

        if not isinstance(telefone, str):
            raise TypeError(f"O telefone deve ser uma string, mas recebeu {type(telefone).__name__}")

        if not isinstance(nivel_abilidade, int):
            raise TypeError(f"O Nível de Habilidade deve ser um inteiro, mas recebeu {type(nivel_abilidade).__name__}")
        if nivel_abilidade < 1 or nivel_abilidade > 3:
            raise Exception("O nível de habilidade deve ser entre 1 e 3.")

        # Corrigido o alias para 'tm' ao usar strptime
        try:
            self.data_nascimento = tm.strptime(data_nascimento, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Formato de data inválido. Esperado: dd/mm/yyyy, recebido: {data_nascimento}")

        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.nivel_abilidade = nivel_abilidade
        self.numeroDerrotas = numeroDerrotas
        self.numeroVitorias = numeroVitorias
        self.idade = self.calcular_idade()  # Chama o método e armazena o resultado em self.idade

    def calcular_idade(self):
        # Data atual
        data_atual = tm.localtime()

        # Ano, mês e dia de nascimento
        ano_nascimento = self.data_nascimento.tm_year
        mes_nascimento = self.data_nascimento.tm_mon
        dia_nascimento = self.data_nascimento.tm_mday

        # Cálculo básico da idade
        idade = data_atual.tm_year - ano_nascimento

        # Ajusta a idade se o aniversário ainda não ocorreu este ano
        if (data_atual.tm_mon, data_atual.tm_mday) < (mes_nascimento, dia_nascimento):
            idade -= 1

        return idade  # Retorna a idade calculada


