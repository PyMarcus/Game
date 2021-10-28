import random


class Soma():
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
            operacao = "(" + str(numero1) + ")" + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return operacao
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return operacao
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return operacao
        else:
            operacao = str(numero1) + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return vetor

    def nivel2(self):
        numero1 = random.randint(0, 100)
        numero2 = random.randint(0, 100)
        if numero1 < 0 and numero2 >= 0:
            operacao = "(" + str(numero1) + ")" + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        else:
            operacao = str(numero1) + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return vetor

    def nivel3(self):
        numero1 = random.randint(-100, 100)
        numero2 = random.randint(-100, 100)
        if numero1 < 0 and numero2 >= 0:
            operacao = "(" + str(numero1) + ")" + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        else:
            operacao = str(numero1) + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return vetor

    def nivel4(self):
        numero1 = random.randint(-1000000, 1000000)
        numero2 = random.randint(-1000000, 1000000)
        if numero1 < 0 and numero2 >= 0:
            operacao = "(" + str(numero1) + ")" + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        elif numero2 < 0 and numero1 >= 0:
            operacao = str(numero1) + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        elif numero1 < 0 and numero2 < 0:
            operacao = "(" + str(numero1) + ")" + " + " + "(" + str(numero2) + ")"
            vetor = [operacao, numero1, numero2, '+']
            return vetor
        else:
            operacao = str(numero1) + " + " + str(numero2)
            vetor = [operacao, numero1, numero2, '+']
            return vetor

    def escolha(self):
        """
        Método síntese que verifica a dificuldade e retorna a operação apropriada aleatóriamente
        :return:
        """
        if self.dificuldade == 1:
            return Soma(self.dificuldade).nivel1()
        elif self.dificuldade == 2:
            return Soma(self.dificuldade).nivel2()
        elif self.dificuldade == 3:
            return Soma(self.dificuldade).nivel3()
        elif self.dificuldade == 4:
            return Soma(self.dificuldade).nivel4()


if __name__ == '__main__':
    soma = Soma(4)
    print(soma.nivel1())
    print(soma.nivel2())
    print(soma.nivel3())
    print(soma.nivel4())
    print(soma.escolha())
