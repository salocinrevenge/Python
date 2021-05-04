def acharDiferença(lista):
    p1=0
    p2=len(lista)-1
    if p1==p2:
        return lista[0]
    t1=int(lista[p1])
    t2=int(lista[p2])
    while p2-p1>1:
        if t1<=t2:
            p1+=1
            t1+=int(lista[p1])
        else:
            p2-=1
            t2+=int(lista[p2])
    return abs(t1-t2)

def main():
    while True:
        try:
            nTarefas=input()
            dificuldades=input().split()
            print(acharDiferença(dificuldades))
        except:
            break

main()