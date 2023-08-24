import tkinter as tk
from random import randint



# ====== TKINTER GUI ===========
class Window:

	def __init__(self):
		self.root = tk.Tk()
		self.root.geometry("800x600")
		self.root.config(background="black")
		self.widgets()
		self.root.mainloop()

	def widgets(self):
		self.label_widget()
		self.color1 = 0
		self.color2 = 0
		self.color3 = 0
		self.scale_widget1()
		self.scale_widget2()
		self.scale_widget3()


	def label_widget(self):
		self.label = tk.Label(self.root,
			text="...",
			font="Arial 20",
			)
		self.label.pack(pady=80)

	def scale_widget1(self):
		self.var1 = tk.IntVar()
		self.scale1 = tk.Scale(self.root,
			variable=self.var1,
			from_=0, to=255, length=255,
			orient=tk.HORIZONTAL,
			command=self.scalecommand1)
		self.scale1.pack()


	def scale_widget2(self):
		self.var2 = tk.IntVar()
		self.scale2 = tk.Scale(self.root,
			variable=self.var2,
			from_=0, to=255, length=255,
			orient=tk.HORIZONTAL,
			command=self.scalecommand2)
		self.scale2.pack()

	def scale_widget3(self):
		self.var3 = tk.IntVar()
		self.scale3 = tk.Scale(self.root,
			variable=self.var3,
			from_=0, to=255, length=255,
			orient=tk.HORIZONTAL,
			command=self.scalecommand3)
		self.scale3.pack()




	def rgb_to_hex(self, r, g, b):
		self.hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)


	def refresh_color(self):
		self.rgb_to_hex(self.color1,self.color2,self.color3)
		self.root.title(f"{self.color1},{self.color2},{self.color3}")
		self.label.config(text=(self.hex))
		self.root.config(background=self.hex)


	def scalecommand1(self, scale_size):
		''' modify text in label = scale size '''
		self.color1 = int(scale_size)
		self.refresh_color()


	def scalecommand2(self, scale_size):
		''' modify text in label = scale size '''
		self.color2 = int(scale_size)
		self.refresh_color()


	def scalecommand3(self, scale_size):
		''' modify text in label = scale size '''
		self.color3 = int(scale_size)
		self.refresh_color()


app = Window()