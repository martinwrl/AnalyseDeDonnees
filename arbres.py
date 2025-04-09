


from __future__ import annotations


class Tree:

	def __init__(self, name : str ,*children : Tree):
		self.__label = name
		if len(children) == 1 and isinstance(children[0], (list, tuple)):
			self.__children = tuple(children[0])
		else:
			self.__children = tuple(children)

	def __str__(self):
		if self.is_leaf():
			return str(self.label())
		else:
			string=''
			for a in self.children():
				# A voir ci dessous, peut etre remplacer a.__str__() par juste a si ça ne marche pas
				string += ',' + a.__str__() 
			return f"{self.label()}({string[1:]})"

	def __eq__(self, arbre:Tree):
		if self.is_leaf() and arbre.is_leaf() and self.label() == arbre.label():
			return True
		else:
			if self.nb_children() != arbre.nb_children():
				return False
			else:
				res = True
				for i in range(self.nb_children()):
					res = res and self.children()[i].__eq__(arbre.children()[i])
				return self.label() == arbre.label() and res 


	def label(self):
		return self.__label

	def children(self):
		if self.is_leaf():
			return ()
		else:
			return self.__children

	def nb_children(self):
		return len(list(self.__children))


	def child(self, i:int):
		assert(i<=(len(self.__children)))
		return self.__children[i]

	def is_leaf(self):
		if self.nb_children() == 0:
			return True
		else:
			return False

	def depth(self):
		if self.is_leaf():
			return 0
		else:
			return max(1+ sousArbre.depth() for sousArbre in list(self.__children))

	def __repr__(self):
		return self.__str__()


	def deriv(self, var : str):
		if self.is_leaf():
			if self.label()==var:
				return Tree('1')
			else:
				return Tree('0')
		elif self.depth() == 1:
			if self.label() == '+' or self.label() == '-':
				l = []
				for i in range(self.nb_children()):
					if self.child(i).label() == var:
						l.append('1')
					else:
						l.append('0')
				return Tree(self.label(), tuple(Tree(el) for el in l))
			elif self.label() == '*':
				countVar = 0
				for el in self.children():
					if el.label() == var:
						countVar += 1
				premsVar = True
				l = []
				for i in range(self.nb_children()):
					if premsVar and self.child(i).label() == var:
						l.append(countVar)
					else:
						l.append(self.child(i).label())
				return Tree('*', tuple(Tree(el) for el in l))
		else:
			assert(self.label() in ('-', '+', '*', '/'))
			if self.label() == '+' or self.label() == '-':
				return Tree(self.label(), tuple(sousArbre.deriv(var) for sousArbre in self.children()))
			elif self.label() == '*' and self.nb_children()>=2:
				u = self.child(0)
				v = Tree('*', *self.children()[1:])
				up = u.deriv(var)
				vp = v.deriv(var)
				return Tree('+', Tree('*', up, v), Tree('*', u, vp))

	def simplify(self):

		if self.depth() == 2:
			if self.label() == '+' or self.label() == '-':
				l = []
				for i in range(self.nb_children()):
					if self.child(i).label() != 0:
						l.append(self.child(i))
				if len(l) >= 2:
					return Tree('+', *l)
				elif len(l) == 1:
					return l[0]
				else:
					return Tree('0')
			# il manque encore l'addition et la multiplication de deux entiers
			elif self.label() == '*':
				if Tree('0') in self.__children:
					return Tree('0')
				#### Il y a une erreur dans cette méthode : il y a un probleme lors de comparaison ci dessus. 
				#### Erreur : NoneType object has no attribute is_leaf
				else:
					l = []
					for i in range(self.nb_children()):
						if self.child(i).label() != 1:
							l.append(self.child(i))
					if len(l) >= 2:
						return Tree('*', *l)
					elif len(l)==1:
						return l[0]
					else:
						return Tree('1')














			
if __name__ == '__main__':

	a = Tree('f', Tree('a'), Tree('b'))
	b = Tree('f', Tree('a'), Tree('b'))
	print(a.__eq__(b))
	print(a.__str__())
	c = Tree('e', (Tree('a'), Tree('b'),Tree('c')))
	print(c.__str__())

	print(type(a) == Tree)































