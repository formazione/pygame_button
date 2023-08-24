# the repository is here: https://github.com/formazione/tkinter_tutorial.git
# GiovanniPython on YT
# @pythonprogrammi on X


import tkinter as tk
from tkinter import messagebox
import pygame


class Window:
	def __init__(self):
		root = tk.Tk()
		root.title("MAIN WINDOW")

		hello = tk.Toplevel(root)
		hello.title("Hello")
		hello.but1 = tk.Button(hello,
			text="Hello Button",
			command= lambda : messagebox.showinfo("Hello and attention",
				"A button in a secundary window has been pressed abruptely!")
			)
		hello.but1.pack()

		root.mainloop()

pygame.init()


class Button:
	def __init__(self,text,pos,command):
		self.text = text
		self.command = command
		self.font = pygame.font.SysFont("Arial", 20)
		self.text = self.font.render(text, 1, (0,0,0))
		self.w, self.h = self.text.get_size()
		self.x, self.y = pos
		self.rect = pygame.Rect(self.x, self.x, self.w, self.h)

	def change_text(self, newtext):
		self.text = font.render(newtext, 1, (0,0,0))

	def mouse_collision(self):
		if button.rect.collidepoint(pygame.mouse.get_pos()):
				Window()

	def update(self):
		pygame.draw.rect(screen, (255, 255,255), self.rect)
		screen.blit(self.text, (self.x, self.y))


screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

button = Button("Click me", (100,100), None)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			button.mouse_collision()
	button.update()
	pygame.display.flip()
	clock.tick(60)

