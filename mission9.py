class Article : #Mettre une fonction spéciale qui fait que si 2 objet sont égaux, ils s'additionnent

    def __init__(self,d,p):
        self.__description = d
        self.__prix = p
        
    def description(self) :
        return self.__description

    def prix(self) :
        return self.__prix
        
    def taux_tva(self): 
        return 0.21   # TVA a 21%

    def tva(self):   
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        return self.prix() + self.tva()

    def __str__(self):
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())

class Facture :

    num_facture = 1

    def __init__(self, d, a_list):
        self.__description = d
        self.__articles = a_list
        self.num_facture = Facture.num_facture
        Facture.num_facture += 1 #Quand on le lance une fois, variable de class+1 qui n'est pas réinitialisé à la prochaine instance
        
    def description(self) :
        return 'Facture No {} : {}'.format(self.num_facture, self.__description)
    
    def __str__(self):
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        return self.description() + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC") \
               + self.barre_str()

    def barre_str(self):
        barre_longeur = 83
        return "="*barre_longeur + "\n"

    def article_str(self, art):
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        return self.barre_str() \
               + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva) \
               + self.barre_str()
        
    def articles(self):
        return self.__articles

#------------------------------------------ Partie Livraison ------------------------------------------

    def nombre(self, pce):
        return sum(article.nombre() for article in self.articles() if article.piece() == pce)

    def description_livraison(self):
        return 'Livraison - Facture No {} : {}'.format(self.num_facture, self.__description)

    def entete_livraison_str(self):
        return self.description_livraison() + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description", "poids/pce", "nombre", "poids") \
               + self.barre_str()

    def livraison_str(self, art):
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.poids(), art.nombre(), art.poidstotpce())

    def print_livraison(self):
        s = self.entete_livraison_str()
        totalNombre = 0
        totalPoids = 0.00
        for art in self.__articles:
            s += self.livraison_str(art)
            totalNombre += art.nombre()
            totalPoids += art.poidstotpce()
        s += self.totaux_livraison_str(totalNombre, totalPoids)
        return s

    def totaux_livraison_str(self, nombre, poids):
        return self.barre_str() \
               + "| {0:40} | {1:10} | {2:10.2f} | {3:10.2f} |\n".format(f"{nombre} articles", "", nombre, poids) \
               + self.barre_str()

class ArticleReparation(Article):

    fixe = 20

    def __init__(self, duree):
        super().__init__('Reparation', 0)
        self.duree = duree

    def description(self):
        return 'Reparation ({:.2f} heures)'.format(self.duree)
    
    def prix(self):
        return ArticleReparation.fixe + 35 * self.duree

class Piece(Article):

    def __init__(self, d, p, pds=None, fr=False, tva_red=False):
        super().__init__(d, p)
        self.__poids = pds
        self.__fragile = fr
        self.__tva_reduit = tva_red

    def poids(self):
        return self.__poids
    
    def fragile(self):
        return self.__fragile

    def tva_reduit(self):
        return self.__tva_reduit

    def poidstotpce(self):
        return self.poids() * self.nombre()

    def __eq__(self, other):
        return self.prix() == other.prix() and self.description() == other.description()

class ArticlePiece(Piece):

    def __init__(self, nombre, piece, d, p, pds=None, fr=False, tva_red=False):
        super().__init__(d, p, pds, fr, tva_red)
        self.__nombre = nombre
        self.__piece = piece

    def nombre(self):
        return self.__nombre
    
    def piece(self):
        return self.__piece

    def description(self):
        fr = ' (!)' if self.fragile() else ''
        return '{} * {} @ {}{}'.format(self.nombre(), super().description(), super().prix(), fr)

    def prix(self):
        return super().prix() * self.nombre()

    def taux_tva(self):
        return 0.06 if self.tva_reduit() else 0.21

"""
souris = ArticlePiece(9, 'souris', 'souris bluetooth', 9.99, 10, False, True) #nombre, piece, description, prix, poids, fragile, tva_red
clavier = ArticlePiece(1, 'clavier', 'clavier bluetooth', 19.99, True, True, True)

ordinateur = ArticlePiece(1, 'ordinateur', 'rgb 4090rtx', 999.99, 1, True, False)
vis = ArticlePiece(100, 'vis', 'vis à bois', 0.01, 0.01, False, True)

charette2 = [ordinateur, vis]

charette1 = [souris, clavier]


chaise = ArticleReparation(0.75)
repa = [chaise]
Facture3 = Facture('IKEA', repa)


Facture1 = Facture('PC Store - 22 novembre', charette1)

Facture2 = Facture('PC Store - 22 novembre', charette2)

print(Facture3)
print(Facture2.print_livraison())
print(Facture1)
print(Facture2)"""

#Des exemples si tu le souhaites