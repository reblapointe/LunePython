"""
    Affiche un dessin de la lune, telle que vu aujourd'hui, puis à une date choisie par l'utilisateur, dans le ciel de l'hémisphère nord.
"""


from datetime import datetime # pour obtenir la date d'aujourd'hui
from lune.phase import *


def main():
    print('Lune actuelle')
    aujourdhui = datetime.today()
    jour = aujourdhui.day
    mois = aujourdhui.month
    annee = aujourdhui.year

    decrire_lune(jour, mois, annee)
    print()

    valide = True
    while valide:
        print('-------------------------------------------------------------------')
        print('Entrez une date pour voir l\'état de la lune. Pour quitter, entrez Q')

        try: 
            # Lire les trois nombres
            jour = int(input('Entrez un jour '))
            mois = int(input('Entrez un mois '))
            annee = int(input('Entrez une annee '))
            if est_date_valide(jour, mois, annee):
                decrire_lune(jour, mois, annee)
                print()
            else:
                print('Ceci n\'est pas une date.')
        except:
            valide = False


if __name__ == "__main__":
    main()
