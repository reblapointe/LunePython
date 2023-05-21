
def corde_horizontale(diametre: int, hauteur: int) -> int :
    return sum(1 for j in range(diametre) if est_dans_cercle(hauteur, j, diametre))
        

def est_dans_cercle(rangee: int, colonne: int, diametre: float) -> bool:
    rayon = diametre / 2
    x = rangee - rayon
    y = colonne - rayon
    return x**2 + y**2 < rayon**2
