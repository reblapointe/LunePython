    
from Date import *

PHASE_NOUVELLE_LUNE = 0
PHASE_PREMIER_CROISSANT = 1
PHASE_PREMIER_QUARTIER = 2
PHASE_GIBBEUSE_CROISSANTE = 3
PHASE_PLEINE_LUNE = 4
PHASE_GIBBEUSE_DECROISSANTE = 5
PHASE_DERNIER_QUARTIER = 6
PHASE_DERNIER_CROISSANT = 7

CYCLE_LUNAIRE = 29.53

def age_lune(jour: int, mois: int, annee: int) -> float:
    date_nouvelle_lune_connue = jour_julien(13, 1, 2021)
    jours_depuis = jour_julien(jour, mois, annee) - date_nouvelle_lune_connue
    nb_nouvelles_lunes_depuis = jours_depuis / CYCLE_LUNAIRE
    age = nb_nouvelles_lunes_depuis % 1 * CYCLE_LUNAIRE
    if age < 0:        
        age += CYCLE_LUNAIRE
    return age

def est_dans_cercle(rangee: int, colonne: int, diametre: float) -> bool:
    rayon = diametre / 2
    x = rangee - rayon
    y = colonne - rayon
    return x**2 + y**2 < rayon**2

def est_croissante(age: float) -> bool:
    return age < CYCLE_LUNAIRE / 2

def dessiner_lune(age: float, hemisphere_nord: bool = True):
    TAILLE_DESSIN = 21
    l = luminosite(age)
    droite_eclairee = est_croissante(age)
    if not hemisphere_nord:
        droite_eclairee = not droite_eclairee
    for i in range(TAILLE_DESSIN + 1):
        largeur = 0
        for j in range(TAILLE_DESSIN):
            if est_dans_cercle(i, j, TAILLE_DESSIN):
                largeur += 1

        for j in range(TAILLE_DESSIN + 1):
            if est_dans_cercle(i, j, TAILLE_DESSIN):
                decalage = (TAILLE_DESSIN - largeur) / 2
                if est_illuminee(j - decalage, largeur, l, droite_eclairee):
                    print('██', end = '')
                else:
                    print('  ', end = '')
            else:
                print('··', end = '')
        print()

def est_illuminee(position:float, largeur:int, luminosite:float, droite_eclairee: bool) -> bool:
    return droite_eclairee and (largeur - position) / largeur < luminosite or not droite_eclairee and (position / largeur < luminosite)

def luminosite(age: float) -> float :
    if est_croissante(age):
        return age / (CYCLE_LUNAIRE / 2)
    else:
        return (CYCLE_LUNAIRE - age) / (CYCLE_LUNAIRE / 2)

def phrase(age: float) -> int:
    l = luminosite(age)
    croissante = est_croissante(age)
    if l < 0.04:
        p = PHASE_NOUVELLE_LUNE
    elif l < 0.35:
        if croissante:
            p = PHASE_PREMIER_CROISSANT
        else:
            p = PHASE_DERNIER_CROISSANT
    elif l < 0.66:
        if croissante:
            p = PHASE_PREMIER_QUARTIER
        else:
            p = PHASE_DERNIER_QUARTIER
    elif l < 0.96:
        if croissante:
            p = PHASE_GIBBEUSE_CROISSANTE
        else:
            p = PHASE_GIBBEUSE_DECROISSANTE
    else:
        p = PHASE_PLEINE_LUNE 
    return p