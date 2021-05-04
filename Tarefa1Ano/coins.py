moedas=(100.00,50.00,20.00,10.00,5.00,2.00,1.00,0.5,0.25,0.1,0.05,0.01)

def DarDinheiro(valor, dizNota, dizMoeda):
    for moeda in moedas:
        if not moeda > valor:
            nMoedas=int(valor*100)//int(moeda*100)
            if moeda>1.5:
                if dizNota==True:
                    print("NOTAS:")
                    dizNota=False
                print(str(nMoedas)+" nota(s) de R$ {:.2f}".format(moeda))
            else:
                if dizMoeda:
                    print("MOEDAS:")
                    dizMoeda=False
                print(str(nMoedas)+" moeda(s) de R$ {:.2f}".format(moeda))
            return valor-(moeda*nMoedas),dizNota,dizMoeda

def main():
    valor=float(input())
    dizNota = True
    dizMoeda = True
    while valor>0.001:
        valor,dizNota,dizMoeda=DarDinheiro(valor,dizNota,dizMoeda)




main()