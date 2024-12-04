class ListeVide(Exception):
    """Exception levée si l'historique est vide lors d'une tentative d'annulation."""
    pass

class Robot:
    """Classe de base représentant un robot générique."""
    
    def __init__(self, name):
        self.__name = name
        self.__history = []  # Liste pour enregistrer les actions du robot

    def name(self):
        """Retourne le nom du robot."""
        return self.__name

    def history(self):
        """Retourne l'historique des actions du robot."""
        return self.__history

    def move_forward(self, distance):
        """Avance d'une certaine distance (méthode à implémenter dans les sous-classes)."""
        self.history().append(('forward', distance))

    def move_backward(self, distance):
        """Recule d'une certaine distance (méthode à implémenter dans les sous-classes)."""
        self.history().append(('backward', distance))

    def turn_left(self):
        """Tourne à gauche (méthode à implémenter dans les sous-classes)."""
        self.history().append(('left', 90))

    def turn_right(self):
        """Tourne à droite (méthode à implémenter dans les sous-classes)."""
        self.history().append(('right', 90))

    def position(self):
        """Retourne la position du robot (méthode à implémenter dans les sous-classes)."""
        pass

    def angle(self):
        """Retourne l'angle actuel du robot (méthode à implémenter dans les sous-classes)."""
        pass

    def __str__(self):
        """Retourne une représentation textuelle du robot."""
        return f"{self.name()}@{self.position()} angle: {self.angle()}"

    def unplay(self):
        if not self.history():
            raise ListeVide("Historique vide")  # Exception si l'historique est vide
        for action, value in reversed(self.history()): #Commande géniale qui inverse les listes (évite de la réécrire)
            if action == 'forward':
                self.move_backward(value) #Comme ça les actions sont bien rejouées à l'envers ( car les angles sont inversées etc...)
            elif action == 'backward':
                self.move_forward(value)
            elif action == 'left':
                self.turn_right()
            elif action == 'right':
                self.turn_left()
        self.history().clear() #Clear la liste (d'où le nom :/)