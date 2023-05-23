"""
    Utilitaire pour un cercle console. Les coordonnées sont toutes entières
    
    Auteur: Rébecca Lapointe
    Date: 20 mai 2023
    
    Fonctions:
    corde_horizontale(diametre: int, hauteur: int) -> int:
        Calcule la norme entière d'une corde horizontale dans un cercle.

    est_dans_cercle(rangee: int, colonne: int, diametre: float) -> bool:
        Vérifie si un point est situé à l'intérieur d'un cercle.
"""


def corde_horizontale(diametre: int, hauteur: int) -> int:
    """
    Calcule la norme entière d'une corde horizontale dans un cercle.

        Parameters:
            diametre (int): Le diamètre du cercle.
            hauteur (int): La hauteur de la corde.

        Returns:
            int: Le nombre de points situés sur la corde horizontale.
    """
    return sum(1 for j in range(diametre) if est_dans_cercle(hauteur, j, diametre))
        

def est_dans_cercle(rangee: int, colonne: int, diametre: float) -> bool:
    """
    Vérifie si un point est situé à l'intérieur d'un cercle.

        Parameters:
            rangee (int): La position en x du point.
            colonne (int): La position en y du point.
            diametre (float): Le diamètre du cercle.

        Returns:
            bool: True si le point est à l'intérieur du cercle, False sinon.
    """
    rayon = diametre / 2
    x = rangee - rayon
    y = colonne - rayon
    return x**2 + y**2 < rayon**2
