from bordas import destacar_bordas
from modulo import *


def testar_bordas():
    larg, alt, imagem = carregar_imagem_codificada("testes/cross.in")
    imagem = decodificar(larg, alt, imagem)
    larg2, alt2, bordas_esperadas = carregar_imagem_codificada("testes/cross.res")
    bordas_esperadas = decodificar(larg2, alt2, bordas_esperadas)

    bordas_calculadas = destacar_bordas(larg, alt, imagem)

    escrever_imagem_decodificada(larg,alt,bordas_calculadas,"testes/teste.txt")
    escrever_imagem_decodificada(larg, alt, bordas_esperadas, "testes/testeres.txt")
    assert bordas_esperadas == bordas_calculadas



testar_bordas()
