"""
Ce fichier contient des fonctions et des constantes pour le calcul et la représentation de la phase de la lune.

Auteur : Rébecca Lapointe
Date : 20 mai 2023

Fonctions:
- age_lune(jour: int, mois: int, annee: int) -> float:
    Calcule l'âge de la lune en jours à partir d'une date donnée.

- est_croissante(age: float) -> bool:
    Vérifie si la lune est dans sa phase croissante.

- dessiner_lune(age: float, hemisphere_nord: bool = True):
    Dessine une représentation graphique de la lune en fonction de son âge.

- est_illuminee(position: float, largeur: int, luminosite: float, droite_eclairee: bool) -> bool:
    Vérifie si une position donnée dans la représentation graphique de la lune est éclairée.

- luminosite(age: float) -> float:
    Calcule la luminosité de la lune en fonction de son âge.

- phase(age: float) -> int:
    Détermine la phase de la lune en fonction de son âge.

- decrire_lune(jour: int, mois: int, annee: int):
    Affiche une description de la phase de la lune pour une date donnée.
"""
from lune.date import *
from lune.cercle import *

""" Constantes pour la phases de la lune """
PHASE_NOUVELLE_LUNE = 0
PHASE_PREMIER_CROISSANT = 1
PHASE_PREMIER_QUARTIER = 2
PHASE_GIBBEUSE_CROISSANTE = 3
PHASE_PLEINE_LUNE = 4
PHASE_GIBBEUSE_DECROISSANTE = 5
PHASE_DERNIER_QUARTIER = 6
PHASE_DERNIER_CROISSANT = 7

""" Durée du cycle lunaire """
CYCLE_LUNAIRE = 29.53

def age_lune(jour: int, mois: int, annee: int) -> float:
    """
    Calcule l'âge de la lune en jours à partir d'une date donnée.

    Parameters:
        - jour (int): Le jour.
        - mois (int): Le mois.
        - annee (int): L'année.

    Return:
        float : L'âge de la lune en jours.
    """
    date_nouvelle_lune_connue = jour_julien(13, 1, 2021)
    jours_depuis = jour_julien(jour, mois, annee) - date_nouvelle_lune_connue
    return jours_depuis % CYCLE_LUNAIRE

def est_croissante(age: float) -> bool:
    """
    Vérifie si la lune est dans sa phase croissante.

    Paramètres :
        - age (float) : L'âge de la lune en jours.

    Retour :
        bool : True si la lune est dans sa phase croissante, False sinon.
    """
    return age < CYCLE_LUNAIRE / 2

def dessiner_lune(age: float, hemisphere_nord: bool = True):
    """
    Dessine une représentation graphique de la lune en fonction de son âge.

    Parameters :
        - age (float): L'âge de la lune en jours.
        - hemisphere_nord (bool): Indique si on doit représenter la lune telle que vue dans l'hémisphère nord, ou. Par défaut, True.

    Returns :
        None
    """
    TAILLE_DESSIN = 21
    lum = luminosite(age)
    droite_eclairee = est_croissante(age) ^ (not hemisphere_nord)

    for i in range(TAILLE_DESSIN + 1):
        largeur = corde_horizontale(TAILLE_DESSIN, i)
        for j in range(TAILLE_DESSIN + 1):
            if est_dans_cercle(i, j, TAILLE_DESSIN):
                decalage = (TAILLE_DESSIN - largeur) / 2
                if est_illuminee(j - decalage, largeur, lum, droite_eclairee):
                    c = '██'
                else:
                    c = '  '
            else:
                c = '··'
            print(c, end = '')
        print()

def est_illuminee(position:int, largeur:int, luminosite:float, droite_eclairee: bool) -> bool:
    """
    Vérifie si une position dans la représentation graphique de la lune est éclairée pour une largeur de lune.

    Parameters:
        - position (int): La position à vérifier à partir du début de la lune à gauche
        - largeur (int): La largeur de la lune
        - luminosite (float): La luminosité de la lune.
        - droite_eclairee (bool): Indique si la droite ou la gauche de la lune est éclairée

    Returns:
        bool: True si la position est éclairée, False sinon.
    """
    if droite_eclairee:
        return (largeur - position) / largeur < luminosite
    else:
        return position / largeur < luminosite

def luminosite(age: float) -> float :
    """
    Calcule la luminosité de la lune en fonction de son âge.

    Parameters:
        - age (float): L'âge de la lune en jours.

    Returns :
        float: La luminosité de la lune.
    """
    mi_lune = CYCLE_LUNAIRE / 2
    if est_croissante(age):
        return age / mi_lune
    else:
        return (CYCLE_LUNAIRE - age) / mi_lune

def phase(age: float) -> int:
    """
    Détermine la phase de la lune en fonction de son âge.

    Parameters:
        - age (float): L'âge de la lune en jours.

    Returns:
        int: La phase de la lune (une valeur parmi les constantes PHASE_*)
    """
    l = luminosite(age)
    croissante = est_croissante(age)
    
    if l < 0.04:
        p = PHASE_NOUVELLE_LUNE
    elif l < 0.35:
        p = PHASE_PREMIER_CROISSANT if croissante else PHASE_DERNIER_CROISSANT
    elif l < 0.66:
        p = PHASE_PREMIER_QUARTIER if croissante else PHASE_DERNIER_QUARTIER
    elif l < 0.96:
        p = PHASE_GIBBEUSE_CROISSANTE if croissante else PHASE_GIBBEUSE_DECROISSANTE
    else:
        p = PHASE_PLEINE_LUNE 
    return p

def decrire_lune(jour: int, mois: int, annee: int):
    """
    Affiche une description de la phase de la lune pour une date donnée.

    Parameters:
        - jour (int): Le jour du mois.
        - mois (int): Le mois.
        - annee (int): L'année.

    Returns :
        None
    """
    age = age_lune(jour, mois, annee)
    p = phase(age)
    description = [
        "Nouvelle lune",
        "Premier croissant",
        "Premier quartier",
        "Gibbeuse croissante",
        "Pleine lune",
        "Gibbeuse décroissante",
        "Dernier quartier",
        "Dernier croissant"
    ][p]
    l = luminosite(age)
    print(f"En date du {jour}/{mois}/{annee}, à minuit heure locale.")
    print(f"La lune a {round(age)} jour(s).")
    print(f"Elle est dans sa phase {description}. ({round(l * 100)}%)")
    dessiner_lune(age)
    print()
