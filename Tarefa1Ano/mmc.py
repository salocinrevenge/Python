#mmc*mdc=produto
#mmc=produto/mdc

def calcularMDC(num1,num2):
    if num2==0:
        return num1
    else:
        return calcularMDC(num2,num1%num2)

def calcularMMC(num1,num2):
    return (num1*num2)//calcularMDC(num1,num2)

def main():
    par=tuple(map(int,input().split()))
    par=(max(par[0],par[1]),min(par[0],par[1]))
    print(calcularMMC(par[0],par[1]))

main()

#para entrada "278943861 849435618", a saída é "78981616985280368", mas era esperado "78981616985280366"