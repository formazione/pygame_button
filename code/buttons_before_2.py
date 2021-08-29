import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style=1, borderc=(255,255,255),
        command=lambda: print('''Add the param 'command' 
to this button istance binding it to the name of a fuction,
i.e. command=show_image where show image is a normal function.
You can use lambda too.''')):
        # the hover_colors attribute needs to be fixed
        super().__init__()
        self.text = text
        self.command = command
        # --- colors ---
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors
        self.style = style
        self.borderc = borderc # for the style2
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        buttons.add(self)

    def render(self):
        self.text_render = self.font.render(self.text, 1, self.fg)
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        self.hover()
        self.click()

    def draw_button1(self):
        ''' draws 4 lines around the button and the background '''
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background of the button
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))  

    def draw_button2(self):
        ''' a linear border '''
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x, self.y, self.w , self.h), self.borderc)

    def hover(self):
        ''' checks if the mouse is over the button and changes the color if it is true '''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # you can change the colors when the pointer is on the button if you want
            self.colors = self.hover_colors
            # pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            self.colors = self.original_colors
            
        self.render()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("Execunting code for " + self.text)
                # self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1




# FUNCTIONS

def print_hello():
    print("Ciao")


if __name__ == '__main__':
    pygame.init()
    print("\nHey you run this but...\n...it is not the main file.")
    print("\nPlease, stop looking at an empty window\nClose it and Run main3f.py")

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
    loop()
