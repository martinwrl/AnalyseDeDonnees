import unittest
from arbres import Tree  # à adapter selon le nom réel de ton fichier

class TestTree(unittest.TestCase):

    def setUp(self):
        self.leaf = Tree('a')
        self.tree1 = Tree('f', Tree('a'), Tree('b'))
        self.tree2 = Tree('g', Tree('a'))
        self.tree3 = Tree('+', Tree('a'), Tree('X'))
        self.tree4 = Tree('+', Tree('0'), Tree('1'))
        self.tree5 = Tree('+', Tree('X'), Tree('5'))
        self.poly = Tree('+',
                         Tree('+',
                              Tree('*', Tree('3'), Tree('*', Tree('X'), Tree('X'))),
                              Tree('*', Tree('5'), Tree('X'))),
                         Tree('7'))

    def test_label(self):
        self.assertEqual(self.leaf.label(), 'a')

    def test_children(self):
        self.assertEqual(self.tree1.nb_children(), 2)
        self.assertEqual(self.tree2.nb_children(), 1)
        self.assertEqual(self.leaf.nb_children(), 0)

    def test_child(self):
        self.assertEqual(self.tree1.child(0).label(), 'a')
        self.assertEqual(self.tree1.child(1).label(), 'b')

    def test_is_leaf(self):
        self.assertTrue(self.leaf.is_leaf())
        self.assertFalse(self.tree1.is_leaf())

    def test_depth(self):
        self.assertEqual(self.leaf.depth(), 0)
        self.assertEqual(self.tree1.depth(), 1)
        self.assertEqual(self.poly.depth(), 4)

    def test_str(self):
        self.assertEqual(str(self.leaf), 'a')
        self.assertEqual(str(self.tree1), 'f(a,b)')
        self.assertEqual(str(self.tree2), 'g(a)')

    def test_eq(self):
        t1 = Tree('f', Tree('a'), Tree('b'))
        t2 = Tree('f', Tree('a'), Tree('b'))
        self.assertEqual(t1, t2)
        self.assertIsNot(t1, t2)  # Vérifie qu'ils ne pointent pas sur le même objet

    def test_deriv_addition(self):
        deriv = self.tree3.deriv('X')
        self.assertEqual(str(deriv), '+(0,1)')

    def test_deriv_polynome(self):
        d = self.poly.deriv('X').simplify()
        self.assertEqual(str(d), '+(*(6,X),5)')  # brut

    def test_substitute(self):
        result = self.tree3.substitute(Tree('X'), Tree('b'))
        self.assertEqual(str(result), '+(a,b)')

    def test_simplify(self):
        simplified = self.tree4.simplify()
        self.assertEqual(str(simplified), '1')

    def test_eval_poly(self):
        result = self.poly.substitute(Tree('X'), Tree('2')).simplify()
        self.assertEqual(str(result), '29')

    def test_evaluate(self):
        result = self.tree5.evaluate('X', 3)
        result2 = self.poly.evaluate('X', 1)
        self.assertEqual(result, 8)
        self.assertEqual(result2, 15)

if __name__ == '__main__':
    unittest.main()