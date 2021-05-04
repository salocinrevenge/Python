import pygame

class Objeto:
    pygame.init()
    velX=0
    velY=0
    def __init__(self, x, y, localImagem,classe):
        self.gravity=1.5
        self.x = x
        self.y = y
        self.imagem = pygame.image.load(localImagem).convert_alpha()
        self.largura,self.altura=self.imagem.get_size()
        self.classe = classe

    def render(self, screen):
        screen.blit(self.imagem, (int(self.x), int(self.y)))

    def tick(self):
        self.x += self.velX
        self.y += self.velY

    def setID(self,id):
        self.id=id

    def clamp(self,num,min,max):
        if min>num:
            return min
        elif max<num:
            return max
        else:
            return num

    def pointRectColision(self,x,y):
        if self.x<=x<=self.x+self.largura and self.y<=y<=self.y+self.altura:
            return True
        else:
            return False
    def rectRectColision(self,x,y,largura,altura):
        if self.pointRectColision(x,y) or self.pointRectColision(x+largura,y) or self.pointRectColision(x,y+altura) or self.pointRectColision(x+largura,y+altura):
            return True
        else:
            return False