class Salle:
    def _init_(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        return f"Code: {self.code}, Description: {self.description}, Categorie: {self.categorie}, Capacite: {self.capacite}"