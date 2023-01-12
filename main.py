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


def verif(formule):
    if test(formule[len(formule) - 1]) is False:
        raise Exception("Erreur Fin : Ne pas mettre de nombre a la fin")
    ope = 0
    chiffre = 0
    nombre = ""
    for i in range(len(formule)):
        if test(formule[i]):
            ope += 1
        else:
            if formule[i] != ' ':
                nombre += formule[i]
            else:
                if nombre != "":
                    chiffre += 1
                    nombre = ""
    if ope == chiffre - 1:
        return True
    else:
        raise Exception("Erreur Ratio : Mauvais Ration Nombre/Operateur")


def verif_debut(chaine):
    count = 0
    i = 0
    while count != 2:
        if test(chaine[i]) is True:
            raise Exception("Erreur Debut : Minimum deux nombres")
        if chaine[i] == ' ':
            count += 1
        i += 1
    return True


def verif_total(chaine):
    if verif_debut(chaine) and verif(chaine):
        return True
    else:
        return False


def test(char):
    if char == '+' or char == '-' or char == '*' or char == '/':
        return True
    else:
        return False


def calcul(op, pile):
    a = int(pile.get())
    pile.pop()
    b = int(pile.get())
    pile.pop()
    if op == '+':
        return b + a
    elif op == '-':
        return b - a
    elif op == '*':
        return b * a
    elif op == '/':
        if a == 0:
            raise Exception("Erreur Division - Pas de Division par 0")
        return b / a


def process(chaine):
    pile1 = Pile()
    val = ""
    for i in range(len(chaine)):
        if test(chaine[i]):
            if i != len(chaine) - 1:
                if (chaine[i + 1] != ' ' and chaine[i - 1] != ' ') is False:
                    raise Exception("Erreur Operateur : Séparer les nombres et les opérateurs avec ' '")
            pile1.add(calcul(chaine[i], pile1))
        else:
            if chaine[i] != ' ':
                val += chaine[i]
            else:
                if val != "":
                    pile1.add(val)
                    val = ""
    return pile1.afficher()


def main():
    chaine = input("Entrez une formule : ")
    if verif_total(chaine):
        process(chaine)


main()
