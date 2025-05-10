from arbres import Tree
import unittest



class TestArbre(unittest.TestCase):

	def test_feuille(self):
		a = Tree('r')
		self.assertTrue(a.label()=='r')
		self.assertTrue(a.is_leaf())

	def test_children(self):
		a = Tree('e', Tree('e'), Tree('z', Tree('x'), Tree('w')))
		self.assertTrue(not a.is_leaf())

	def test_depth(self):
		a = Tree('e', Tree('e'), Tree('z', Tree('x'), Tree('w')))
		self.assertTrue(a.depth()==2)

	def test_str(self):
		a = Tree('f', Tree('a'), Tree('b'))
		self.assertTrue(str(a) == "f(a,b)")

	def test_eq(self):
		a = Tree('f', Tree('a'), Tree('b'))
		b = Tree('f', Tree('a'), Tree('b'))
		self.assertEqual(a, b)

		


if __name__ == '__main__':
	unittest.main()