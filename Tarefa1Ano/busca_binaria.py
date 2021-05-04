def buscaBinaria(valor,lista,min,max):
    if max-min<2:
        return -1
    if lista[((max-min)//2)+min]==valor:
        return ((max-min)//2)+min
    elif lista[((max-min)//2)+min]<valor:
        return buscaBinaria(valor,lista,min+((max-min)//2),max)
    else:
        return buscaBinaria(valor,lista,min,max-((max-min)//2))

def main():
    lista=list(map(int,input().split()))
    numero=int(input())
    print(buscaBinaria(numero,lista,0,len(lista)-1))

main()