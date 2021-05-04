from funcoes import isInt
from neuronio import Neuronio
from random import randint


class Rede:
    rede = []

    def __init__(self, numeroDeNeuroniosPorColuna):
        for i in numeroDeNeuroniosPorColuna:
            if not isInt(i):
                print("Número de neuronios inválido!")
                return
            coluna = []
            for _ in range(i):
                coluna.append(Neuronio)
            self.rede.append(coluna)

    def calcular(self, entrada):
        resposta = []
        for i, coluna in enumerate(self.rede):
            for j, neuronio in enumerate(coluna):
                if i == 0:
                    neuronio.adicionarValor(entrada[j])
                elif i == len(self.rede) - 1:
                    resposta.append(neuronio.saída)
                else:
                    for anterior in self.rede[i - 1]:
                        neuronio.adicionarValor(anterior.saída)
        for coluna in self.rede:
            for neuronio in coluna:
                neuronio.resetar()
        return resposta

    def aleatorizarPesos(self):
        for coluna in self.rede:
            for neuronio in coluna:
                neuronio.peso = randint(-100, 100)
