class Neuronio:
    saída = 0
    peso = 1

    def resetar(self):
        self.saída = 0

    def adicionarValor(self, valor):
        self.saída += (valor * self.peso)
