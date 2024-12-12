import unittest
from orderedlinkedlist import *

class TestOrderlinkedlist(unittest.TestCase):
    def test_listevide(self):
        linked_list = OrderedLinkedList()
        self.assertEqual(linked_list.length(), 0)  

    def test_elementsimple(self):
        linked_list = OrderedLinkedList()
        linked_list.add(5)
        self.assertEqual(linked_list.length(), 1)  

    def test_elementsmultiples(self):
        linked_list = OrderedLinkedList()
        linked_list.add(10)
        linked_list.add(20)
        linked_list.add(30)
        self.assertEqual(linked_list.length(), 3)  

    def test_remove_debut(self):
        linked_list = OrderedLinkedList()
        linked_list.add(100)
        linked_list.add(200)
        linked_list.add(300)
        linked_list.remove(100)  # Suppression du premier élément (100)
        self.assertEqual(linked_list.length(), 2)  

    def test_remove_milieu(self):
        linked_list = OrderedLinkedList()
        linked_list.add(100)
        linked_list.add(200)
        linked_list.add(300)
        linked_list.remove(200)  # Suppression de l'élément du milieu (200)
        self.assertEqual(linked_list.length(), 2)  

    def test_remove_fin(self):
        linked_list = OrderedLinkedList()
        linked_list.add(100)
        linked_list.add(200)
        linked_list.add(300)
        linked_list.remove(300)  # Suppression du dernier élément (300)
        self.assertEqual(linked_list.length(), 2)  

    def test_remove_nonelement(self):
        linked_list = OrderedLinkedList()
        linked_list.add(100)
        linked_list.add(200)
        linked_list.add(300)
        linked_list.remove(400)  # Tentative de suppression d'un élément non présent
        self.assertEqual(linked_list.length(), 3)  

    def test_remove_listevide(self):
        linked_list = OrderedLinkedList()
        self.assertEqual(linked_list.length(), 0)

if __name__ == "__main__":
    unittest.main()
