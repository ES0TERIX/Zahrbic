class Pile:
    """ Classe Pile dans laquelle  a été codé le principe de la pile """
    pile = []

    def pop(self):
        self.pile[-1:] = []
        return self.pile

    def add(self, item):
        self.pile[len(self.pile):] = [item]
        return self.pile

    def afficher(self):
        print(self.pile)

    def get(self):
        return self.pile[-1]


def verif(chaine):
    """Fonction qui vérifie si la chaine est correcte
    - vérifie le nombre d'opérateurs et nombres
    - vérifie si le dernier caractère est opérateur
    - vérifie que chaque element est bien séparé par un espace
    """
    if test_operateur(chaine[len(chaine) - 1]) is False:
        raise Exception("Erreur Fin : Ne pas mettre de nombre a la fin")
    nb_operateur = 0
    nb_chiffre = 0
    chaine_nombre = ""
    for i in range(len(chaine)):
        if test_operateur(chaine[i]):
            nb_operateur += 1
        else:
            if chaine[i] != ' ':
                chaine_nombre += chaine[i]
            else:
                if chaine_nombre != "":
                    nb_chiffre += 1
                    chaine_nombre = ""
    if nb_operateur == nb_chiffre - 1:
        return True
    else:
        raise Exception("Erreur Ratio : Mauvais Ration Nombre/Operateur")


def verif_debut(chaine):
    """
    Vérifie que les deux premiers éléments de la chaine sont bien des nombres
    """
    count = 0
    i = 0
    while count != 2:
        if test_operateur(chaine[i]) is True:
            raise Exception("Erreur Debut : Minimum deux nombres")
        if chaine[i] == ' ':
            count += 1
        i += 1
    return True


def verif_total(chaine):
    """Réalise toute les verifications de la chaine"""
    if verif_debut(chaine) and verif(chaine):
        return True
    else:
        return False


def test_operateur(char):
    """Vérifie si le caractère est un opérateur et retourne vrai ou faux"""
    if char == '+' or char == '-' or char == '*' or char == '/':
        return True
    else:
        return False


def calcul(operateur, pile):
    """Fonction qui réalise le calcul entre deux nombres en fonction de l'opérateur"""
    a = int(pile.get())
    pile.pop()
    b = int(pile.get())
    pile.pop()
    if operateur == '+':
        return b + a
    elif operateur == '-':
        return b - a
    elif operateur == '*':
        return b * a
    elif operateur == '/':
        if a == 0:
            raise Exception("Erreur Division - Pas de Division par 0")
        return b / a


def process(chaine):
    """Parcours la chaine et réalise les calculs"""
    pile1 = Pile()
    chaine_nombre = ""
    for i in range(len(chaine)):
        if test_operateur(chaine[i]):
            if i != len(chaine) - 1:
                if (chaine[i + 1] != ' ' and chaine[i - 1] != ' ') is False:
                    raise Exception("Erreur Operateur : Séparer les nombres et les opérateurs avec ' '")
            pile1.add(calcul(chaine[i], pile1))
        else:
            if chaine[i] != ' ':
                chaine_nombre += chaine[i]
            else:
                if chaine_nombre != "":
                    pile1.add(chaine_nombre)
                    chaine_nombre = ""
    return pile1.afficher()


def main():
    chaine = input("Entrez une formule : ")
    if verif_total(chaine):
        process(chaine)


main()
