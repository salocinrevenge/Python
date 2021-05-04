def unir(lista1,lista2):
    resposta=[]
    ponteiro1=0
    ponteiro2=0
    for _ in range(len(lista1)+len(lista2)):
        if ponteiro1==len(lista1):
            resposta+=lista2[ponteiro2:len(lista2)]
            break
        if ponteiro2==len(lista2):
            resposta+=lista1[ponteiro1:len(lista1)]
            break
        if lista1[ponteiro1]<=lista2[ponteiro2]:
            resposta.append(lista1[ponteiro1])
            ponteiro1+=1
        else:
            resposta.append(lista2[ponteiro2])
            ponteiro2 += 1
    return resposta



def organizar(listas):
    if len(listas)==1:
        return listas[0]
    else:
        for i in range(1,(len(listas)//2)+1,1):
            listas[i-1]=unir(listas[i],listas.pop(i-1))
        return organizar(listas)


def main():
    #receber
    lista=list(map(int,input().split()))

    #organizar
    listas=[]
    for i in lista:
        listas.append([i])
    lista=organizar(listas)

    #mostrar
    for i in lista:
        print(i,end=" ")
    print()
main()