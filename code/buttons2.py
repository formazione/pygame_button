import pygame
import pygame.gfxdraw
import sys
import os



pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()

class Button(pygame.sprite.Sprite):

    def __init__(self, position, text, size,
                colors="white on blue",
                hover_colors="red on green",
                style=1, borderc=(255,255,255),
                command=lambda: print("No command activated for this button")):
    
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
                print("Execunting code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1




# FUNCTIONS for the buttons on click
# I used this convention ... on_+text of the button


def b0_click():
    ''' prints something and start cmd '''
    print("Ciao bello")
    os.system("start")


def b1_click():
    print("Ciao bello questo è RUN")


def b2_click():
    print("This is Save")

def b3_click():
    os.system("py colorpycker.py")

def buttons_def():
    b0 = Button(
        (10, 10),
        "Click me now",
        24,
        "blue on white",
        command=b0_click)

    b1 = Button(
        (10, 100),
        "Run the program",
        40, "black on red",
        command=b1_click)

    b2 = Button(
        (10, 170),
        "Save this file",
        36,
        "#417130 on yellow",
        hover_colors="gray on darkgrey",
        style=2,
        borderc=(255,255,0),
        command=b2_click)

    b3 = Button(
        (10, 250),
        "Colorpycker",
        36,
        "#417130 on red",
        hover_colors="yellow on black",
        style=2,
        borderc=(255,255,0),
        command=b3_click)

# ======================= this code is just for example, start the program from the main file
# in the main folder, I mean, you can also use this file only, but I prefer from the main file
# 29.8.2021

if __name__ == '__main__':
    pygame.init()
    game_on = 0
    def loop():
        # BUTTONS ISTANCES
        game_on = 1
        buttons_def() # it creates the istances of the Button
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
