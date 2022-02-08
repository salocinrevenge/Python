"""
Rubiks 2x2 cube solver by Nicolas Hecker in Portuguese
o cubo eh passado atraves de um txt dado por:
..BB....
..BB....
WWRRYYOO
WWRRYYOO
..GG....
..GG....
em suas cores (em ingles) originais e:
..LL....
..LL....
FFUUBBDD
FFUUBBDD
..RR....
..RR....
suas posicoes.
W= branco; B= azul; Y= amarelo; R= vermelho; O= laranja; G= Verde
L= esquerda; U= Cima; R= direita; B= tras; D= baixo; F= frente

"""

cubosMontados = []

def mostrar(cubo):
    '''
    mostra o cubo como um origami de cubo 2d completado com pontos
    '''
    for linha in cubo:
        for letra in linha:
            print(letra,end="")
        print()
    print()

def criarCubo(caminho):
    cubo = []   #matriz de caracteres
    try:
        with open(caminho) as arquivo:    #criar o cubo a partir de arquivo txt
            texto = arquivo.readlines() #le tudo do arquivo
            for linha in texto:
                linhaAlvo = []
                for letra in linha.strip():
                    linhaAlvo.append(letra)
                cubo.append(linhaAlvo)
    except FileNotFoundError:
        print("Arquivo faltante nos cubos montados para comparação!")
        exit(-1)

    #mostrar(cubo)
    return cubo

def copiarCubo(parCubo):
    """
    receber um cubo (par de cubo e caminho) e criar um novo cubo identico
    ao original
    Retorna o novo cubo
    """
    cuboNovo = ([],parCubo[1])
    for linha in parCubo[0]:
        novaLinha = []
        for charac in linha:
            novaLinha.append(charac)
        cuboNovo[0].append(novaLinha)
    return cuboNovo

def terminou(cubo):
    """
    retornar True se o cubo estiver montado ou False se ainda nao estiver
    """
    global cubosMontados
    if len(cubosMontados) == 0:
        for i in range(24):
            cubosMontados.append(criarCubo("montados/"+str(i)+".txt"))

    for montado in cubosMontados:
        if cubo == montado:
            return True
    return False

def criarNovosCubos(parCubo,visitados,novos):
    """
    pegar o cubo dado (par de cubo com movimento), realizar 6 movimentos com 
    esse cubo, verificar se esses novos cubos são realmente novos (ou seja, não
    estão contidos em visitados), verifica se o cubo gerado não está montado
    ainda e o adiciona tanto em novos quanto em visitados.
    Retorna quando todos os movimentos forem feitos ou quando um cubo estiver
    montado.
    Retorno: True se montado, False se nenhum movimento resolve o cubo.
    
    """
    movimentos = ("f","f'","u","u'","r","r'")
    for i in range(6):
        novoParCubo = copiarCubo(parCubo)
        acao(novoParCubo[0],movimentos[i])
        novoParCubo=(novoParCubo[0],novoParCubo[1]+movimentos[i])
        novo = True
        for cubosVisitados in visitados:
            if novoParCubo[0] == cubosVisitados[0]:
                novo = False
        if not novo:
            continue
        finalizado = False
        if terminou(novoParCubo[0]):
            finalizado = True
        novos.append(novoParCubo)
        visitados.append(novoParCubo)
        if finalizado:
            return True
    return False

def resolver(cubo):
    """
    receber um cubo e retornar a sequencia de movimentos que resolve esse cubo

    """
    visitados = []
    novos = []
    visitados.append((cubo,""))
    novos.append((cubo,""))
    resolvido = False
    while not resolvido: #enquanto o cubo nao for resolvido
        for cuboNovo in novos:  #possivel erro nessa linha!! TODO
            if criarNovosCubos(cuboNovo,visitados,novos):
                resolvido = True
                break
            novos.remove(cuboNovo)
    print("O cubo foi resolvido com essa sequencia: "+novos[len(novos)-1][1])

def girarFH(cubo):
    '''
    rotaciona a face do cubo no sentido horario
    
    '''
    cubo[2][0], cubo[3][0],cubo[3][1],cubo[2][1] = cubo[3][0],cubo[3][1],cubo[2][1],cubo[2][0]  #rotacao na face
    cubo[2][2], cubo[0][2], cubo[3][7], cubo[4][2] = cubo[0][2], cubo[3][7], cubo[4][2], cubo[2][2] #rotacao em uma lateral
    cubo[3][2], cubo[1][2], cubo[2][7], cubo[5][2] = cubo[1][2], cubo[2][7], cubo[5][2], cubo[3][2] #rotacao na segunda lateral
    
def girarFA(cubo):
    '''
    rotaciona a face do cubo no sentido antihorario
    
    '''
    cubo[2][0], cubo[2][1],cubo[3][1],cubo[3][0] = cubo[2][1],cubo[3][1],cubo[3][0],cubo[2][0]  #rotacao na face
    cubo[0][2], cubo[3][7], cubo[4][2], cubo[2][2] = cubo[2][2], cubo[0][2], cubo[3][7], cubo[4][2] #rotacao em uma lateral
    cubo[1][2], cubo[2][7], cubo[5][2], cubo[3][2] = cubo[3][2], cubo[1][2], cubo[2][7], cubo[5][2] #rotacao em outra lateral

def girarBH(cubo):
    '''
    rotaciona a traseira do cubo no sentido horario
    
    '''
    cubo[2][5], cubo[3][5],cubo[3][4],cubo[2][4] = cubo[2][4],cubo[2][5],cubo[3][5],cubo[3][4]  #rotacao na face
    cubo[3][6], cubo[4][3], cubo[2][3], cubo[0][3] = cubo[0][3], cubo[3][6], cubo[4][3], cubo[2][3] #rotacao em uma lateral
    cubo[2][6], cubo[5][3], cubo[3][3], cubo[1][3] = cubo[1][3], cubo[2][6], cubo[5][3], cubo[3][3] #rotacao na segunda lateral

def girarBA(cubo):
    '''
    rotaciona a traseira do cubo no sentido antihorario
    
    '''
    cubo[2][4],cubo[2][5],cubo[3][5],cubo[3][4] = cubo[2][5], cubo[3][5],cubo[3][4],cubo[2][4] #rotacao na face
    cubo[0][3], cubo[3][6], cubo[4][3], cubo[2][3] = cubo[3][6], cubo[4][3], cubo[2][3], cubo[0][3] #rotacao em uma lateral
    cubo[1][3], cubo[2][6], cubo[5][3], cubo[3][3] = cubo[2][6], cubo[5][3], cubo[3][3], cubo[1][3] #rotacao na segunda lateral

def girarLH(cubo):
    '''
    rotaciona a esquerda do cubo no sentido horario
    
    '''
    cubo[0][3], cubo[1][3],cubo[1][2],cubo[0][2] = cubo[0][2],cubo[0][3],cubo[1][3],cubo[1][2]  #rotacao na face
    cubo[2][7], cubo[2][5], cubo[2][3], cubo[2][1] = cubo[2][1], cubo[2][7], cubo[2][5], cubo[2][3] #rotacao em uma lateral
    cubo[2][6], cubo[2][4], cubo[2][2], cubo[2][0] = cubo[2][0], cubo[2][6], cubo[2][4], cubo[2][2] #rotacao na segunda lateral
    
def girarLA(cubo):
    '''
    rotaciona a esquerda do cubo no sentido antihorario
    
    '''
    cubo[0][2],cubo[0][3],cubo[1][3],cubo[1][2] = cubo[0][3], cubo[1][3],cubo[1][2],cubo[0][2]  #rotacao na face
    cubo[2][1], cubo[2][7], cubo[2][5], cubo[2][3] = cubo[2][7], cubo[2][5], cubo[2][3], cubo[2][1] #rotacao em uma lateral
    cubo[2][0], cubo[2][6], cubo[2][4], cubo[2][2] = cubo[2][6], cubo[2][4], cubo[2][2], cubo[2][0] #rotacao em outra lateral

def girarRH(cubo):
    '''
    rotaciona a direita do cubo no sentido horario
    
    '''
    cubo[4][3], cubo[5][3],cubo[5][2],cubo[4][2] = cubo[4][2],cubo[4][3],cubo[5][3],cubo[5][2]  #rotacao na face
    cubo[3][0], cubo[3][6], cubo[3][4], cubo[3][2] = cubo[3][6], cubo[3][4], cubo[3][2], cubo[3][0] #rotacao em uma lateral
    cubo[3][1], cubo[3][7], cubo[3][5], cubo[3][3] = cubo[3][7], cubo[3][5], cubo[3][3], cubo[3][1] #rotacao em outra lateral
    
def girarRA(cubo):
    '''
    rotaciona a direita do cubo no sentido antihorario
    
    '''
    cubo[4][2],cubo[4][3],cubo[5][3],cubo[5][2] = cubo[4][3], cubo[5][3],cubo[5][2],cubo[4][2]  #rotacao na face
    cubo[3][6], cubo[3][4], cubo[3][2], cubo[3][0] = cubo[3][0], cubo[3][6], cubo[3][4], cubo[3][2] #rotacao em uma lateral
    cubo[3][7], cubo[3][5], cubo[3][3], cubo[3][1] = cubo[3][1], cubo[3][7], cubo[3][5], cubo[3][3] #rotacao na segunda lateral

def girarUH(cubo):
    '''
    rotaciona o topo do cubo no sentido horario
    
    '''
    cubo[2][3], cubo[3][3],cubo[3][2],cubo[2][2] = cubo[2][2],cubo[2][3],cubo[3][3],cubo[3][2]  #rotacao na face
    cubo[2][4], cubo[4][3], cubo[3][1], cubo[1][2] = cubo[1][2], cubo[2][4], cubo[4][3], cubo[3][1] #rotacao em uma lateral
    cubo[3][4], cubo[4][2], cubo[2][1], cubo[1][3] = cubo[1][3], cubo[3][4], cubo[4][2], cubo[2][1] #rotacao na segunda lateral
    
def girarUA(cubo):
    '''
    rotaciona o topo do cubo no sentido antihorario
    
    '''
    cubo[2][2],cubo[2][3],cubo[3][3],cubo[3][2] = cubo[2][3], cubo[3][3],cubo[3][2],cubo[2][2]  #rotacao na face
    cubo[1][2], cubo[2][4], cubo[4][3], cubo[3][1] = cubo[2][4], cubo[4][3], cubo[3][1], cubo[1][2] #rotacao em uma lateral
    cubo[1][3], cubo[3][4], cubo[4][2], cubo[2][1] = cubo[3][4], cubo[4][2], cubo[2][1], cubo[1][3] #rotacao em outra lateral

def girarDH(cubo):
    '''
    rotaciona a base do cubo no sentido horario
    
    '''
    cubo[2][7], cubo[3][7],cubo[3][6],cubo[2][6] = cubo[2][6],cubo[2][7],cubo[3][7],cubo[3][6]  #rotacao na face
    cubo[0][2], cubo[3][0], cubo[5][3], cubo[2][5] = cubo[2][5], cubo[0][2], cubo[3][0], cubo[5][3] #rotacao em uma lateral
    cubo[0][3], cubo[2][0], cubo[5][2], cubo[3][5] = cubo[3][5], cubo[0][3], cubo[2][0], cubo[5][2] #rotacao na segunda lateral
    
def girarDA(cubo):
    '''
    rotaciona a base do cubo no sentido antihorario
    
    '''
    cubo[2][6],cubo[2][7],cubo[3][7],cubo[3][6] = cubo[2][7], cubo[3][7],cubo[3][6],cubo[2][6]  #rotacao na face
    cubo[2][5], cubo[0][2], cubo[3][0], cubo[5][3] = cubo[0][2], cubo[3][0], cubo[5][3], cubo[2][5] #rotacao em uma lateral
    cubo[3][5], cubo[0][3], cubo[2][0], cubo[5][2] = cubo[0][3], cubo[2][0], cubo[5][2], cubo[3][5] #rotacao em outra lateral

def acao(cubo, codigoDoMovimento):
    '''passar o cubo e o codigo de giro e esta funcao chama a funcao correta'''
    if codigoDoMovimento[0] == 'f': #movimento frontal
        if len(codigoDoMovimento) >1 and codigoDoMovimento[1] == "'": #sentido antihorario
            girarFA(cubo)
        else:   #sentido horario
            girarFH(cubo)
        return
    if codigoDoMovimento[0] == 'b': #movimento traseiro
        if len(codigoDoMovimento) >1 and codigoDoMovimento[1] == "'": #sentido antihorario
            girarBA(cubo)
        else:   #sentido horario
            girarBH(cubo)
        return
    if codigoDoMovimento[0] == 'r': #movimento da direita
        if len(codigoDoMovimento) >1 and codigoDoMovimento[1] == "'": #sentido antihorario
            girarRA(cubo)
        else:   #sentido horario
            girarRH(cubo)
        return
    if codigoDoMovimento[0] == 'l': #movimento da esquerda
        if len(codigoDoMovimento) >1 and codigoDoMovimento[1] == "'": #sentido antihorario
            girarLA(cubo)
        else:   #sentido horario
            girarLH(cubo)
        return
    if codigoDoMovimento[0] == 'u': #movimento superior
        if len(codigoDoMovimento) >1 and codigoDoMovimento[1] == "'": #sentido antihorario
            girarUA(cubo)
        else:   #sentido horario
            girarUH(cubo)
        return
    if codigoDoMovimento[0] == 'd': #movimento inferior
        if len(codigoDoMovimento) >1 and codigoDoMovimento[1] == "'": #sentido antihorario
            girarDA(cubo)
        else:   #sentido horario
            girarDH(cubo)
        return
    print("A ação solicitada não foi catalogada e não pode ser executada!")
    return

def main(): #recebe o cubo do arquivo e chama as funcoes para gira-lo

    cubo = criarCubo("cubo.txt")
    mostrar(cubo)
    resolver(cubo)

    """
    if terminou(cubo):
        print("ta montado")
        return
    #receber comandos
    entrada = input("Insira ação: ")
    while entrada not in ["sair","escape","exit","quit","esc","0","s","q"]:
        acao(cubo,entrada)
        mostrar(cubo)
        terminou(cubo)
        entrada = input("Insira ação: ")
    """

main()

