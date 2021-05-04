from modulo import carregar_imagem_decodificada,carregar_imagem_codificada,escrever_imagem_decodificada,escrever_imagem_codificada,codificar,decodificar

def testar_leitura_pbm():
    largura, altura, imagem = carregar_imagem_decodificada("testes/jota.pbm")
    assert largura == 6

    assert altura == 10
    matriz_esperada = [
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['0', '0', '0', '0', '1', '0'],
        ['1', '0', '0', '0', '1', '0'],
        ['0', '1', '1', '1', '0', '0'],
        ['0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0'],
    ]
    assert imagem == matriz_esperada


def testar_leitura_p1c():
    largura, altura, imagem = carregar_imagem_codificada("testes/disquete.p1c")
    assert largura == 16

    assert altura == 16
    matriz_esperada =['1', '00', '14', '01', '2', '00', '1', '11', '1', '00', '1', '11', '8', '00', '1', '11', '1',
                      '01', '1', '11', '2', '00', '1', '11', '1', '00', '1', '11', '8', '00', '1', '11', '1', '00', '1',
                      '11', '2', '00', '1', '11', '1', '00', '1', '11', '8', '00', '1', '11', '1', '00', '1', '11', '2',
                      '00', '1', '11', '2', '00', '8', '10', '2', '00', '1', '11', '2', '00', '1', '11', '2', '00', '6',
                      '11', '2', '10', '1', '11', '1', '00', '1', '11', '2', '00', '1', '11', '2', '00', '6', '11', '2',
                      '00', '1', '11', '1', '00', '1', '11', '3', '00', '13', '10', '1', '00']

    assert imagem == matriz_esperada

def testar_escrever_imagem_decodificada():
    larg, alt, imagem = carregar_imagem_codificada("testes/cross.out")
    imagem = decodificar(larg, alt, imagem)
    escrever_imagem_decodificada(larg, alt, imagem, "testes/cruzout1.pbm")
    with open("testes/teste2.txt") as arquivo:
        texto = arquivo.readlines()
    with open("testes/feep.pbm") as arquivo:
        assert texto == arquivo.readlines()

def testar_escrever_imagem_codificada():
    larg,alt,imagem = carregar_imagem_decodificada("testes/feep.pbm")
    codificacao = codificar(larg,alt,imagem)
    escrever_imagem_codificada(larg, alt, codificacao, "testes/teste2.txt")
    with open("testes/teste2.txt") as arquivo:
        texto = arquivo.readlines()
    with open("testes/feep.p1c") as arquivo:
        assert texto == arquivo.readlines()

testar_escrever_imagem_decodificada()