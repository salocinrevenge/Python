def calcular(registro,num):
    pass
    if num==1:
        return registro
    else:
        if num % 2 == 0:
            num /= 2
        else:
            num = ((num * 3) + 1) / 2
        return calcular(registro+1,num)

def main():
    print(calcular(0,int(input())))

main()