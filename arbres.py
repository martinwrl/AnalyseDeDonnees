


from __future__ import annotations


class Tree:

	def __init__(self, name : str ,*children : Tree):
		self.__label = name
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
		if arbre.is_leaf() and self.is_leaf() and self.label() == arbre.label():
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
			return []
		else:
			return tuple(self.__children)

	def nb_children(self):
		return len(self.__children)

	def child(self, i:int):
		assert(i<=(len(self.__children)))
		return self.__children[i]

	def is_leaf(self):
		if len(self.__children) == 0:
			return True
		else:
			return False

	def depth(self):
		if self.is_leaf():
			return 0
		else:
			return max(1+sousArbre.depth() for sousArbre in self.children())


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
					if self.child(i) == var:
						l.append('1')
					else:
						l.append('0')
					return Tree(self.label(), (Tree(el) for el in l))
			elif self.label() == '*':
				countVar = 0
				for el in self.children():
					if el == var:
						countVar += 1
				premsVar = True
				l = []
				for i in range(self.nb_children()):
					if premsVar and self.child(i).label() == var:
						l.append(countVar)
					else:
						l.append(self.child(i).label())
		else:
			assert(self.label() in ('-', '+', '*', '/'))
			if self.label() == '+' or self.label() == '-':
				return Tree(self.label(), (sousArbre.deriv(var) for sousArbre in self.children()))
			elif self.label() == '*' and self.nb_children()>=2:
				return Tree('+', Tree('*', (el for el in (self.child(0).deriv(var), self.children()[1:]))), Tree('*', self.child(0), Tree('*', (el for el in self.children()[1:])).deriv(var) )    )










			
if __name__ == '__main__':

	a = Tree('f', Tree('a'), Tree('b'))
	b = Tree('f', Tree('a'), Tree('b'))
	print(a.__eq__(b))
	print(a.__str__())
	c = Tree('e', Tree('a'), Tree('b'),Tree('c'))
	print(c.__str__())
































