from Lune import *
from datetime import datetime

def main():
    print('Lune actuelle')
    aujourdhui = datetime.today()
    jour = aujourdhui.day
    mois = aujourdhui.month
    annee = aujourdhui.year

    age = age_lune(jour, mois, annee)
    p = phrase(age)
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

    valide = True
    
    print("-------------------------------------------------------------------")
    print("Entrez une date pour voir l'état de la lune. Pour quitter, entrez Q")

    # Lire les trois nombres
    jour = int(input("Entrez un jour "))
    mois = int(input("Entrez un mois "))
    annee = int(input("Entrez une annee "))
    
    if est_date_valide(jour, mois, annee):
        age = age_lune(jour, mois, annee)
        p = phrase(age)
        l = luminosite(age)
        print(f"En date du {jour}/{mois}/{annee}, à minuit heure locale.")
        print(f"La lune a {round(age)} jour(s).")
        print(f"Elle est dans sa phase ({round(l * 100)}%)")
        dessiner_lune(age)
        print()
    else:
        print("Ceci n'est pas une date")

if __name__ == "__main__":
    main()
