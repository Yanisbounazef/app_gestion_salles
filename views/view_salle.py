from services_salle import creer_salle, afficher_salles, supprimer_une_salle, modifier_une_salle

def menu():
    while True:
        print("\n===== MENU GESTION SALLES =====")
        print("1. Ajouter une salle")
        print("2. Afficher les salles")
        print("3. Modifier une salle")
        print("4. Supprimer une salle")
        print("5. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            code = input("Code : ")
            description = input("Description : ")
            categorie = input("Categorie : ")

            try:
                capacite = int(input("Capacite : "))
            except:
                print("Erreur : entre un nombre pour la capacite")
                continue

            creer_salle(code, description, categorie, capacite)
            print("Salle ajoutée avec succès")

        elif choix == "2":
            afficher_salles()

        elif choix == "3":
            code = input("Code a modifier : ")
            description = input("Nouvelle description : ")
            categorie = input("Nouvelle categorie : ")

            try:
                capacite = int(input("Nouvelle capacite : "))
            except:
                print("Erreur : entre un nombre pour la capacite")
                continue

            modifier_une_salle(code, description, categorie, capacite)
            print("Salle modifiée avec succès")

        elif choix == "4":
            code = input("Code a supprimer : ")
            supprimer_une_salle(code)
            print("Salle supprimée avec succès")

        elif choix == "5":
            print("Fin du programme")
            break

        else:
            print("Choix invalide")