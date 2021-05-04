def encontrarMaior(lista,maior):
    if not len(lista)==0:
        maior = max(maior, lista[0])
        maior=max(maior,encontrarMaior(lista[1:len(lista)],maior))
    return maior

def main():
    lista = list(map(int,input().split()))
    print(encontrarMaior(lista,lista[0]))
    pass

main()