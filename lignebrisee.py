import tkinter as tk
from tkinter import ttk 
import tkinter.font as tkfont
from numpy import random
import numpy as np 





root = tk.Tk()


def readWord(canva, word:str, h:int, w:int, color:str, ystart:int):
	y = ystart
	for l in word:
		if l not in 'udh':
			print('le mot n\'est pas correct')
			break
	for i in range(len(word)):
		if word[i] == 'u':
			canva.create_line(i*w, y, (i+1)*w, y-h, fill=color)
			y-=h
		elif word[i] == 'd':
			canva.create_line(i*w, y, (i+1)*w, h+y, fill=color)
			y+=h
		else:
			canva.create_line(i*w, y, (i+1)*w, y, fill=color)


def createWords(l:list, n:int):
	L = ['' for i in range(n)] 		# La liste des mots créés pour chaquue ligne
	order = [i for i in range(n)]
	for crois in l:
		for i in range(n):
			L[i] += 'hh'
		L[order[crois]] = L[order[crois]][:-1] + 'd'
		L[order[crois+1]] = L[order[crois+1]][:-1] + 'u'
		order[crois], order[crois + 1] = order[crois + 1], order[crois]
	for i in range(n):
			L[i] += 'h'
	return L, order

def changeColors(canva):
	canva.delete("all")
	global colorList
	global n
	global w 
	global croisements
	liste = np.array(colorList)
	random.shuffle(liste)
	colorList = list(liste)
	lignesBrisees(n, w, croisements)


def lignesBrisees(n, w, croisements:list): 
	global colorList
	Words, order = createWords(croisements, n)
	i = 1	
	for color in colorList[:n]:
		readWord(canva, Words[i-1], w, w, color, i*w)
		i+=1
	return order




if __name__ == '__main__':



	n = 6
	w = 70
	croisements = [3, 2, 1, 0, 4, 2, 3, 4, 2, 0, 1]
	colorList = ['green', 'red', 'blue', 'yellow', 'cyan', 'orange', 'black']



	canva = tk.Canvas(root, width=(len(croisements)*2+1)*w, height=(n+1)*w, bg='white', borderwidth=0, highlightthickness=0)
	quit = tk.Button(root, bg='black', text="Quit", command=root.destroy)
	colorButton = tk.Button(root, bg='black', text="Color", command=lambda : changeColors(canva))

	order = lignesBrisees(n, w, croisements)

	text1 = tk.Label(root, text="Croisements")
	text2 = tk.Label(root, text=f"{croisements}", borderwidth=2, relief='solid')
	text3 = tk.Label(root, text="Sortie")
	text4 = tk.Label(root, text=f"{order}", borderwidth=2, relief='solid')

	sideFrame = tk.Frame(root, height=(n+1)*w, width=30)
	# Labels inside side Frame

	for i in range(n):
		tk.Label(sideFrame, text=f"{i}").place(x=10, y=i*w+10+w/2)



	canva.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
	quit.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
	colorButton.grid(row=2, column=3, columnspan=2, padx=10, pady=10)
	text1.grid(row=1, column=1, padx=10, pady=10)
	text2.grid(row=1, column=2, padx=10, pady=10)
	text3.grid(row=1, column=3, padx=10, pady=10)
	text4.grid(row=1, column=4, padx=10, pady=10)
	sideFrame.grid(row=0, column=0)

	root.mainloop()


