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