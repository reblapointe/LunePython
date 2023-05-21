
def est_bissextile(annee: int) -> bool:
    return annee % 400 == 0 or annee % 4 == 0 and annee % 100 != 0
    
def nb_jours_dans_mois(annee: int, mois: int) -> int:
    match (mois):
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 29 if est_bissextile(annee) else 28
        case _:
            return 31

def est_date_valide(jour: int, mois: int, annee: int) -> bool:
    return 1 <= jour <= nb_jours_dans_mois(annee, mois) and 1 <= mois <= 12     

def jour_julien(jour: int, mois: int, annee: int) -> int:
    return 1461 * (annee + 4800 + (mois - 14) // 12) // 4 + 367 * (mois - 2 - 12 * ((mois - 14) // 12)) // 12 - 3 * ((annee + 4900 + (mois - 14) // 12) // 100) // 4 + jour - 32075;
