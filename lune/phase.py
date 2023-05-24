"""
    Ce fichier contient des fonctions et des constantes pour le calcul et la représentation de la phase de la lune.

    Auteur: Rébecca Lapointe
    Date: 20 mai 2023

    Fonctions:
        age_lune(jour: int, mois: int, annee: int) -> float:
            Calcule l'âge de la lune en jours à partir d'une date donnée.

        est_croissante(age: float) -> bool:
            Vérifie si la lune est dans sa phase croissante.

        dessiner_lune(age: float, hemisphere_nord: bool = True):
            Dessine une représentation graphique de la lune en fonction de son âge.

        est_illuminee(position: float, largeur: int, luminosite: float, droite_eclairee: bool) -> bool:
            Vérifie si une position donnée dans la représentation graphique de la lune est éclairée.

        luminosite(age: float) -> float:
            Calcule la luminosité de la lune en fonction de son âge.

        phase(age: float) -> str:
            Détermine la phase de la lune en fonction de son âge.

        decrire_lune(jour: int, mois: int, annee: int):
            Affiche une description de la phase de la lune pour une date donnée.
"""


import lune.date as date
import lune.cercle as cercle


""" Durée du cycle lunaire """
CYCLE_LUNAIRE = 29.53


def age_lune(jour: int, mois: int, annee: int) -> float:
    """
    Calcule l'âge de la lune en jours à partir d'une date donnée. L'âge de la lune correspond au nombre de jour 
    passé depuis la dernière nouvelle lune.

        Parameters:
            jour (int): Le jour.
            mois (int): Le mois.
            annee (int): L'année.

        Return:
            float: L'âge de la lune en jours.
    """
    date_nouvelle_lune_connue = date.jour_julien(13, 1, 2021)
    jours_depuis = date.jour_julien(jour, mois, annee) - date_nouvelle_lune_connue
    return jours_depuis % CYCLE_LUNAIRE


def est_croissante(age: float) -> bool:
    """
    Vérifie si la lune est dans sa phase croissante. La lune croit dans la première moitié de son cycle, puis elle décroit.

        Parameters:
            age (float): L'âge de la lune en jours.

        Returns
            bool: True si la lune est dans sa phase croissante, False sinon.
    """
    return age < CYCLE_LUNAIRE / 2


def dessiner_lune(age: float, hemisphere_nord: bool = True):
    """
    Dessine une représentation graphique de la lune en fonction de son âge.

        Parameters:
            age (float): L'âge de la lune en jours.
            hemisphere_nord (bool): Indique si on doit représenter la lune telle que vue dans l'hémisphère nord, ou. Par défaut, True.

        Returns:
            None
    """
    TAILLE_DESSIN = 21
    lum = luminosite(age)
    droite_eclairee = est_croissante(age) ^ (not hemisphere_nord)

    for i in range(TAILLE_DESSIN + 1):
        largeur = cercle.corde_horizontale(TAILLE_DESSIN, i) # Largeur du cercle lunaire à la ligne i
        for j in range(TAILLE_DESSIN + 1):
            if cercle.est_dans_cercle(i, j, TAILLE_DESSIN):
                decalage = (TAILLE_DESSIN - largeur) / 2 # début gauche du cercle lunaire
                if est_illuminee(j - decalage, largeur, lum, droite_eclairee):
                    c = "██" # portion illuminée
                else:
                    c = "  " # portion sombre
            else:
                c = "··" # voûte céleste
            print(c, end = "")
        print()

    # Example: Pour une lune de 5 jours (premier croissant, illuminée à 31%)
    #        ············································
    #        ··············          ██████··············
    #        ··········                ████████··········
    #        ········                    ████████········
    #        ······                      ██████████······
    #        ····                        ████████████····
    #        ····                        ████████████····
    #        ··                            ████████████··
    #        ··                            ████████████··
    #        ··                            ████████████··
    #        ··                            ████████████··
    #        ··                            ████████████··
    #        ··                            ████████████··
    #        ··                            ████████████··
    #        ··                            ████████████··
    #        ····                        ████████████····
    #        ······                      ██████████······
    #        ········                    ████████········
    #        ··········                ████████··········
    #        ··············          ██████··············
    #        ············································
        

def est_illuminee(position:int, largeur:int, luminosite:float, droite_eclairee: bool) -> bool:
    """
    Vérifie si une position dans la représentation graphique de la lune est éclairée 
    pour une largeur de dessin.

        Parameters:
            position (int): La position à vérifier à partir du début de la lune à gauche.
            largeur (int): La largeur de la lune.
            luminosite (float): La luminosité de la lune.
            droite_eclairee (bool): Indique si la droite ou la gauche de la lune est éclairée.

        Returns:
            bool: True si la position est éclairée, False sinon.
    """
    if droite_eclairee:
        return (largeur - position) / largeur < luminosite
    else:
        return position / largeur < luminosite


def luminosite(age: float) -> float:
    """
    Calcule la luminosité de la lune en fonction de son âge.
    La luminosité minimale est 0 à la nouvelle lune.
    La luminosité maximale est 1 à la pleine lune.

        Parameters:
            age (float): L'âge de la lune en jours.

        Returns:
            float: La luminosité de la lune.
    """
    mi_lune = CYCLE_LUNAIRE / 2
    if est_croissante(age):
        return age / mi_lune
    else:
        return (CYCLE_LUNAIRE - age) / mi_lune


def phase(age: float) -> str:
    """
    Détermine la phase de la lune en fonction de son âge.

        Parameters:
            age (float): L'âge de la lune en jours.

        Returns:
            str: le nom de la phase de la lune.
    """
    l = luminosite(age)
    croissante = est_croissante(age)
    
    if l < 0.04:
        p = "nouvelle lune"
    elif l < 0.35:
        p = "premier croissant" if croissante else "dernier croissant"
    elif l < 0.66:
        p = "premier quartier" if croissante else "dernier quartier"
    elif l < 0.96:
        p = "gibbeuse croissante" if croissante else "gibbeuse décroissante"
    else:
        p = "pleine lune" 
    return p


def decrire_lune(jour: int, mois: int, annee: int):
    """
    Affiche une description de la phase de la lune pour une date donnée.

        Parameters:
            jour (int): Le jour du mois.
            mois (int): Le mois.
            annee (int): L'année.

        Returns:
            None
    """
    age = age_lune(jour, mois, annee)
    l = luminosite(age)
    p = phase(age)
    print(f"En date du {jour}/{mois}/{annee}, à minuit heure locale.")
    print(f"La lune a {round(age)} jour(s).")
    print(f'Elle est dans sa phase "{p}". ({round(l * 100)}% illuminée)')
    dessiner_lune(age)
    print()
