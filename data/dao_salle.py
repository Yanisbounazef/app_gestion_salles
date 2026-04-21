import mysql.connector
import json
from models.salle import Salle

def connecter_db():
    print("Ouverture config")

    with open("data/config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    print("Config lue :", config)

    connexion = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
        use_pure=True
    )

    print("Connexion créée")
    return connexion
def ajouter_salle(salle):
    connexion = connecter_db()
    curseur = connexion.cursor()

    requete = """
    INSERT INTO salle (code, description, categorie, capacite)
    VALUES (%s, %s, %s, %s)
    """

    valeurs = (salle.code, salle.description, salle.categorie, salle.capacite)

    curseur.execute(requete, valeurs)
    connexion.commit()

    print("Salle ajoutée avec succès")

    curseur.close()
    connexion.close()