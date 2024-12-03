import unittest
from math import pi
from graphics import GraphWin
from XYRobot import XYRobot

class TestXYRobot(unittest.TestCase):

    def setUp(self):
        self.robot = XYRobot("Hagrid", 100, 100)
    
    def testinit(self):
        self.assertEqual(self.robot.position(), (100,100), "Erreur dans la position initiale")
        self.assertEqual(self.robot.angle(), 0., "Erreur dans l'angle initial")
    
    def test_turn_right(self):
        self.robot.turn_right()
        self.assertEqual(self.robot.angle(), 90, "Erreur dans la rotation à droite")
        self.robot.turn_right()
        self.assertEqual(self.robot.angle(), 180, "Erreur dans la deuxième rotation à droite")

    def test_turn_left(self):
        self.robot.turn_left() #self.instant.methode obligatoire vu que c'est un autre fichier
        self.assertEqual(self.robot.angle(), 270, "Erreur dans la rotation à droite")
        self.robot.turn_left()
        self.assertEqual(self.robot.angle(), 180, "Erreur dans la deuxième rotation à droite")

    def test_turn(self):
        self.robot.turn_left()
        self.robot.turn_right()
        self.assertEqual(self.robot.angle(), 0, "Erreur dans la combinaison de rotation")

    def test_forward(self):
        self.robot.move_forward(100)
        self.assertEqual(self.robot.position(), (200,100), "Erreur dans translation vers l'avant")

    def test_backward(self):
        self.robot.move_backward(100)
        self.assertEqual(self.robot.position(), (0,100), "Erreur dans translation vers l'arrière")

    def test_moves(self):
        self.robot.move_forward(100)
        self.robot.move_backward(100)
        self.assertEqual(self.robot.position(), (100,100), "Erreur dans la combinaison de mouvement")

    def test_history(self):
        self.robot.move_forward(100)
        self.robot.move_backward(100)
        self.robot.turn_right()
        self.robot.turn_left()
        self.assertEqual(self.robot.history(), [('forward', 100), ('backward', 100), ('right', 90), ('left', 90)], "Erreur dans l'historique")

    def test_unplay(self):
        self.robot.move_forward(100)
        self.robot.move_backward(100)
        self.robot.turn_right()
        self.robot.turn_left()
        self.robot.unplay()
        self.assertEqual(self.robot.position(), (100,100), "Erreur dans l'inverse des mouvements")
        self.assertEqual(self.robot.history(), [], 'Historique non supprimé')



if __name__ == '__main__':
    unittest.main(verbosity=2)