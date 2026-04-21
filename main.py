from data.dao_salle import connecter_db

print("Avant connexion")

try:
    conn = connecter_db()
    print("Connexion réussie")
except Exception as e:
    print("Erreur :", e)

print("Fin du programme")