class Niveau:
    def __init__(self, vitesseBalle, vitesseRaquette, pourcentageBriquesModifie, pourcentageBonus):
        self.vitesseBalle = 5
        self.vitesseRaquette = 5
        self.pourcentageBriquesModifie = 0.5
        self.pourcentageBonus = 0.08

    def __str__(self):
        return f"Niveau({self.vitesseBalle}, {self.vitesseRaquette}, {self.pourcentageBriquesModifie}, {self.pourcentageBonus})"




def get_page(nom):
    # Retourne la classe correspondante en fonction du nom du bouton
    mapping = {
        "Niveau1": Niveau(5, 5, 0.5, 0.08),
        "Niveau2": Niveau(6, 6, 0.5, 0.08),
        "Niveau3": Niveau(7, 7, 0.5, 0.08),
    }
    if nom == "Quitter":
        exit(0)
    print(f"get_page({nom}) nom")
    print(mapping[nom])
    return mapping[nom]

test = "2"
dict = {"1": "a", "2": Niveau(6, 6, 0.5, 0.08), "3": Niveau(7, 7, 0.5, 0.08),}
print(dict[test])