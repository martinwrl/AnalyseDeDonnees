
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

	def up(self, n):
		return PolynomialZq(self.poly, self.q, n)

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

	def opp(self):
		NP = [0 for i in range(self.n)]
		for i in range(len(self.poly)):
			NP[i] -= self.poly[i]
		return PolynomialZq([coeff % self.q for coeff in NP], self.q, self.n)

	def mulKaratsuba(self, Q):

		assert(self.getInfos() == Q.getInfos())
		
		if len(self.poly) == 1:
			return PolynomialZq([self.poly[0]*Q.poly[0]], self.q , 1)
		else:
			p = self.poly
			q = Q.getPoly()
			d = len(p)
			
			i,n = self.getInfos()
			if d%2!=0:
				p,q = p+[0],q+[0]
				d+=1
			l = int(d/2)
			p0 = PolynomialZq(self.poly[:l], i,l)
			p1 = PolynomialZq(self.poly[l:], i,l)
			q0 = PolynomialZq(Q.poly[:l], i,l)
			q1 = PolynomialZq(Q.poly[l:], i,l)
			p0q0 = p0.mulKaratsuba(q0)
			p1q1 = p1.mulKaratsuba(q1)
			prod = p0.add(q1)
			prod = prod.mulKaratsuba(q0.add(q1))
			prod = prod.add(p0q0.add(p1q1))
			prod = prod.opp()


			p1q1 = PolynomialZq([0 for i in range(2*l)]+p1q1.getPoly(), i, 4*l)
			prod = PolynomialZq([0 for i in range(l)]+prod.getPoly(), i, 4*l)
			p0q0 = p0q0.up(4*l)
			return PolynomialZq([coeff%i for coeff in p0q0.add(prod).add(p1q1).getPoly()] ,i, 4*l)








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

	assert(PolynomialZq([0,0,2],4,4).mul(PolynomialZq([0,0,5,3],4,4)).__str__() == "0*X^3 + 0*X^2 + 2*X^1 + 2")

	### EXERCICE 6
	# L'exercice 6 n'est pas fini, la methode mulKaratsuba ne fonctionne pas. 

	P = PolynomialZq([1,0,0,0,2], 4, 5)
	Q = PolynomialZq([3, 0, 4, 4, 0], 4, 5)
	
	P = PolynomialZq([2,6], 4, 2)
	Q = PolynomialZq([2,3], 4, 2)	
	print(P.mulKaratsuba(Q))
	print(P.mul(Q))











