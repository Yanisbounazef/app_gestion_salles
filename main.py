from models.salle import Salle
from data.dao_salle import ajouter_salle

salle1 = Salle("B101", "Salle informatique", "Laboratoire", 25)
ajouter_salle(salle1)