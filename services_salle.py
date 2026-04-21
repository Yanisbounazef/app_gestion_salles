from data.dao_salle import ajouter_salle, recuperer_salles, supprimer_salle, modifier_salle
from models.salle import Salle

def creer_salle(code, description, categorie, capacite):
    salle = Salle(code, description, categorie, capacite)
    ajouter_salle(salle)

def afficher_salles():
    return recuperer_salles()

def supprimer_une_salle(code):
    supprimer_salle(code)

def modifier_une_salle(code, description, categorie, capacite):
    modifier_salle(code, description, categorie, capacite)