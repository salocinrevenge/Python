import pygame
from handler import Handler

HEIGHT = 650
WIDTH = 480
reset=False


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
# icon = pygame.image.load("pacIcon.png")
# pygame.display.set_icon(icon)


def render(handler,tela):
    handler.render(tela)
    pygame.display.update()


def tick(handler):
    global reset
    if handler.haJogadores:
        handler.tick()
    else:
        reset=True


def main():
    global reset
    running = True
    clock = pygame.time.Clock()
    fps = 30
    handler = Handler(HEIGHT,WIDTH)
    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    handler.comandos("pular")
                    handler.comandos("start")

        if not running:
            break
        if reset:
            handler.reset(HEIGHT,WIDTH)
            reset=False
        tick(handler)
        render(handler,screen)

main()