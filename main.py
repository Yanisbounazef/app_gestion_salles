from data.dao_salle import ajouter_salle, modifier_salle
from models.salle import Salle

# Ajouter une salle
salle1 = Salle("B101", "Salle informatique", "Laboratoire", 25)
ajouter_salle(salle1)

# Modifier la salle
modifier_salle("B101", "Salle informatique MODIF", "Laboratoire", 30)