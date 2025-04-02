
# Les indices e la liste prise en entrée correspondent aux degrés des polynomes unitaires associés. 
# L'indice 0 est ainsi le terme constant, et le dernier de la liste celui de plus haut degré.

class Polynomial:

	def __init__(self, l):
		self.poly = l


	def __str__(self):
		chaine = ""
		for i in range(len(self.poly)-1, 0, -1):
			chaine += f"{self.poly[i]}*X^{i} + "
		chaine += f"{self.poly[0]}"
		return chaine[:len(chaine)]

	def getPoly(self):
		return self.poly

	# On additionne le polynome au polynome Q et on en créé un nouveau

	def add(self, Q):
		NP = [0 for i in range(max(len(self.poly), len(Q.getPoly())))]
		for i in range(len(self.poly)):
			NP[i] += self.poly[i]
		for i in range(len(Q.getPoly())):
			NP[i] += Q.getPoly()[i]
		return Polynomial(NP)

	def scalar(self, c):
		Q = []
		for coeff in self.poly:
			Q.append(coeff*c)
		return Polynomial(Q)

############################################################################################

class PolynomialZq:

	def __init__(self, l, q, n):
		self.n = n 
		self.q = q

		if len(l)>self.n:
			p = [coeff for coeff in l][:self.n]
			for i in range(self.n,len(l)):
				if l[i]!=0:
					p[i%self.n] = -l[i]
		else:
			p = l + [0 for i in range(n-len(l))]
		
		self.poly = [coeff % self.q for coeff in p]
	
	def __str__(self):
		chaine = ""
		for i in range(len(self.poly)-1, 0, -1):
			chaine += f"{self.poly[i]}*X^{i} + "
		chaine += f"{self.poly[0]}"
		return chaine[:len(chaine)]

	def getPoly(self):
		return self.poly

	def getInfos(self):
		return self.n, self.q

	def rescale(self, r):
		Q = []
		for coeff in self.poly:
			Q.append(coeff % r)
		return PolynomialZq(Q)

	def add(self, Q):
		assert(self.getInfos() == Q.getInfos())
		NP = [0 for i in range(self.n)]
		for i in range(len(self.poly)):
			NP[i] += self.poly[i]
		for i in range(len(Q.getPoly())):
			NP[i] += Q.getPoly()[i]
		return PolynomialZq([coeff % self.q for coeff in NP], self.q, self.n)

	def mul(self, Q):
		assert(self.getInfos() == Q.getInfos())

		p = self.poly
		q = Q.getPoly()
		d = len(p)
		NP = [0 for i in range(2*d-1)]
		for i in range(d):
			for j in range(d):
				NP[i+j]+=p[i]*q[j]
		return PolynomialZq(NP, self.getInfos()[0], self.getInfos()[1])


if __name__ == '__main__':

	### EXERCICE 1

	P = Polynomial([3,5,0,2])
	assert(P.__str__() == "2*X^3 + 0*X^2 + 5*X^1 + 3")
	Q = Polynomial([4,0,8,5,6])
	assert(P.add(Q).__str__() == "6*X^4 + 7*X^3 + 8*X^2 + 5*X^1 + 7")

	### EXERCICE 3

	assert(PolynomialZq([5,0,2], 4, 3).add(PolynomialZq([3, 2, 1], 4, 3)).__str__()=="3*X^2 + 2*X^1 + 0")

	# test pour saboir si le modulo des polynomes fonctionne bien
	assert(PolynomialZq([2,5,7,3,5], 3, 3).__str__() == "1*X^2 + 1*X^1 + 0")
	### EXECICE 5
	assert(PolynomialZq([0,0,2],4,4).mul(PolynomialZq([0,0,5,3],4,4)).__str__() == 0*X^3 + 0*X^2 + 2*X^1 + 2)
	











