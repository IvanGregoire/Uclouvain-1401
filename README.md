Réalisé par Ivan Grégoire et Alexandre Groteclaes

Le README a été écrit par chatgpt, mais un exemple est disponible dans le code à la toute fin

Pour faire une facture il faut :

1) Créer une instance de ArticlePiece(nombre, nom, description, prix unitaire HTVA, poids (optionnel), fragilité (optionnel), TVA réduite (optionnel)) ou créer une instance ArticleReparation(heure)

2) Créer une liste avec toutes les instances

3) Créer une instance facture

4) 2 choix possibles : 

	- print(Facture) ou print(Facture.print_livraison()) 

ATTENTION, pour pouvoir imprimer une facture de livraison, il faut impérativement avoir le poids et la tva 
