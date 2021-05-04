from math import ceil

def calcular(valor,expoente,base):
    if expoente == 0:
        return valor
    if expoente == 1:
        return valor*base
    else:
        return calcular(valor*base*base,expoente-2,base)

def main():
    base,expoente=input().split()
    print(calcular(1,int(expoente),int(base)))
main()