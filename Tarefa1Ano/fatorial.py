def calcularFat(atual,NFatorial):
    if NFatorial ==0:
        return 1
    if NFatorial==1:
        return atual*1
    else:
        return atual*NFatorial*calcularFat(atual,NFatorial-1)

def main():
    print(calcularFat(1,int(input())))

main()