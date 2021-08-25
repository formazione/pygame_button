import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

buttons = pygame.sprite.Group()

class Button(pygame.sprite.Sprite):
    def __init__(self, screen, position, text, size,
        colors="white on blue",
        hover_colors="red on green"):
        super().__init__()
        self.text = text
        self.colors = colors
        self.original_colors = colors
        self.hover_colors = hover_colors
        self.fg, self.bg = self.colors.split(" on ")
        self.font = pygame.font.SysFont("Arial", size)
        self.text_render = self.font.render(self.text, 1, self.fg)
        self.image = self.text_render
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        buttons.add(self)

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))

        if self.rect.collidepoint(pygame.mouse.get_pos()):

            self.colors = self.hover_colors
        else:
            self.colors = self.original_colors
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print(self.position)
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1


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
b0 = Button(screen, (10, 10), "1st button", 55, "black on white")
b1 = Button(screen, (10, 100), "2nd button", 40, "black on red")
b2 = Button(screen, (10, 200), "3rd button", 36, "red on yellow")
print(b0.x)

loop()
