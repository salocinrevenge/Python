def mostrarKesimo(lista,posicao,atual):
    if posicao==atual:
        return lista[atual]
    else:
        return mostrarKesimo(lista,posicao,atual+1)

def main():
    lista=list(map(int,input().split()))
    lista.sort()
    k=int(input())
    print(mostrarKesimo(lista,k-1,0))

main()