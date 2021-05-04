
def returnerIdade(obj):
    return obj.idade

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

lista = []
lista.append(Pessoa("ana", 10, 100, 123))
lista.append(Pessoa("daoberto", 21, 89, 202))
lista.append(Pessoa("maria", 200, 40, 150))
lista.append(Pessoa("nicolas", 19, 75, 175))
lista.append(Pessoa("arthur", 15, 60, 170))
lista.sort(key=returnerIdade, reverse=True)
for i in range(len(lista)):
    print(lista[i].nome)