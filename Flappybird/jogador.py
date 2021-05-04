from objeto import Objeto


class Jogador(Objeto):
    velMax=20
    vivo = True
    start=False
    pulando = False

    def render(self, screen):
        screen.blit(self.imagem, (int(self.x), int(self.y)))

    def tick(self):
        if self.vivo and self.start:
            self.inteligencia()
            if self.pulando:
                self.pulando = False
                self.velY=-14

            self.velY=self.clamp(self.velY,self.velMax*-1,self.velMax)
            self.velY+=self.gravity
            self.x += self.velX
            self.y += self.velY

    def inteligencia(self):
        pass

    def pular(self):
        self.pulando = True
