import tkinter as tk 
import numpy as np 
import random as rd
import math as m
import time


graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]



class Window():

	def __init__(self, g):
		self.h = 600
		self.w = 600
		self.l0 = 30
		self.k = -1
		self.dt = 0.04

		self.running = False

		self.graph = g
		self.n = len(g)

		self.pos = np.array([[rd.randint(1,self.w), rd.randint(1,self.h)] for i in range(self.n)], dtype=float)
		self.vit = np.array([[(rd.random()-0.5)*10, (rd.random()-0.5)*10] for i in range(self.n)], dtype=float)
		self.acc = np.zeros((self.n, 2), dtype=float)



		self.root = tk.Tk()
		self.canva = tk.Canvas(self.root, width=self.w, height=self.h)

	def run(self):

		self.draw()

		self.root.bind("<Key>", self.keyPressed)

		self.canva.grid(column=0, row=0, padx=0, pady=0)
		self.root.mainloop()

	def keyPressed(self, event):
		if event.char.lower() == "f":
			self.running = True
			self.update_simulation()
		if event.char.lower() == "q":
			self.running = False



	def update_simulation(self):
		if not self.running:
			return
		self.calcul_pos()
		self.draw()
		self.root.after(int(self.dt * 1000), self.update_simulation)

	def dist(self, X, Y):
		return ((X[0]-Y[0])**2+(X[1]-Y[1])**2)**(1/2)

	def calcul_pos(self): # application de la loi de hook
		self.acc[:] = 0
		for i in range(self.n):
			for v in self.graph[i]:
				l = self.dist(self.pos[i], self.pos[v])
				if l == 0:
					continue  # avoid division by zero
				dx = self.pos[i][0] - self.pos[v][0]
				dy = self.pos[i][1] - self.pos[v][1]
				force_x = self.k * (l - self.l0) * dx/l
				force_y = self.k * (l - self.l0) * dy/l
				self.acc[i][0] += force_x
				self.acc[i][1] += force_y
			self.vit[i][0] += self.acc[i][0] * self.dt
			self.vit[i][1] += self.acc[i][1] * self.dt
			self.pos[i][0] += self.vit[i][0] * self.dt
			self.pos[i][1] += self.vit[i][1] * self.dt

			if self.pos[i][0] > 600 or self.pos[i][0] < 0:
				self.vit[i][0] = - self.vit[i][0]
			if self.pos[i][1] > 600 or self.pos[i][1] < 0:
				self.vit[i][1] = - self.vit[i][1]


	def draw(self):
		self.canva.delete("all")
		for i in range(self.n):
			for j in self.graph[i]:  # sucs de i a j
				self.canva.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
		for i in range(self.n):
			x, y = self.pos[i]
			self.canva.create_oval(x-8,y-8,x+8,y+8,fill="#f3e1d4")
			self.canva.create_text(x,y,text=str(i), fill="#000000")




if __name__ == '__main__':
	win = Window(graph)
	win.run()








