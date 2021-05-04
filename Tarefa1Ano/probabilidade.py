#
# Algoritmo por Nícolas Hecker Silva, RA:186132
# Este programa lê uma lista de numeros naturais, analisa a frequencia deles e cria uma
# segunda lista com os números em ordem crescente de peso de valor
#



def criarSequenciaSemRepetir(lista):
    """

    :param lista: Uma lista com valores naturais sem ordem e com possiveis repetiçoes
    :return: retorna a lista com nenhum valor repetido
    """
    newList = []    # Cria a lista a ser devolvida
    for elemento in lista:  #Percorre toda a lista original
        if len(newList) == 0:
            newList.append(elemento)    #O primeiro valor nunca será repetido (essa linha tambem previne o erro de lista vazia)
        else:
            for jaCopiados in newList:
                if elemento == jaCopiados: #verifica se o elemento já foi copiado
                    break
            else: #Caso o for tenha sido concluido sem interrupçoes (Não houver valores repetidos)
                newList.append(elemento) #adiciona o elemento
    return newList #retorna a lista sem repetiçoes


def calcularQuantidades(original, secundaria, quantidades):
    """
    Atribui as quantidades de elementos repetidos na da lista secundaria na original à lista "quantidades"
    :param original: lista com numeros naturais se restriçoes
    :param secundaria: variação da lista "original" sem valores repetidos
    :param quantidades: lista, com o mesmo numero de 0s que elementos em "secundaria", a receber a frequqncia de cada valor
    :return: Não retorna
    """
    for i,item in enumerate(secundaria):#Percorre a lista secundaria recebendo seu indice
        for itemoriginais in original:#Percorre os itens originais para identificar os itens iguais
            if item == itemoriginais:
                quantidades[i]+=1   #Caso aja itens iguais ao analizado, incrementa a frequencia desse valor

def acharPos(lista,numero,valores,peso,inicio,fim):
    """
    Função recursiva para achar a posição correta a ser utilizada em "organizarLista()"
    Esta função encontra a posição de um item dado (contendo o numero e sua frequencia),
    em um intervalo definido
    :param lista: a lista na qual o valor deve ser organizado
    :param numero: o valor numerico do elemento
    :param valores: a lista de frequencias organizada de forma respectiva com "valores"
    :param peso: a frequencia do elemento
    :param inicio: a posição do inicio (int) do intervalo analizado
    :param fim: a posição do fim (int) do intervalo analisado
    :return: retorna a posição correta do elemento
    """
    if fim==(inicio + 1): #caso o intervalo contenha apenas dois numeros
        if peso<valores[inicio]:    #verifica por frequencia a posição do elemento
            return inicio
        elif peso>valores[inicio]:
            return fim
        else: #caso os pesos sejam iguais
            if numero<lista[inicio]:    #verifica por valor a posição do elemento
                return inicio
            else:
                return fim
    else:
        diferenca=fim-inicio    #recebe o tamanho do intervalo
        if peso>valores[inicio+(diferenca//2)]: #verifica se o elemento deve estar na segunda metade do intervalo por peso
            return acharPos(lista,numero,valores,peso,inicio+(diferenca//2),fim)
        elif peso<valores[inicio+(diferenca//2)]:#verifica se o elemento deve estar na primeira metade do intervalo por peso
            return acharPos(lista, numero, valores, peso, inicio, inicio + (diferenca // 2))
        else: #caso os pesos sejam iguais
            if numero<lista[inicio+(diferenca//2)]:#verifica se o elemento deve estar na primeira metade do intervalo por valor
                return acharPos(lista, numero, valores, peso, inicio, inicio + (diferenca // 2))
            else:# o elemento deve estar na segunda metade do intervalo por valor
                return acharPos(lista,numero,valores,peso,inicio+(diferenca//2),fim)



def organizarLista(lista, frequencia):
    """
    Esta função recebe uma lista de valores e outra de frequqncias e, para
    cada valor, encontra a posição devida, e a insere lá
    :param lista: Uma lista com valores não organizados, porém não repetidos
    :param frequencia: Uma lista com as frequencias na mesma posição que a primeira lista dada
    :return: Não retorna nada
    """
    for i in range(len(lista)): #for utilizando range, pois os valores são modificados no processo
        if i==0:    # O primeiro valor já está organizado
            continue
        pos=acharPos(lista,lista[i],frequencia,frequencia[i],0,i) #utiliza a função para atribuir a posição correta para esse valor na variavel "pos"
        #a função acima utiliza o início em 0 e fim em i, de forma a separar a lista original em duas: a parte organizada
        #e a não organizada (depois de i). Assim, ao terminar de incrementar "i" a lista estará completamente organizada.
        lista.insert(pos,lista[i]) #coloca o valor analisado na posição correta
        lista.pop(i+1)#retira o valor da sua antiga posição
        frequencia.insert(pos,frequencia[i]) #realiza as duas operaçoes acima com a lista de frequencias
        frequencia.pop(i+1)

def main():
    '''
        Esta é a função principal, que possui o papel de receber a lista,
        executar as funçoes de organização, criação de uma lista secundária
         e imprimir os valores obtidos
    :return: Não retorna nada
    '''

    Entrada = input().split() #Recebe os valores e os separa retirando os espaços
    L = [] #Cria a lista "original"
    for elemento in Entrada:
        L.append(int(elemento)) #Coloca os elementos de Entrada na lista "original" (foi a forma mais eficiente que encontrei)
    noRepet = criarSequenciaSemRepetir(L) #Cria sequencia sem repetir
    quantidades = []    # Cria uma lista para armazenar a frequencia de cada valor
    for _ in noRepet:
        quantidades.append(0)  # inicializa "quantidades" com 0s na quantia de numeros em noRepet
    calcularQuantidades(L, noRepet, quantidades) # atribui as respectivas quantidades para "quantidades"
    organizarLista(noRepet,quantidades) #Organiza a lista com base nos critérios exigidos
    for elemento in noRepet:
        print(elemento,end=" ") #imprime a lista final


main() #chama a função principal