import pygame
import pygame.gfxdraw
from buttons import *

pygame.init()


def loop():
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        buttons.update()
        buttons.draw(screen)
        clock.tick(60)
        pygame.display.update()
    pygame.quit()

# BUTTONS ISTANCES
b0 = Button((10, 10), "Click", 55, "black on white")
b1 = Button((10, 100), "Run", 40, "black on red")

b2 = Button((10, 170), "Save", 36, "red on yellow",
    hover_colors="blue on orange", style=2, borderc=(255,255,0))

loop()
