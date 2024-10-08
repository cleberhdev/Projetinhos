#CADASTRO DOS JOGADORES ----------------------------------------------------------------------------------------------------
from datetime import datetime # importação da biblioteca 
jogador=str(input('digite seu nome '))
endereço=str(input('digite seu endereço '))  
telefone=int(input('digite um telefone para contato'))
dn=input('qual a sua data de nascimento?')
id=int(input("qual a sua idade?"))
nivel_abilidade=int(input("""qual o seu nivel de abilidade [1]INICIANTE
                          [2]INTERMEDIARIO  
                          [3]AVAÇADO"""))
if nivel_abilidade == 1:
       print('OK')
if nivel_abilidade == 2:
       print('OK')
if nivel_abilidade == 3 :
        print('OK')
else:
      print('opção invalida')
numeroD=int(input('qual o numero de derrotas'))
numeroV=int(input('qual o numero de vitorias'))

jogador2=str(input('digite o nome do segundo jogador'))
endereço2=str(input('digite seu endereço '))  
telefone2=int(input('digite um telefone para contato'))
dn2=input('qual a sua data de nascimento?')
id2=int(input("qual a sua idade?"))
nivel_abilidade2=int(input("""qual o seu nivel de abilidade [1]INICIANTE
                          [2]INTERMEDIARIO  
                          [3]AVAÇADO"""))
if nivel_abilidade2 == 1:
       print('OK')
if nivel_abilidade2 == 2:
       print('OK')
if nivel_abilidade2 == 3 :
        print('OK')
else:
      print('opção invalida')
numeroD2=int(input('qual o numero de derrotas'))
numeroV2=int(input('qual o numero de vitorias'))
print("")
print("")



#AGENDAMENTO DA QUADRA  ----------------------------------------------------------------------------------------------------
print('AGENDAMENTO DA QUADRA ')
def horario_quadra():
       while True: 
        horario_input=input("digite o horario para agendamento")
        try: #para gerar erro se o usuario digitar o horário errado
             horario=datetime.strptime(horario_input,"%H:%M")
             return horario   
        except ValueError:# é como se fosse o senão do try
         print('você digitou o formato o formato do horário errado ')
horario_quadra()
dt_agendamento=input('digite a data para agendamento')
QD_agendada=int(input("""Qual quadra deseja agendar [1]Quadra
                 [2]Quadra
                 [3]Quadra
                 [4]Quadra
                 [5]Quadra
                 [6]Quadra"""))