fx =dict()

def calcularFib(Nfib):
    global fx
    try:
        return fx[str(Nfib)]
    except:
        if Nfib <=2:
            return Nfib
        else:
            res=calcularFib(Nfib-1)+calcularFib(Nfib-2)+calcularFib(Nfib-3)
            fx[str(Nfib)]=res
            return res

def main():
    print(calcularFib(int(input())))

main()