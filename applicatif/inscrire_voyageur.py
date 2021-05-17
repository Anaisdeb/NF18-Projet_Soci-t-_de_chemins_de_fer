import psycopg2


def inscrire_voyageur(connexion):
    cur = connexion.cursor()
    nom = input("Veuillez rentrer votre nom svp ")
    prenom = input("Veuillez rentrer votre prénom svp ")
    adresse = input("Veuillez rentrer votre adresse svp ")
    num_tel = int(
        input("Veuillez rentrer votre numéro de téléphone (sur 10 chiffres) svp ")
    )
    reg = input('Etes vous un utilisateur régulier ? (répondre "oui" ou "non") ')

    # Si voyageur régulier -> Num_Carte + statut à définir
    if reg == "oui":
        regulier = True
        num_carte = int(
            input("Veuillez rentrer votre numéro de carte (sur 16 chiffres) svp ")
        )
        statut_int = int(
            input(
                "Quel type de voyageur êtes vous ? Répondez 1 pour voyageur, 2 pour grandVoyageur, 3 pour grandVoyageurPlus "
            )
        )
        if statut_int == 1:
            statut = "voyageur"
        if statut_int == 2:
            statut = "grandVoyageur"
        if statut_int == 3:
            statut = "grandVoyageurPlus"
        query = (
            "INSERT INTO Voyageur(nom,prenom,adresse,num_tel,num_carte, statut, regulier) VALUES('%s','%s','%s','%s','%s','%s','%s');"
            % (nom, prenom, adresse, num_tel, num_carte, statut, regulier)
        )
    # Si pas Voyageur Régulier : PAS de num_carte ou de statut
    else:
        regulier = False
        query = (
            "INSERT INTO Voyageur(nom,prenom,adresse,num_tel, regulier) VALUES('%s','%s','%s','%s',%s);"
            % (nom, prenom, adresse, num_tel, regulier)
        )

    try:
        cur.execute(query)
        connexion.commit()
    except psycopg2.DataError as e:
        print("L'élement n'a pas pu être inséré aux voyageurs")
        print("Message système :", e)
        connexion.rollback()
