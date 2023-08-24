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
		self.dynamic_elevation = elevation
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
		self.top_rect.y = self.original_y_pos - self.dynamic_elevation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elevation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elevation = self.elevation
				if self.pressed == True:
					self.command()

					self.pressed = False
					self.change_text(self.text)
		else:
			self.dynamic_elevation = self.elevation
			self.top_color = '#475F77'





pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()
gui_font = pygame.font.Font(None,30)


class Window():
	''' put here all the button istances
	    put in this class the command methods for the buttons '''

	def __init__(self):
		self.buttons_istances()

	def button1_command(self):
		''' code executed on click of button1 '''
		print("Let the game begin")
		self.button1.text = "Loading assets..."


	def button_help_command(self):
		''' code executed on click of button1 '''
		print("Opening help file")
		self.button1.text = "X"
		os.system("help.txt")


	def buttons_istances(self):
		''' code executed when you click "?" button on top left corner'''
		self.button1 = Button('Start the Game',200,40,(100,200),5, self.button1_command)
		self.button2 = Button('Options',200,40,(100,250),5)
		self.button2.command = (lambda: print("What difficulty you want to choose?"))
		self.button3 = Button('Quit the game',200,40,(100,300),5)
		self.button3.bind(lambda: print("Ok, bye"))
		self.button_help = Button('?',40,40,(0,0),5, command=self.button_help_command)

try:
	Window()
except NameError:
	print("Must have a wrong function name or not existing function for a button command.")
	os.system("help.txt")


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