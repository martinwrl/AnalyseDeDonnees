import tkinter as tk 
import numpy as np
from numpy import random
import random




class App():

	def __init__(self, data, w):

		self.w = w
		self.lines = []
		self.data = data

		self.data.createLines()
		l = self.data.listLines
		self.lines = []
		for el in l:
			lt = []
			for t in el:
				lt.append((t[0]*self.w, t[1]*self.w))
			self.lines.append(lt)


		self.root = tk.Tk()

		self.canva = tk.Canvas(self.root, width=(len(self.data.croisements)*2+1)*self.w, height=(self.data.n+1)*self.w, bg='white', borderwidth=0, highlightthickness=0)
		self.quit = tk.Button(self.root, text="Quit", command=self.root.destroy)
		self.colorButton = tk.Button(self.root, text="Color", command=self.colorChange)

		self.randomEntrelacs = tk.Button(self.root, text="Entrelacs Random", command=self.entrelacsRandom)

		self.text1 = tk.Label(self.root, text="Croisements")
		self.text2 = tk.Label(self.root, text=f"{self.data.croisements}", borderwidth=2, relief='solid')
		self.text3 = tk.Label(self.root, text="Sortie")
		self.text4 = tk.Label(self.root, text=f"{self.data.order}", borderwidth=2, relief='solid')

		self.sideFrame = tk.Frame(self.root, height=(self.data.n+1)*self.w, width=30)
		# Labels inside side Frame

		for i in range(self.data.n):
			tk.Label(self.sideFrame, text=f"{i}").place(x=10, y=i*self.w+10+self.w/2)

		self.colorList = ['green', 'red', 'blue', 'yellow', 'cyan', 'orange', 'black']

	def colorChange(self):
		self.shuffleColors()
		self.redraw()

	def entrelacsRandom(self):
		n = self.data.len
		l = []
		for i in range(n):
			l.append(random.randint(0, self.data.n-2))
		self.data.croisements = l 
		self.data.createLines()
		l = self.data.listLines
		self.lines = []
		for el in l:
			lt = []
			for t in el:
				lt.append((t[0]*self.w, t[1]*self.w))
			self.lines.append(lt)
		self.redraw()

	def runForever(self):

		self.lignesBrisees()


		self.text1 = tk.Label(self.root, text="Croisements")
		self.text2 = tk.Label(self.root, text=f"{self.data.croisements}", borderwidth=2, relief='solid')
		self.text3 = tk.Label(self.root, text="Sortie")
		self.text4 = tk.Label(self.root, text=f"{self.data.order}", borderwidth=2, relief='solid')

		self.canva.bind("<Button-1>", self.click)

		self.canva.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
		self.quit.grid(row=2, column=1, padx=10, pady=10)
		self.colorButton.grid(row=2, column=3, padx=10, pady=10)
		self.randomEntrelacs.grid(row=2, column=2, padx=10, pady=10)
		self.text1.grid(row=1, column=1, padx=10, pady=10)
		self.text2.grid(row=1, column=2, padx=10, pady=10)
		self.text3.grid(row=1, column=3, padx=10, pady=10)
		self.text4.grid(row=1, column=4, padx=10, pady=10)
		self.sideFrame.grid(row=0, column=0)
		self.root.mainloop()

	def click(self, event):
		x = event.x
		y = event.y 
		listRem = [] 
		

		for i in range(len(self.data.croisements)-1):
			if self.data.croisements[i] == self.data.croisements[i+1]:
				listRem.append((self.data.croisements[i], i))
		for i in range(len(listRem)):
			d = self.dist((x, y), (listRem[i][1]*self.w*2+self.w*1.5, (listRem[i][0]+1.5)*self.w))
			if d <= self.w/2:
				L=[]
				for j in range(len(self.data.croisements)):
					if j != listRem[i][1] and j != listRem[i][1] + 1:
						L.append(self.data.croisements[j])
				self.data.croisements = L
				self.data.createLines()
				l = self.data.listLines
				self.lines = []
				for el in l:
					lt = []
					for t in el:
						lt.append((t[0]*self.w, t[1]*self.w))
					self.lines.append(lt)
				self.redraw()
				self.redraw()
		

	def dist(self, X, Y):
		(x1, y1) = X
		(x2, y2) = Y
		return ((x2-x1)**2+(y2-y1)**2)**(1/2)


	def redraw(self):
		self.canva.delete("all")
		self.lignesBrisees()

	
	def shuffleColors(self):
		liste = np.array(self.colorList)
		random.shuffle(liste)
		self.colorList = list(liste)


	def lignesBrisees(self): 
		j = 0
		for line in self.lines:
			for i in range(len(line)-1):
				self.canva.create_line(line[i][0], line[i][1], line[i+1][0], line[i+1][1], fill=self.colorList[j])
			j+=1




class Data():

	def __init__(self, croisements, n):

		self.croisements = croisements
		self.n = n
		self.order = []
		self.wordList = []
		self.listLines = []
		self.len = len(croisements)

		'''
			def readWord(self, word:str, color:str, ystart):
				y = ystart
				listL = [(0, y)]
				for l in word:
					if l not in 'udh':
						print('le mot n\'est pas correct')
						break
				for i in range(len(word)):
					if word[i] == 'u':
						listL.append(((i+1)*self.w, y-self.w))
						y-=self.w
					elif word[i] == 'd':
						listL.append(((i+1)*self.w, self.w+y))
						y+=self.w
					else:
						listL.append(((i+1)*self.w, y))
		'''


	def createLines(self):
		L = ['' for i in range(self.n)] 		# La liste des mots créés pour chaquue ligne
		order = [i for i in range(self.n)]
		for crois in self.croisements:
			for i in range(self.n):
				L[i] += 'hh'
			L[order[crois]] = L[order[crois]][:-1] + 'd'
			L[order[crois+1]] = L[order[crois+1]][:-1] + 'u'
			order[crois], order[crois + 1] = order[crois + 1], order[crois]
		for i in range(self.n):
				L[i] += 'h'
		self.order = order
		self.wordList = L
		self.listLines = []
		for j in range(1, self.n+1):
			y = j
			listL = [(0, y)]
			for l in self.wordList[j-1]:
				if l not in 'udh':
					print('le mot n\'est pas correct')
					break
			for i in range(len(self.wordList[j-1])):
				if self.wordList[j-1][i] == 'u':
					listL.append((i+1, y-1))
					y-=1
				elif self.wordList[j-1][i] == 'd':
					listL.append((i+1, 1+y))
					y+=1
				else:
					listL.append((i+1, y))

			self.listLines.append(listL)

if __name__ == '__main__':

	data = Data([3, 2, 0, 1, 2, 3, 2, 3, 0, 3], 6)
	app = App(data, 70)
	app.runForever()







