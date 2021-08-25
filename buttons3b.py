
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self, screen, position, text, size, colors="white on blue"):
        super().__init__()
        self.colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        self.font = pygame.font.SysFont("Arial", size)
        self.text_render = self.font.render(text, 1, self.fg)
        self.image = self.text_render
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.update()
        buttons.add(self)

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))
        # screen.blit(self.text_render, self.position)

        # self.rect = screen, position, text, size, colors="white on blue"screen.blit(self.text_render, (self.x, self.y))



def start():
    print("Ok, let's go")


def not_hover():
    for x in buttons:
        x.colors = "red on yellow"
        x.update()

def menu():
    """ This is the menu that waits you to click the s key to start """


    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEMOTION:
                # 2. put the collide check for mouse hover here for each button
                if b0.rect.collidepoint(pygame.mouse.get_pos()):
                    b0.colors = "red on green"
                elif b1.rect.collidepoint(pygame.mouse.get_pos()):
                    b1.colors = "red on green"
                elif b2.rect.collidepoint(pygame.mouse.get_pos()):
                    b2.colors = "red on green"
                else:
                    # this will work for every buttons going back to original color after mouse goes out
                    not_hover()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 3. here the interactions with the click of the mouse... done
                if b0.rect.collidepoint(pygame.mouse.get_pos()):
                    print(b0.y)
                if b1.rect.collidepoint(pygame.mouse.get_pos()):
                    print(b1.y)
        buttons.update()
        buttons.draw(screen)
        pygame.display.update()
    pygame.quit()
# 1 - create the buttons with an istance of Button here...
b0 = Button(screen, (10, 10), "1st button (b0) at b0 = 10", 55, "red on yellow")
b1 = Button(screen, (10, 100), "2nd button (b1) at b1 = 100", 55, "red on yellow")
# This button has no interaction (69 add...)
b2 = Button(screen, (10, 200), "3rd button - no action", 55, "red on yellow")
print(b0.x)
# follow the comments to add buttons:
# 1 - create the buttons with an istance of Button here... line 80
# 2. put the collide check for mouse hover here for each button.... line 62
# 3. here the interactions with the click of the mouse... done line 69

menu()
