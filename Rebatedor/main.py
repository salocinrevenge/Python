import pygame
from random import randint
from datetime import date, datetime

ALTURAJANELA = 650
LARGURAJANELA = 480

pygame.init()

screen = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Rebata a Bolinha")


def clamp(num, nmin, nmax):
    if num > nmax:
        return nmax
    if num < nmin:
        return nmin
    return num


def colidirRecPonto(x1, y1, x2, y2, X1, Y1):
    if x1 <= X1 <= x2:
        if y1 <= Y1 <= y2:
            return 1
    return 0


def colidirRetang(x1, y1, x2, y2, X1, Y1, X2, Y2):
    if colidirRecPonto(x1, y1, x2, y2, X1, Y1) == 1:
        return 1
    if colidirRecPonto(x1, y1, x2, y2, X2, Y1) == 1:
        return 1
    if colidirRecPonto(x1, y1, x2, y2, X1, Y2) == 1:
        return 1
    if colidirRecPonto(x1, y1, x2, y2, X2, Y2) == 1:
        return 1
    return 0


def criarJogo(cruzamento):
    cor = (randint(0, 255), randint(0, 255), randint(0, 255))
    bola = BolaI(cor)
    jogador = JogadorI(cor, bola, cruzamento)
    inverter = randint(0, 0)
    if inverter != 0:
        jogador.x = LARGURAJANELA - 20
    bola.setJogador(jogador)
    jogo = [jogador, bola]
    return jogo

def lerJogos(jogos):
    nome = "carregar.txt"
    with open(nome, 'r') as arquivo:
        for linha in arquivo:
            jogos.append(criarJogo(None))
            novaLinha = linha.split()
            posicaoDeLeitura = 9
            profundidade = 3
            i = j = k = 0
            while profundidade != 0:
                if novaLinha[posicaoDeLeitura] in {"neuronio", "axonio", "coluna"}:
                    posicaoDeLeitura += 2
                    continue
                if novaLinha[posicaoDeLeitura] == '<':
                    posicaoDeLeitura += 1
                    if profundidade == 2:
                        k = 0
                        j += 1
                    else:
                        k = 0
                        j = -1
                        i += 1
                    profundidade += 1
                    continue
                if novaLinha[posicaoDeLeitura] == '>':
                    profundidade += -1
                    posicaoDeLeitura += 1
                    continue

                jogos[len(jogos)-1][0].cerebro.camadas[i][j].pesosAxonios[k] = int(novaLinha[posicaoDeLeitura][:len(novaLinha[posicaoDeLeitura])-1])
                posicaoDeLeitura += 1
                k += 1
                # jogos[len(jogos)-1][0].x = LARGURAJANELA - 20
    return jogos

def criarJogos(quantidade, cruzamento):
    jogos = []
    if quantidade == 0:
        return lerJogos(jogos)
    for _ in range(quantidade):
        jogos.append(criarJogo(cruzamento))
    return jogos


def mostrarJogos(jogos, tela):
    for jogo in jogos:
        for elemento in jogo:
            elemento.mostrarObj(tela)


def tempoJogos(jogos):
    for jogo in jogos:
        for elemento in jogo:
            elemento.tempoObj()
            if elemento.tipo == "bolaI":
                if elemento.perdeu:
                    jogos.remove(jogo)


def cruzar(num1, num2):
    if num2 is None:
        num2 = num1
    opcao = randint(0, 4)
    if opcao == 0:
        return num1
    if opcao == 1:
        return (num1 * 3 + num2) // 4
    if opcao == 2:
        return (num1 + num2) // 2
    if opcao == 3:
        return (num2 * 3 + num1) // 4
    if opcao == 4:
        return num2


def mutar(num):
    chance = randint(1, 60)

    if chance == 1:
        return clamp(num * randint(-3, 3) + randint(-11, 11), -100, 100)
    if chance < 4:
        return clamp(num * randint(-2, 2) + randint(-11, 11), -100, 100)
    if chance < 7:
        return clamp(num * randint(-1, 1) + randint(-11, 11), -100, 100)
    if chance < 12:
        return clamp(num * randint(1, 1) + randint(-11, 11), -100, 100)
    return num


"""
def evoluir(individuos):
    pass
"""


class Neuronio:
    def __init__(self):
        self.valorPrincipal = 0
        self.axonios = []
        self.pesosAxonios = []

    def adicionarNeuronio(self, neuronio, pesoAxonio):
        self.axonios.append(neuronio)
        self.pesosAxonios.append(pesoAxonio)

    def somarValorPrincipal(self, valor):
        self.valorPrincipal += valor

    def resetValorPrincipal(self):
        self.valorPrincipal = 0

    def passarValorAdiante(self):
        for i, axonio in enumerate(self.axonios):
            axonio.somarValorPrincipal(self.valorPrincipal * self.pesosAxonios[i])


class Cerebro:
    def __init__(self, camadas, cruzamento):
        self.camadas = camadas
        self.resetNeuronios()
        if cruzamento is None or not cruzamento[0]:
            self.criarCerebroAleatorio()
        else:
            self.criarCerebroCruzando(cruzamento)

    def criarCerebroCruzando(self, cruzamento):
        for i in range(len(self.camadas) - 1):
            for j in range(len(self.camadas[i])):
                for k in range(len(self.camadas[i + 1])):
                    if cruzamento[1]:
                        self.camadas[i][j].adicionarNeuronio(self.camadas[i + 1][k], mutar(
                            cruzar(cruzamento[0][0].cerebro.camadas[i][j].pesosAxonios[k],
                                   cruzamento[1][0].cerebro.camadas[i][j].pesosAxonios[k])))
                    else:
                        self.camadas[i][j].adicionarNeuronio(self.camadas[i + 1][k], mutar(
                            cruzar(cruzamento[0][0].cerebro.camadas[i][j].pesosAxonios[k],
                                   None)))

    def criarCerebroAleatorio(self):
        for i in range(0, len(self.camadas) - 1):
            for neuronio in self.camadas[i]:
                for proxNeuronio in self.camadas[i + 1]:
                    neuronio.adicionarNeuronio(proxNeuronio, randint(-100, 100))

    def resetNeuronios(self):
        for camada in self.camadas:
            for neuronio in camada:
                neuronio.resetValorPrincipal()

    def lerDados(self, dX, dY, velXBola, velYBola, velYP):
        self.camadas[0][0].somarValorPrincipal(dX)
        self.camadas[0][1].somarValorPrincipal(dY)
        self.camadas[0][2].somarValorPrincipal(velXBola)
        self.camadas[0][3].somarValorPrincipal(velYBola)
        self.camadas[0][4].somarValorPrincipal(velYP)

    def passarTudoAdiante(self):
        for i in range(0, len(self.camadas) - 1):
            for neuronio in self.camadas[i]:
                for j in range(len(neuronio.axonios)):
                    if neuronio.valorPrincipal > 0:
                        neuronio.axonios[j].somarValorPrincipal(
                            (neuronio.valorPrincipal * neuronio.pesosAxonios[j]) // 100)

    def executarAcao(self):
        if self.camadas[len(self.camadas) - 1][0].valorPrincipal > 0:
            subir = 1
        else:
            subir = 0
        if self.camadas[len(self.camadas) - 1][1].valorPrincipal > 0:
            descer = 1
        else:
            descer = 0
        return subir, descer

    def mostrarCerebro(self):
        print("mostrando camadas")
        for i, camada in enumerate(self.camadas):
            print(f"camada {i}: ", end="")
            for j, neuronio in enumerate(camada):
                print(f"{j} {neuronio.valorPrincipal} ", end="")
            print()

    def decidirAcao(self, dX, dY, velXBola, velYBola, velYP):
        self.resetNeuronios()
        self.lerDados(dX, dY, velXBola, velYBola, velYP)
        self.passarTudoAdiante()
        # self.mostrarCerebro()
        return self.executarAcao()


def criarCamada(numNeuronios):
    camada = []
    for _ in range(numNeuronios):
        camada.append(Neuronio())
    return camada


def leitorPontosJogos(jogo):
    if jogo is None:
        return 0
    return jogo[1].pontos


class Organizador:
    def __init__(self, jogos):
        self.jogos = jogos
        self.geracao = 1
        self.melhor = None
        self.segundo = None
        self.tempo = 0
        self.selecionarPorPonto = False

    def organizarJogos(self):
        self.tempo += 1
        self.jogos.sort(key=leitorPontosJogos, reverse=True)
        interromper = False
        if self.tempo > 15000:
            interromper = True
            self.selecionarPorPonto = True
        if self.geracao > 40 and not self.selecionarPorPonto:
            self.geracao = 0
            self.jogos = criarJogos(200, None)
            return
        if len(self.jogos) == 0 or interromper:
            self.jogos = criarJogos(50, (self.melhor, self.segundo))
            self.geracao += 1
            self.tempo = 0
            self.melhor = None
            self.segundo = None
        if self.selecionarPorPonto:
            if leitorPontosJogos(self.melhor) < leitorPontosJogos(self.jogos[0]):
                self.segundo = self.melhor
                self.melhor = self.jogos[0]
            elif leitorPontosJogos(self.segundo) < leitorPontosJogos(self.jogos[0]) and self.melhor is not self.jogos[
                0]:
                self.segundo = self.jogos[0]
            elif len(self.jogos) > 1:
                if leitorPontosJogos(self.segundo) < leitorPontosJogos(self.jogos[1]):
                    self.segundo = self.jogos[1]
        else:
            self.melhor = self.jogos[0]
            if len(self.jogos) > 1:
                self.segundo = self.jogos[1]

    def mostrarOrganizador(self, tela):
        melhorTmp = self.melhor
        if melhorTmp:
            melhorTmp = self.melhor[1].pontos
        else:
            melhorTmp = 0
        segundoTmp = self.segundo
        if segundoTmp:
            segundoTmp = self.segundo[1].pontos
        else:
            segundoTmp = 0
        tela.blit(fonthud.render(f"Geracao: {self.geracao}, melhor: {melhorTmp}, segundo: {segundoTmp}", True,
                                 (122, 122, 122)),
                  (LARGURAJANELA // 2 - 160, 10))


class JogadorI:
    def __init__(self, cor, bola, cruzamento):
        self.cerebro = Cerebro([criarCamada(5), criarCamada(4), criarCamada(2)], cruzamento)
        self.bola = bola
        self.tipo = "jogador"
        self.x = 10
        self.y = randint(0, ALTURAJANELA - 50)
        self.aceleracao = 5
        self.velY = 0
        self.largura = 10
        self.altura = 50
        self.aparencia = pygame.Surface((self.largura, self.altura))
        self.aparencia.fill(cor)

    def mostrarObj(self, tela):
        tela.blit(self.aparencia, (self.x, self.y))

    def inteligencia(self):
        subir, descer = self.cerebro.decidirAcao(self.bola.x - self.x, self.bola.y - self.y, self.bola.velX,
                                                 self.bola.velY, self.aceleracao)
        if subir and descer:
            self.velY = 0
        elif subir and not descer:
            self.velY = -self.aceleracao
        elif descer and not subir:
            self.velY = self.aceleracao
        else:
            self.velY = 0

    def tempoObj(self):
        self.velY = 0
        self.inteligencia()
        self.y += self.velY
        self.y = clamp(self.y, 0, ALTURAJANELA - self.altura)
        return 0

    def comando(self, chave):
        if chave == 'w':
            self.velY += -self.aceleracao
            return
        if chave == 'nw':
            self.velY += self.aceleracao
            return
        if chave == 's':
            self.velY += self.aceleracao
            return
        if chave == 'ns':
            self.velY += -self.aceleracao
            return


class BolaI:
    def __init__(self, cor):
        self.perdeu = 0
        self.tipo = "bolaI"
        self.jogador = None
        self.pontos = 0
        self.tempo = 0
        self.x = 21
        self.y = randint(0, ALTURAJANELA - 50)
        self.velX = 3
        self.velY = randint(-3, 3)
        if self.velY == 0:
            self.velY = 3
        self.largura = 20
        self.altura = 20
        self.aparencia = pygame.Surface((self.largura, self.altura))
        pygame.draw.circle(self.aparencia, cor, (10, 10), 10)

    def setJogador(self, jogador):
        self.jogador = jogador

    def mostrarObj(self, tela):
        tela.blit(self.aparencia, (self.x, self.y))

    def tempoObj(self):
        self.tempo += 1
        if self.tempo > 15:
            self.tempo = 0
            if abs(self.jogador.y - self.y) < 30:
                self.pontos += 1
            if abs(self.jogador.y - self.y) < 10:
                self.pontos += 2

        self.colisao()
        self.x += self.velX
        self.y += self.velY
        if self.x + self.largura > LARGURAJANELA or self.x < 0:
            self.velX *= -1
        if self.y + self.altura > ALTURAJANELA or self.y < 0:
            self.velY *= -1
        if (self.x < 1 and self.jogador.x == 10) or (self.x + self.largura > LARGURAJANELA - 4 and self.jogador.x == LARGURAJANELA - 20):
            self.perdeu = True
            return 1
        return 0

    def colisao(self):
        if colidirRetang(self.jogador.x, self.jogador.y, self.jogador.x + self.jogador.largura,
                         self.jogador.y + self.jogador.altura, self.x, self.y, self.x + self.largura,
                         self.y + self.altura) == 1:
            self.velX *= -1
            self.pontos += 10


class Bola:
    def __init__(self):
        self.perdeu = 0
        self.tipo = "bola"
        self.pontos = 0
        self.x = 20
        self.y = ALTURAJANELA // 2 - 10
        self.velX = 3
        self.velY = 3
        self.largura = 20
        self.altura = 20
        self.aparencia = pygame.Surface((self.largura, self.altura))
        pygame.draw.circle(self.aparencia, (112, 39, 105), (10, 10), 10)

    def mostrarObj(self, tela, visivel):
        if visivel:
            mostrarHUD(tela, self.pontos)
            tela.blit(self.aparencia, (self.x, self.y))
            if self.perdeu:
                mostrarPerdeu(tela, self.pontos)

    def tempoObj(self):
        self.x += self.velX
        self.y += self.velY
        if self.x + self.largura > LARGURAJANELA:
            self.velX *= -1
        if self.y + self.altura > ALTURAJANELA or self.y < 0:
            self.velY *= -1
        '''if self.x < 1:
            self.perdeu = 1
            return 1'''
        return 0

    def colisao(self, elementos):
        for elemento in elementos:
            if elemento.tipo == "jogador":
                if colidirRetang(elemento.x, elemento.y, elemento.x + elemento.largura, elemento.y + elemento.altura,
                                 self.x, self.y, self.x + self.largura, self.y + self.altura) == 1:
                    self.velX *= -1
                    self.pontos += 1


class Fundo:
    def __init__(self):
        self.tipo = "fundo"
        self.x = 0
        self.y = 0
        self.largura = LARGURAJANELA
        self.altura = ALTURAJANELA
        self.aparencia = pygame.Surface((self.largura, self.altura))
        self.aparencia.fill((0, 0, 0))

    def mostrarObj(self, tela):
        tela.blit(self.aparencia, (self.x, self.y))


class Jogador:
    def __init__(self):
        self.tipo = "jogador"
        self.x = 10
        self.y = ALTURAJANELA // 2 - 25
        self.velY = 0
        self.largura = 10
        self.altura = 50
        self.aparencia = pygame.Surface((self.largura, self.altura))
        self.aparencia.fill((3, 187, 133))

    def mostrarObj(self, tela, visivel):
        if visivel:
            tela.blit(self.aparencia, (self.x, self.y))

    def tempoObj(self):
        self.y += self.velY
        self.y = clamp(self.y, 0, ALTURAJANELA - self.altura)
        return 0

    def comando(self, chave):
        if chave == 'w':
            self.velY += -5
            return
        if chave == 'nw':
            self.velY += 5
            return
        if chave == 's':
            self.velY += 5
            return
        if chave == 'ns':
            self.velY += -5
            return


# fontes
fontPause = pygame.font.Font('freesansbold.ttf', 30)
fonthud = pygame.font.Font('freesansbold.ttf', 20)


def mostrarPause(tela):
    tela.blit(fontPause.render("JOGO PAUSADO", True, (255, 100, 100)),
              (LARGURAJANELA // 2 - 110, ALTURAJANELA - 30))


def mostrarHUD(tela, pontos):
    tela.blit(fonthud.render(f"Pontuação: {pontos}", True, (122, 122, 122)),
              (LARGURAJANELA // 2 - 60, 10))


def mostrarPerdeu(tela, pontos):
    tela.blit(fontPause.render(f"Você Perdeu :(", True, (255, 100, 100)),
              (LARGURAJANELA // 2 - 110, ALTURAJANELA // 2 - 30))
    tela.blit(fontPause.render(f"Pontuação: {pontos}", True, (255, 100, 100)),
              (LARGURAJANELA // 2 - 100, ALTURAJANELA // 2))


def imprimirObjetos(organizador):
    jogos = organizador.jogos
    data = date.today()
    hora = datetime.now()
    nome = "{}-{}-{};{}-{}".format(data.day, data.month,
                                   data.year, hora.hour, hora.minute)
    conteudo = ""
    for i, jogo in enumerate(jogos):
        conteudo = conteudo + f"{i+1} jogador: < "
        for j, coluna in enumerate(jogo[0].cerebro.camadas):
            conteudo = conteudo + f"coluna {j+1}: < "
            for k, neuronio in enumerate(coluna):
                conteudo = conteudo + f"neuronio {k+1}: < "
                for m, axonio in enumerate(neuronio.pesosAxonios):
                    conteudo = conteudo + f"axonio {m+1}: {axonio}; "
                conteudo = conteudo + " > "
            conteudo = conteudo + " > "
        conteudo = conteudo + " >\n"
    with open(f"{nome}.txt", 'w') as arquivo:
        arquivo.writelines(conteudo)


def reset():
    objetos = [Bola(), Jogador()]
    perdeu = 0
    return objetos, perdeu


def tempo(objetos, pause, perdeu, organizador):
    if not pause and not perdeu:
        organizador.organizarJogos()
        tempoJogos(organizador.jogos)
        for obj in objetos:
            if obj.tempoObj():
                perdeu = True
            if obj.tipo == "bola":
                obj.colisao(objetos)
    return perdeu


def mostrar(tela, fundo, objetos, pause, organizador):
    fundo.mostrarObj(tela)
    mostrarJogos(organizador.jogos, tela)
    organizador.mostrarOrganizador(tela)
    for obj in objetos:
        obj.mostrarObj(tela, 0)
    if pause:
        mostrarPause(tela)
    pygame.display.update()


def main():
    pause = False
    running = True
    clock = pygame.time.Clock()
    fps = 60
    objetos, perdeu = reset()
    fundo = Fundo()
    jogos = criarJogos(20, None)
    organizador = Organizador(jogos)
    while running:
        clock.tick(fps)
        mostrar(screen, fundo, objetos, pause, organizador)
        perdeu = tempo(objetos, pause, perdeu, organizador)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and not pause:
                    objetos[1].comando('w')
                if event.key == pygame.K_s and not pause:
                    objetos[1].comando('s')
                if event.key == pygame.K_p:
                    if pause:
                        pause = False
                    else:
                        pause = True
                if event.key == pygame.K_UP:
                    fps = fps * 6
                if event.key == pygame.K_DOWN:
                    fps = clamp(fps // 6, 1, 10000)
                if event.key == pygame.K_i:
                    imprimirObjetos(organizador)
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    break
                if event.key == pygame.K_r:
                    objetos, perdeu = reset()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    objetos[1].comando('nw')
                if event.key == pygame.K_s:
                    objetos[1].comando('ns')


main()
# lerJogos([])
