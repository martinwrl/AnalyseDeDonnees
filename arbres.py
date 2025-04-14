


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
		if self.nb_children() == 1:
			return self.child(0).deriv(var)
		elif self.is_leaf():
			if self.label()==var:
				return Tree('1')
			else:
				return Tree('0')
		elif self.depth() == 1:
			if self.label() == '+' or self.label() == '-':
				l = []
				for child in self.children():
					if child.label() == var:
						l.append(Tree('1'))
					else:
						l.append(Tree('0'))
				return Tree(self.label(), tuple(el for el in l))
			elif self.label() == '*':
				countVar = 0
				for child in self.children():
					if child.label() == var:
						countVar += 1
				premsVar = True
				l = []
				for child in self.children():
					if premsVar and child.label() == var:
						l.append(countVar)
						premsVar = False
					else:
						l.append(child.label())
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
		if self.nb_children() == 1:
			return self.child(0).simplify()
		if self.depth() == 0:
			return self

		simplChildren = tuple(child.simplify() for child in self.children())
		simpl = Tree(self.label(), simplChildren)

		if self.label() in ('*', '+', '-'):
			flattened = []
			for child in simplChildren:
				if self.label() == child.label():
					flattened.extend(child.children())
				else:
					flattened.append(child)
			simplChildren = tuple(flattened)

		if self.label() == '+' or self.label() == '-':
			constant = 0
			other = []
			for child in simplChildren:
				try:
					constant += int(child.label())
				except:
					other.append(child)
			if constant != 0:
				other.append(Tree(str(constant)))
			if not other:
				return Tree('0')
			elif len(other) == 1:
				return other[0]
			else:
				return Tree(self.label(), *other)

		if self.label() == '*':
			if any(child.label() == '0' for child in simplChildren):
				return Tree('0')
			constant = 1
			other = []
			for child in simplChildren:
				try:
					constant *= int(child.label())
				except:
					other.append(child)
			if constant == 0:
				return Tree('0')
			if constant != 1:
				other = [Tree(str(constant))] + other
			if not other:
				return Tree('1')
			elif len(other) == 1:
				return other[0]
			else:
				return Tree(self.label(), *other)

		return simpl
		
	def substitute(self, t1:Tree, t2:Tree):
		if self == t1:
			return t2
		elif self.is_leaf():
			return self
		else:
			return Tree(self.label(), tuple(child.substitute(t1, t2) for child in self.children()))

	def infixe(self):
		if self.is_leaf():
			return self.label()
		else:
			return "".join([f"{self.label()}{child.infixe()}" for child in self.children()])[1:]

	def evaluate(self, var:str, x:int):
		return int(self.substitute(Tree(var), Tree(str(x))).simplify().__str__())


			
if __name__ == '__main__':
	b = Tree('+',
		Tree('+',
			Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X'))),
			Tree('*', Tree('5'), Tree('X'))),
	 	Tree('7'))
	a = Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X')))
	print(b.simplify().infixe())































