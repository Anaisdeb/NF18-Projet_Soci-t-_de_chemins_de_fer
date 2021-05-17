def afficher_billet(connexion):
    cur = connexion.cursor()
    # afficher les billets
    num_billet = int(input("Quel est le numéro de votre billet svp ?"))
    query = ("SELECT * FROM Billet where id=%s") % num_billet

    cur.execute(query)
    row = cur.fetchone()
    print(
        "Votre billet a pour gare de départ, la %s et pour gare d'arrivée, la %s"
        % (row[1], row[3])
    )
    # modifier un des trajets du billet
    if row[5] == True:
        answer = input(
            "Vous avez souscrit à une assurance pour votre billet et êtes autorisé à la modifier, voulez vous le modifier ? Répondez oui ou non."
        )
        # on appelle la fonction reserver billet, puis on récupère l'ID du billet
        if answer == "oui":
            query = "SELECT COUNT(*) FROM Trajet WHERE trajet.id = %s" % num_billet
            cur.execute(query)
            nombre_traj = cur.fetchone()
            print("Votre billet est composé de %s trajet(s)" % nombre_traj)
            query = "SELECT * from Trajet WHERE trajet.id = %s" % num_billet
            cur.execute(query)
            trajets = cur.fetchall()
            print(
                "Trajet n° ***** Gare de départ         ***** ville de départ         ***** Heure de départ       *****Gare d'arrivée      *****ville d'arrivée       *****heure d'arrivée \n \n \n  ",
            )
            i = 1
            for raw in trajets:
                query = (
                    "SELECT horaire.depart, horaire.arrivee, arret.nom_gare, arret.ville FROM Trajet, Horaire, arret WHERE Trajet.id = %d AND trajet.horaire_depart = %d AND trajet.horaire_depart=horaire.id AND horaire.rang=arret.rang AND horaire.code_ligne=arret.code_ligne"
                    % (num_billet, trajets[1])
                )

                cur.execute(query)
                depart = cur.fetchone()
                print(
                    f"  {i}       ***** {depart[2]}       *****{depart[3]}                   *****    {depart[0]}       ",
                    end="",
                )
                query = (
                    "SELECT horaire.depart, horaire.arrivee, arret.nom_gare, arret.ville FROM Trajet, Horaire, arret WHERE Trajet.id = %d AND trajet.horaire_arrivee= %d AND trajet.horaire_arrivee=horaire.id AND horaire.rang=arret.rang AND horaire.code_ligne=arret.code_ligne"
                    % (num_billet, trajets[2])
                )
                cur.execute(query)
                arrivee = cur.fetchone()
                print(
                    f"*****    {arrivee[2]}      *****     {arrivee[3]}     *****    {arrivee[1]}"
                )

                i += 1

    else:
        print("Entendu, Bon voyage!!!")
