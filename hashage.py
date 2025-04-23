import matplotlib.pyplot as plt 
import time


####### Fonstions de Hashage : 

def hashNaive(key : str): # Uniquement sur les chaines de characteres !
	return sum([ord(i) for i in key])

def hashJenkins(key : str):
	l = len(key)
	i = 0
	h = 0
	while i != l:
		h += ord(key[i])
		h += h << 3
		h += h >> 5
		h *= 47
		i+=1
		
		h %= 67117
	h += h << 3
	h += h >> 11
	h += h << 5
	return h





####### Table de Hashage

class Hashable():

	def __init__(self, hs, N):
		self.__h = hs 
		self.__N = N
		self.__tab = [None for i in range(N)]
		self.__rempl = 0

	def put(self, key, value):
		t1 = time.perf_counter()
		h = self.__h(key) % self.__N
		self.__rempl += 1
		if self.__tab[h] == None: 
			self.__tab[h] = [(key, value)]
		else:
			self.__tab[h].append((key, value))
		t2 = time.perf_counter()
		print(t2-t1)
		if self.__rempl >= 1.2*self.__N:
			self.resize()

	def get(self, key):
		h = self.__h(key) % self.__N
		if self.__tab[h] == None:
			return None
		else:
			for (k, v) in self.__tab[h]:
				if key == k:
					return v
		return None

	def repartition(self):
		X = range(self.__N)
		Y = []
		for l in self.__tab:
			if l != None:
				Y.append(len(l)-1)
			else:
				Y.append(0)
		width = 1/1.5
		plt.bar(X, Y, width, color='red')
		plt.show()
		print(sum(Y))

	def resize(self):
		self.__tab += [None for i in range(self.__N)]
		self.__N *=2
		self.__rempl //= 2
			
			
if __name__ == '__main__':

	h = Hashable(hashJenkins, 16)
	h.put('abc', 4)
	h.put('acb', 5)
	#h.repartition()
	
	with open('frenchssaccent.dic') as dico:
		D = Hashable(hashJenkins, 12345)
		listeMots = dico.read().split("\n")
		for el in listeMots:
			D.put(el, len(el))
		D.repartition()
	

	










