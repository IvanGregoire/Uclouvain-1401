class Node:
    def __init__(self, data=None):
        self.__data = data
        self.next = None #A None s'il n'y a pas de prochain
    def value(self):
        return self.__data

class OrderedLinkedList:
    def __init__(self):
        self.head = None #Tête de liste 

    def length(self):
        current = self.head
        total = 1 
        if current is None:
            return 0
        while current.next is not None:
            total +=1
            current = current.next
        return total

    def add(self, data):
        new_node = Node(data) #Crée une instance de Node comportant le data
        if self.head is None or data < self.head.value():
            new_node.next = self.head #Le data du premier est devenu le data du second (d'où le .next)
            self.head = new_node
            return

        current = self.head #Si une valeur est déjà attribué 
        while current.next is not None and data >= current.next.value():
            current = current.next
            
        new_node.next = current.next #Je prend le node du current.next et je dis qu'il est maintenant décalé de 1 unité
        current.next = new_node #J'en ai marre des nexts
    
    def remove(self,data):
        if self.head is None:
            return 

        if self.head.value() == data:
            self.head = self.head.next #Si le premier doit être supprimé, on le remplace par le 2ème
            return

        current = self.head
        while current.next is not None: #Vérifie qu'on est pas à la fin
            if current.next.value() == data:
                current.next = current.next.next
                return
            current = current.next
  
    def __str__(self):
        result = []

        if self.head is None:
            raise Exception("Hagrid a mangé toute la soupe")

        current = self.head
        while current is not None: #Pas de current.next comme ça on inclus le dernier noeud
            result.append(current.value())
            current = current.next
        return ", ".join(map(str, result)) #"séparateur".join(itérable en str) si l'itérable n'est pas en str, convertir avec map(type, itérable)

"""classement = OrderedLinkedList()
classement.add(10)
classement.add(20)
classement.add(30)
print(classement)
classement.remove(10)
print(classement)
print(classement.length())"""