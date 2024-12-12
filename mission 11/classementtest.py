import unittest
from classement import Classement
from resultat import Resultat
from coureur import Coureur

class TestClassement(unittest.TestCase):

    def setUp(self):
        self.classement = Classement()
        self.coureur1 = Coureur("Alfred", 24)
        self.coureur2 = Coureur("Bernard", 27)
        self.resultat1 = Resultat(self.coureur1, 100)
        self.resultat2 = Resultat(self.coureur2, 90)

    def test_initial_size(self):
        self.assertEqual(self.classement.size(), 0)

    def test_add_resultat(self):
        self.classement.add(self.resultat1)
        self.assertEqual(self.classement.size(), 1)

    def test_get_resultat(self):
        self.classement.add(self.resultat1)
        self.assertEqual(self.classement.get(self.coureur1), self.resultat1)

    def test_get_position(self):
        self.classement.add(self.resultat1)
        self.classement.add(self.resultat2)
        self.assertEqual(self.classement.get_position(self.coureur2), 1)
        self.assertEqual(self.classement.get_position(self.coureur1), 2)

    def test_remove_resultat(self):
        self.classement.add(self.resultat1)
        self.classement.add(self.resultat2)
        self.assertEqual(self.classement.remove(self.coureur1), self.coureur1)
        self.assertEqual(self.classement.size(), 1)
        self.assertFalse(self.classement.remove(self.coureur1))

    def test_str(self):
        self.classement.add(self.resultat1)
        self.classement.add(self.resultat2)
        expected_str = ["1- Bernard    : 90", "2- Alfred     : 100\n"]
        self.assertEqual(str(self.classement), "\n".join(expected_str))

if __name__ == '__main__':
    unittest.main()
