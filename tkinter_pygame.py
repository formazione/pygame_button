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

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
rect = pygame.Rect(100,100,100,50)
font = pygame.font.SysFont("Arial", 20)
click = font.render("Click me", 1, (0,0,0))
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			if rect.collidepoint(pygame.mouse.get_pos()):
				Window()
	pygame.draw.rect(screen, (255, 255,255), rect)
	screen.blit(click, rect)
	pygame.display.flip()
	clock.tick(60)

