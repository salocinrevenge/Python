from random import randint

from jogador import Jogador
from objeto import Objeto
import pygame
from objeto import Objeto


class Handler:
    def __init__(self, altura, largura):
        self.reset(altura,largura)

    def reset(self,altura,largura):
        self.score=0
        self.objetos = []
        self.deletar = []
        self.start = False
        self.time = 0
        self.haJogadores = True
        self.telaAlt = altura
        self.telaLarg = largura
        fundo = Objeto(0, -30, "imagens/fundo.png", "background")
        fundo.velX = -1
        gramado = Objeto(0, altura - 80, "imagens/gramado.png", "gramado")
        gramado.velX = -2
        chão = Objeto(0, altura - 30, "imagens/chão.png", "chão")
        chão.velX = -5
        flappy = Jogador(largura // 4, altura // 2, "imagens/flappy.png", "flappy")
        self.adicionarObjeto(fundo)
        self.adicionarObjeto(gramado)
        self.adicionarObjeto(chão)
        self.adicionarObjeto(flappy)

    def render(self, screen):
        tmpID = 0
        for obj in self.objetos:
            if obj.classe == "chão":
                tmpID = obj.id
            else:
                obj.render(screen)
        self.objetos[tmpID].render(screen)

    def tick(self):
        if self.time % 30==1:
            print(self.score)
        if self.start:
            self.time += 1
        if len(self.deletar) > 0:
            for id in self.deletar:
                for i, obj in enumerate(self.objetos):
                    if obj.id == id:
                        del (self.objetos[i])
                        break
            self.deletar.clear()
            self.atualizarIds()
        self.spawner()
        self.fundos()
        for obj in self.objetos:
            obj.tick()
        self.colisoes()
        self.canos()
        self.acharJogadores()

    def adicionarObjeto(self, objeto):
        self.objetos.append(objeto)
        self.objetos[len(self.objetos) - 1].setID(len(self.objetos) - 1)

    def deletarObjeto(self, id):
        self.deletar.append(id)

    def atualizarIds(self):
        for i, obj in enumerate(self.objetos):
            obj.setID(i)

    def limpar(self):
        self.objetos.clear()

    def comandos(self, comando):
        if comando == "pular":
            for obj in self.objetos:
                if obj.classe == "flappy":
                    obj.pular()
                    break
        if comando == "start":
            self.start = True
            for obj in self.objetos:
                if obj.classe == "flappy":
                    obj.start = True

    def spawner(self):
        if self.start:
            if self.time % 100 == 0:
                self.spawnObstaculo()

    def spawnObstaculo(self):
        posY = randint(40, self.telaAlt - 200)
        canoCima = Objeto(self.telaLarg, 0, "imagens/UGCano.png", "cano")
        canoCima.y = posY - canoCima.altura
        canoCima.velX = -5
        canoBaixo = Objeto(self.telaLarg, 100, "imagens/DGCano.png", "cano")
        canoBaixo.y = canoCima.y + canoCima.altura + 160
        canoBaixo.velX = -5
        self.adicionarObjeto(canoCima)
        self.adicionarObjeto(canoBaixo)

    def colisoes(self):
        for obj in self.objetos:
            if obj.classe == "flappy":
                if not obj.vivo:
                    self.deletarObjeto(obj.id)
                    break
                for obj2 in self.objetos:
                    if obj2.classe == "chão" or obj2.classe == "cano":
                        if obj2.rectRectColision(obj.x, obj.y, obj.largura, obj.altura):
                            obj.vivo = False
                            break

    def fundos(self):
        for obj in self.objetos:
            if obj.classe in {"background","gramado","chão"}:
                if obj.x<=-obj.largura//2:
                    obj.x=0

    def canos(self):
        for obj in self.objetos:
            if obj.classe=="cano":
                if self.telaLarg//4-4<=obj.x<=self.telaLarg//4:
                    self.score+=0.5
                if obj.x<=-obj.largura:
                    self.deletarObjeto(obj.id)

    def acharJogadores(self):
        for obj in self.objetos:
            if obj.classe=="flappy":
                return
        else:
            self.haJogadores=False
            return
