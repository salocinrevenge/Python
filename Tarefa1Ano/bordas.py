from modulo import *


def dentro(min, max, num):
    if min <= num < max:
        return True
    else:
        return False


def detectarElemento(linha, coluna, imagem, largura, altura):
    if dentro(0, altura, linha) and dentro(0, largura, coluna):
        return int(imagem[linha][coluna])
    else:
        return 0


def possui0Vizinho(linha, coluna, imagem, largura, altura):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == 0 or not j == 0:
                if detectarElemento(linha + i, coluna + j, imagem, largura, altura) == 0:
                    return True
    return False


def destacar_bordas(largura, altura, imagem):
    nova_imagem = []
    for i, linha in enumerate(imagem):
        nova_linha = []
        for j, elemento in enumerate(linha):
            if int(elemento) == 1:
                if possui0Vizinho(i, j, imagem, largura, altura):
                    nova_linha.append(1)
                else:
                    nova_linha.append(0)
            else:
                nova_linha.append(0)
        nova_imagem.append(nova_linha)
    return nova_imagem


def main():
    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
