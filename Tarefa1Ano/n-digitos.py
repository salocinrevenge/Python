def elevado(base, expoente):
    res = 1
    for _ in range(expoente):
        res *= base
    return res


def somarDig(num):
    soma = 0
    for dig in str(num):
        soma += int(dig)
    return soma


def preencher0s(num, ordem):
    ndig = len(str(num))
    res = num * elevado(10, ordem - ndig)
    return res

def completar(num,soma):
    addDig=soma-somarDig(num)
    if len(str(addDig))==1:
        return num*10+addDig
    else:
        return -1

def encontrarValor(atual, ordem, soma):
    if len(str(atual))>=ordem:
        return
    if len(str(atual))==ordem-1:
        tmp2=completar(atual,soma)
        if tmp2>0:
            print(tmp2)
        return
    if somarDig(atual) == soma:
        print(preencher0s(atual, ordem))
        return
    else:
        if atual == 0:
            for tmp in range(1, 10):
                if somarDig(atual) + tmp <= soma:
                    encontrarValor(atual*10+tmp,ordem,soma)
                else:
                    break
        else:
            for tmp in range(0, 10):
                if somarDig(atual) + tmp <= soma:
                    encontrarValor(atual*10+tmp,ordem,soma)
                else:
                    break


def main():
    n, s = tuple(map(int, input().split()))
    encontrarValor(0, n, s)


main()
