import sys
from Models.game import Mensagens
from colorama import Fore
from random import choice

if __name__ == '__main__':
    opcao = True
    contador = 0
    jogo = Mensagens()
    while opcao:
        if opcao == False:
            break
        else:
            variavel = jogo.verificador()
            if variavel == 1:
                contador += 1
                print(f"Você tem {contador} pontos(s)!")
            else:
                print(f"Você tem {contador} pontos(s)!")
            try:
                colorama = [Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.LIGHTCYAN_EX]
                escolha = str(input(choice(colorama) + "Deseja continuar? (S/N): "))
            except ValueError:
                sys.exit(1)
            else:
                if escolha.lower() == 's' or escolha.lower() == 'y' or escolha.lower() == 'sim' or escolha.lower() == 'yes':
                    pass
                else:
                    print("Fim!")
                    opcao = False
