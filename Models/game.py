import sys
from random import choice
from Models.soma import Soma
from Models.subtracao import Subtracao
from Models.multiplicacao import Multiplicacao


class Mensagens():
    def dificuldade(self):
        """
        Permite a seleção da dificuldade
        :return:
        """
        try:
            dificuldade = int(input("Informe o nível de dificuldade desejado [1, 2, 3, 4, 5]: "))
        except TypeError:
            print("Tipo de dado não compatível\nFinalizando...")
            sys.exit(1)
        else:
            return dificuldade

    def inicio(self):
        """
        Começa um jogo, conforme a dificuldade desejada.
        :return:
        """
        nivel = Mensagens()
        dificuldade = nivel.dificuldade()
        soma = Soma(dificuldade)
        subtracao = Subtracao(dificuldade)
        multiplicacao = Multiplicacao(dificuldade)

        vetorSorteio = [soma.escolha(), multiplicacao.escolha(), subtracao.escolha()]
        escolha = choice(vetorSorteio)
        print(f"Qual a solução para {escolha[0]} ?")
        return escolha

    def verificador(self):
        contador = 0
        try:
            msg = Mensagens()
            operacao = msg.inicio()
            num1 = operacao[1]
            num2 = operacao[2]
            resposta = int(input("= "))
        except ValueError:
            print("Formato de resposta inválido")
        else:

            if operacao[3] == '+':
                solucao = num1 + num2
                if resposta == solucao:
                    print("Parabéns, resposta correta")
                    contador += 1
                    return contador
                else:
                    print("Resposta incorreta!\nMas, não desista!!!")
                    return contador

            elif operacao[3] == '-':
                solucao = num1 - num2
                if resposta == solucao:
                    print("Parabéns, resposta correta")
                    contador += 1
                    return contador
                else:
                    print("Resposta incorreta!\nMas, não desista!!!")
                    return contador

            elif operacao[3] == 'x':
                solucao = num1 * num2
                if resposta == solucao:
                    print("Parabéns, resposta correta")
                    contador += 1
                    return contador
                else:
                    print("Resposta incorreta!\nMas, não desista!!!")
                    return contador


if __name__ == '__main__':
    msg = Mensagens()
    print(msg.verificador())