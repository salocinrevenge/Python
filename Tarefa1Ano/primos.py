from math import sqrt

def filtra(f,lista):
    listaParaReturn = []
    for elemento in lista:
        if f(elemento):
            listaParaReturn.append(elemento)
    return listaParaReturn

def mapeia(lista,funcao):
    novaLista = []
    for elemento in lista:
        novaLista.append(funcao(elemento))
    return novaLista

def reduz(lista, funcao):
    acumulador=lista[0]
    for i in range(1,len(lista)):
        acumulador=funcao(acumulador,lista[i])
    return acumulador

def primo(numero):
    if numero == 1:
        return False
    for i in range(2,int(sqrt(numero)+1)):
        if numero%i==0:
            return False
    return True

def quadrado(numero):
    return numero*numero

def soma(a,b):
    return a+b

def main():
    Entrada = input()
    if Entrada =="":
        print(0)
        return
    Entrada = Entrada.split()
    lista = []
    for elemento in Entrada:
        lista.append(int(elemento))
    lista=filtra(primo, lista)
    if len(lista)==0:
        print(0)
        return
    lista = mapeia(lista, quadrado)
    print(reduz(lista, soma))

main()
