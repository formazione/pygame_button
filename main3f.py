import pygame
import pygame.gfxdraw
from code.buttons2 import *

# pygame.init()


def buttons_def():
    b0 = Button((10, 10), "Click", 55, "black on white",
        command=print_hello)
    b1 = Button((10, 100), "Run", 40, "black on red")

    b2 = Button((10, 170), "Save", 36, "red on yellow",
        hover_colors="blue on orange", style=2, borderc=(255,255,0))

game_on = 0
def loop():
    # BUTTONS ISTANCES
    game_on = 1
    buttons_def()
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game_on = 0
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    game_on = 0
        if game_on:
            buttons.update()
            buttons.draw(screen)
        else:
            pygame.quit()
            sys.exit()
        buttons.draw(screen)
        clock.tick(60)
        pygame.display.update()
    pygame.quit()




loop()
