"""
    Utilitaire pour les dates.

    Auteur: Rébecca Lapointe
    Date: 20 mai 2023


    Fonctions: 
        est_bissextile(annee: int) -> bool:
            Vérifie si une année donnée est bissextile.

        nb_jours_dans_mois(annee: int, mois: int) -> int:
            Retourne le nombre de jours dans un mois donné d'une année donnée. 
            Retourne 31 pour un mois invalide.

        est_date_valide(jour: int, mois: int, annee: int) -> bool:
            Vérifie si une date donnée est valide.

        def jour_julien(jour: int, mois: int, annee: int) -> int:
            Calcule le jour julien correspondant à une date donnée.
            Le jour julien initial est le 1er janvier de l'année -4712 (avant notre ère) à midi (heure universelle). 
"""


def est_bissextile(annee: int) -> bool:
    """
    Vérifie si une année donnée est bissextile.

        Parameters:
            annee (int): L'année à vérifier.

        Returns:
            bool: True si l'année est bissextile, False sinon.
    """
    return annee % 400 == 0 or annee % 4 == 0 and annee % 100 != 0
    

def nb_jours_dans_mois(annee: int, mois: int) -> int:
    """
    Retourne le nombre de jours dans un mois donné d'une année donnée. 
    Retourne 31 pour un mois invalide.

        Parameters:
            annee (int): L'année.
            mois (int): Le mois (1 pour janvier, 2 pour février, etc.).

        Returns:
            int: Le nombre de jours dans le mois spécifié. 31 pour un mois qui n'existe pas.
    """
    match (mois):
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            return 29 if est_bissextile(annee) else 28
        case _:
            return 31


def est_date_valide(jour: int, mois: int, annee: int) -> bool:
    """
    Vérifie si une date donnée est valide.

        Parameters:
            jour (int): Le jour.
            mois (int): Le mois.
            annee (int): L'année.

        Returns:
            bool: True si la date est valide, False sinon.
    """
    return 1 <= jour <= nb_jours_dans_mois(annee, mois) and 1 <= mois <= 12     


def jour_julien(jour: int, mois: int, annee: int) -> int:
    """
    Calcule le jour julien correspondant à une date donnée.
    Le jour julien initial est le 1er janvier de l'année -4712 (avant notre ère) à midi (heure universelle). 

        Parameters:
            jour (int): Le jour.
            mois (int): Le mois.
            annee (int): L'année.

        Returns:
            int: Le jour julien correspondant à la date spécifiée.
    """
    return 1461 * (annee + 4800 + (mois - 14) // 12) // 4 + 367 * (mois - 2 - 12 * ((mois - 14) // 12)) // 12 - 3 * ((annee + 4900 + (mois - 14) // 12) // 100) // 4 + jour - 32075;
