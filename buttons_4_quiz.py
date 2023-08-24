import pygame, sys
from tkinter import messagebox
import os

def help_empty_command():
	''' function for buttons without command argument '''
	messagebox.showinfo("Attenzione", f"""
		[WARNING]:
			You have not assigned a function to
	 		your button. Create a function called command2, for
	  		example and add command2 as last parameter of the istance
	   		of this buttonex:
	   		button1 = Button('Rome',200,40,(100,200),5, command1))""")

buttons = []
class Button:
	def __init__(self,text,width,height,pos,elevation, command=help_empty_command):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
		self.command = command

		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text = text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		buttons.append(self)

	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def bind(self, command):
		self.command = command

	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.command()
					self.pressed = False
					self.change_text(self.text)
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'



def button1_command():
	print("The first button has some code")
	button1.text = "Pressed"

# def button_help_command():
# 	os.system("button_help.txt")

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)

button1 = Button('Rome',200,40,(100,200),5, button1_command)
button2 = Button('Milan',200,40,(100,250),5, lambda: print("This was done with istance"))
button2.command = (lambda: print("I am Milan button"))
button3 = Button('Neaples',200,40,(100,300),5)
button3.bind(lambda: print("Hello"))
button4 = Button('Genoa',200,40,(100,350),5, command=lambda: print("Genoa (command in istance)"))


button_help = Button('?',40,40,(0,0),5, command=button_help_command)

def buttons_draw():
	for b in buttons:
		b.draw()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill('#DCDDD8')
	buttons_draw()

	pygame.display.update()
	clock.tick(60)