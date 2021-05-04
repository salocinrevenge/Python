def verificarNota(linha):
    """
    Esta função procura a letra D no texto dado supondo uma entrada válida (se o D estiver sozinho, ele será uma nota)
    :param linha: A linha do texto a verificar as notas
    :return: retorna True se possuir alguma nota "D", ou False se não possuir
    """
    for palavra in linha:
        if palavra == "D":
            return True
    else:
        return False

def verificarPresenca(listaDePresenca):
    """
    Esta função verifica a porcentagem de presença do aluno
    :return: True se >=75%, False se <75%
    """
    faltas = 0
    for estadoNaAula in listaDePresenca:
        if estadoNaAula == "faltou":
            faltas += 1

    if faltas/len(listaDePresenca)>0.25: #ou presença >=0.75
        return False
    else:
        return True

def ler_presenca():
    """
    Esta função lê as proximas linhas e retorna o conteúdo quando não houverem mais linhas a se ler
    :return: lista com as strings dadas na entrada
    """
    lista_presenca = []
    while True:  # Não sei quantas linhas a entrada possui
        try:
            lista_presenca.append(input()) #pode dar erro

        except:  # Se acabou o documento
            return lista_presenca

def main():
    """
    função principal, chama funçoes para verificar nota, ler presença e verifica-la
    :return: nada
    """
    if verificarNota(input().split()):
        print("Reprovadx")
        return
    listaDePresenca = ler_presenca()
    if verificarPresenca(listaDePresenca):
        print("Aprovadx")
    else:
        print("Reprovadx")

main()