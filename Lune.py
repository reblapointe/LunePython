from Date import *
from Cercle import *

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
    return jours_depuis % CYCLE_LUNAIRE

def est_croissante(age: float) -> bool:
    return age < CYCLE_LUNAIRE / 2

def dessiner_lune(age: float, hemisphere_nord: bool = True):
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

def est_illuminee(position:float, largeur:int, luminosite:float, droite_eclairee: bool) -> bool:
    if droite_eclairee:
        return (largeur - position) / largeur < luminosite
    else:
        return position / largeur < luminosite

def luminosite(age: float) -> float :
    mi_lune = CYCLE_LUNAIRE / 2
    if est_croissante(age):
        return age / mi_lune
    else:
        return (CYCLE_LUNAIRE - age) / mi_lune

def phase(age: float) -> int:
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
    age = age_lune(jour, mois, annee)
    p = phase(age)
    if p == PHASE_NOUVELLE_LUNE: 
        description = "Nouvelle lune"
    elif p == PHASE_PREMIER_CROISSANT: 
        description = "Premier croissant"
    elif p == PHASE_PREMIER_QUARTIER: 
        description = "Premier quartier"
    elif p == PHASE_GIBBEUSE_CROISSANTE: 
        description = "Gibbeuse croissante"
    elif p == PHASE_PLEINE_LUNE: 
        description = "Pleine lune"
    elif p == PHASE_GIBBEUSE_DECROISSANTE: 
        description = "Gibbeuse décroissante"
    elif p == PHASE_DERNIER_QUARTIER: 
        description = "Dernier quartier"
    elif p == PHASE_DERNIER_CROISSANT: 
        description = "Dernier croissant"
    else: 
        description = "Pas une phase"
    l = luminosite(age)
    print(f"En date du {jour}/{mois}/{annee}, à minuit heure locale.")
    print(f"La lune a {round(age)} jour(s).")
    print(f"Elle est dans sa phase {description}. ({round(l * 100)}%)")
    dessiner_lune(age)
    print()
