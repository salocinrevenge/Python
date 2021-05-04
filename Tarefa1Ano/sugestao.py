def receber_pares_palavras():
    texto = []
    while True:
        try:
            linha = input().split()
            texto.append(linha)
        except:
            return texto


def receber_texto(caminho):
    texto = []
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if linha == "\n":
                continue
            texto.append(linha.lower().split())
        return texto


def remover_pontuacao(palavra, pontuacao):
    novapalavra = ""
    for letra in palavra:
        if letra not in pontuacao:
            novapalavra += letra
    return novapalavra

def nova(lista,palavra):
    for i in range(len(lista)):
        if lista[i][0]==palavra:
            return i
    return -1

def receber_sugestoes_contadas2(texto,pares_palavras,pontuacao):
    sugestoes=[]
    for _ in pares_palavras:
        sugestoes.append([])
    for linhaTexto in texto:
        for posicaoPalavra in range(len(linhaTexto)):
            for posPar_palavra in range(len(pares_palavras)):
                try:
                    if remover_pontuacao(pares_palavras[posPar_palavra][0],pontuacao)==remover_pontuacao(linhaTexto[posicaoPalavra],pontuacao) and remover_pontuacao(pares_palavras[posPar_palavra][1],pontuacao)==remover_pontuacao(linhaTexto[posicaoPalavra+1],pontuacao):
                        try:
                            posicaoNaSugestao=nova(sugestoes[posPar_palavra], remover_pontuacao(linhaTexto[posicaoPalavra+2],pontuacao))
                        except:
                            posicaoNaSugestao = -1
                        if posicaoNaSugestao<0:
                            try:
                                sugestoes[posPar_palavra].append([remover_pontuacao(linhaTexto[posicaoPalavra+2],pontuacao),1])
                            except:
                                pass
                        else:
                            sugestoes[posPar_palavra][posicaoNaSugestao][1]+=1
                except:
                    pass
    return sugestoes


def organizar(matriz):
    for linha in matriz:
        linha.sort()
        linha.sort(key=lambda x:x[1],reverse=True)

def mostrar_resposta(pares,sugestoes):
    for i in range(len(pares)):
        print(f"{pares[i][0]} {pares[i][1]} {sugestoes[i][0][0]}")

def main():
    caminho = input()
    pares_palavras = receber_pares_palavras()
    texto = receber_texto(caminho)
    pontuacao = {".", ",", "?", "!", "'", ";", ":"}
    sugestoes=receber_sugestoes_contadas2(texto, pares_palavras, pontuacao)
    organizar(sugestoes)
    mostrar_resposta(pares_palavras,sugestoes)


main()
