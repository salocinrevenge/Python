# -*- coding: UTF-8 -*-
from math import ceil


def ler_texto(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        texto=[]
        for linhaOriginal in arquivo:
            if linhaOriginal=="\n":
                continue
            texto.append(linhaOriginal.split())
        return texto

def remover_pontuacao(palavra,pontuacao):
    novapalavra=""
    for letra in palavra:
        if letra not in pontuacao:
            novapalavra+=letra
    return novapalavra

def contar_palavras(texto,stop_words,pontuacao):
    palavrasContadas=[]
    palavrasRegistradas=set()
    for linha in texto:
        for palavra in linha:
            novapalavra = remover_pontuacao(palavra,pontuacao).lower()
            if novapalavra in stop_words:
                continue
            if novapalavra not in palavrasRegistradas:
                palavrasRegistradas.add(novapalavra)
                palavrasContadas.append([novapalavra,1])
            else:
                for contadas in palavrasContadas:
                    if contadas[0] == novapalavra:
                        contadas[1]+=1
                        break
                else:
                    print("Algo deu errado em achar palavra em palavras ja contadas")
    return palavrasContadas

def segundovalor(lista_ou_tupla):
    return lista_ou_tupla[1]
def remover_pouco_frequentes(palavras,limiteinferior):
    novaPalavras = []
    for palavra in palavras:
        if palavra[1]>limiteinferior:
            novaPalavras.append(palavra)
        else:
            break
    return novaPalavras

def contar_acima_limite_de_freuqncia(palavrasContadas,limite):
    contador=0
    for palavra in palavrasContadas:
        if palavra[1]<limite:
            break
        contador+=1
    return contador

def responder3(lista,ultimoContado):
    contador=0
    for i in range(ultimoContado,len(lista)):
        if contador>2:
            break;
        if not contador==2:
            print(lista[i][0],end=" ")
        else:
            print(lista[i][0])
        contador+=1


def main():
    pontuacao= {".", ",", "?", "!", "'", ";", ":"}
    caminho=input()
    stop_words=set(input().split())
    texto = ler_texto(caminho)
    palavrasContadas=contar_palavras(texto,stop_words,pontuacao)
    palavrasContadas.sort()
    palavrasContadas.sort(key = segundovalor,reverse=True)
    print(f"{palavrasContadas[0][0]} {palavrasContadas[1][0]} {palavrasContadas[2][0]}")
    palavrasContadas=remover_pouco_frequentes(palavrasContadas,5)
    limite=palavrasContadas[(ceil(len(palavrasContadas)/4))-1][1]
    #print(f"limite: {limite}")
    #print(palavrasContadas)
    resposta2=contar_acima_limite_de_freuqncia(palavrasContadas,limite)
    print(resposta2)
    responder3(palavrasContadas,resposta2)

main()