import random


class Multiplicacao():
    def __init__(self, dificuldade):
        """
        retorna uma multiplicação com base na dificuldade
        :param dificuldade:
        """
        self.dificuldade = dificuldade

    def nivel1(self):
        numero1 = random.randint(0, 10)
        numero2 = random.randint(0, 10)
        if numero1 < 0 and numero2 >= 0:
            operacao = "(" + str(numero1) + ")" + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        else:
            operacao = str(numero1) + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor

    def nivel2(self):
        numero1 = random.randint(0, 100)
        numero2 = random.randint(0, 100)
        if numero1 < 0 and numero2 >= 0:
            operacao = "(" + str(numero1) + ")" + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        else:
            operacao = str(numero1) + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor

    def nivel3(self):
        numero1 = random.randint(-100, 100)
        numero2 = random.randint(-100, 100)
        if numero1 < 0 and numero2 >= 0:
            operacao = "(" + str(numero1) + ")" + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        else:
            operacao = str(numero1) + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor

    def nivel4(self):
        numero1 = random.randint(-1000000, 1000000)
        numero2 = random.randint(-1000000, 1000000)
        if numero1 < 0 and numero2 >= 0:
            operacao = "(" + str(numero1) + ")" + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " x " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, 'x']
            return vetor
        else:
            operacao = str(numero1) + " x " + str(numero2)
            vetor = [operacao, numero1, numero2, 'x']
            return vetor

    def escolha(self):
        """
        Método síntese que verifica a dificuldade e retorna a operação apropriada aleatóriamente
        :return:
        """
        if self.dificuldade == 1:
            return Multiplicacao(self.dificuldade).nivel1()
        elif self.dificuldade == 2:
            return Multiplicacao(self.dificuldade).nivel2()
        elif self.dificuldade == 3:
            return Multiplicacao(self.dificuldade).nivel3()
        elif self.dificuldade == 4:
            return Multiplicacao(self.dificuldade).nivel4()


if __name__ == '__main__':
    multiplicacao = Multiplicacao(1)
    print(multiplicacao.nivel1())
    print(multiplicacao.nivel2())
    print(multiplicacao.nivel3())
    print(multiplicacao.nivel4())
