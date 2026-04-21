from data.dao_salle import recuperer_salles

salles = recuperer_salles()

for salle in salles:
    print("Code :", salle.code)
    print("Description :", salle.description)
    print("Categorie :", salle.categorie)
    print("Capacite :", salle.capacite)
    print("-------------------")