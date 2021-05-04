arq1=input("insira o caminho do arquivo 1:")
with open(arq1,'r') as arquivo:
    texto1=arquivo.readlines()
print(texto1)

arq2=input("insira o caminho do arquivo 2:")
with open(arq2,'r') as arquivo:
    texto2=arquivo.readlines()
print(texto2)

saida = []
for i,elemento in enumerate(texto1):
    if elemento!=texto2[i]:
        saida.append(elemento)
print(saida)

assert texto1==texto2