from orderedlinkedlist import *
from resultat import *

class Classement :
    """
    Une implémentation primitive de classement, non ordonnée et de capacité fixe.
    @author Kim Mens
    @version 01 Décembre 2019
    """

    __maxcapacity = 10

    def __init__(self):
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        self.__resultats = OrderedLinkedList()   # Une liste ordonnée
        self.__size = 0         # nombre de résultats actuel (initialement 0, maximum __maxcapacity)

    def size(self): #liste est une instance d'OrderedLinkedList
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.__resultats.length()

    def add(self,r):
        """
        Ajoute un résultat r dans ce classement.
        @pre:  r est une instance de la classe Resultat
        @post: Le résultat r a été inséré selon l'ordre du classement.
               En cas d'ex-aequo, r est inséré après les autres résultats de même ordre.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Le résultat est simplement ajouté à la dictionnaire, sans tenir compte de l'ordre.
                    Une dictionnaire ne donne pas de garanties sur l'ordre des éléments.
        """
        if self.size() >= self.__maxcapacity :
            raise Exception("Capacity of classement exceeded") #raise Error() faisait des erreurs chez moi
        else :
            self.__resultats.add(r) #J'arrange le tout pour que ce soit en lien avec mes listes

    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        current = self.__resultats.head
        while current is not None:
            if current.value().coureur() == c:
                return current.value() #retourne le nom et le temps
            current = current.next
        return None



    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Etant donné que la dictionnaire de résultats ne connaît pas de position,
                    pour le moment cette méthode retourne toujours "***position inconnue***".
                    A vous de la corriger en utilisant une liste chaînée ordonnée
                    comme structure de données, plutôt qu'une simple dictionnaire.
        """
        position = 1
        current = self.__resultats.head
        while current is not None:  # Vérifie directement current, pas current.next
            if current.value().coureur() == c:
                return position
            current = current.next
            position += 1
        return -1
        

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        
        current = self.__resultats.head 
        while current is not None:
            if current.value().coureur() == c: 
                self.__resultats.remove(current.value())  #Remplace en utilisant la méthode définie dans le fichier de la liste
                self.__size -= 1
                return c
            current = current.next
        return False 

    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = ""
        position = 1
        current = self.__resultats.head
        while current.next is not None:
            s += f"{position} : {str(current.value())}\n"
            current = current.next
            position += 1
        return s
    
