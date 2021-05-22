from chercher_trajet import *


def afficher_trajet(num_billet, cur):
    query = "SELECT COUNT(*) FROM Trajet WHERE trajet.id = %s" % num_billet #Requête nombre de trajet relié au billet
    cur.execute(query)
    nombre_traj = cur.fetchone()
    print()
    print("Votre billet est composé de %s trajet(s)" % nombre_traj) #affichage
    print()
    if nombre_traj[0] != 0: #alors on affiche les trajets du billet
        query = "SELECT * from Trajet WHERE trajet.id = %s" % num_billet #Requête des trajets lié à un numéro de billet précis
        cur.execute(query)
        trajets = cur.fetchall()
        print()
        print(
            "Trajet n° ***** Gare de départ         ***** ville de départ         ***** Heure de départ       *****Gare d'arrivée      *****ville d'arrivée       *****heure d'arrivée \n \n \n  ",
        )
        i = 1
        dico = {}
        for raw in trajets:

            query = (
                "SELECT horaire.depart, arret.nom_gare, arret.ville \
                    FROM Trajet, Horaire, arret \
                    WHERE Trajet.id=%s AND Trajet.place=%s AND  trajet.horaire_depart=horaire.id  AND  horaire.rang=arret.rang AND arret.code_ligne=horaire.code_ligne;"
                % (raw[0], raw[1]) #raw[1] contient l'ID du billet, raw[2] la place dans le train. Ces 2 attributs = clé primaire d'un trajet
            )

            dico[i] = raw[1] #chaque numéro de siège est associé à l'incrémenteur i
            cur.execute(query)
            depart = cur.fetchone()
            print(
                f"  {i}       ***** {depart[1]}       *****{depart[2]}                   *****    {depart[0]}       ",
                end="",
            ) #on affiche dans un premier temps les infos lié à la gare de départ
            query = (
                "SELECT horaire.depart, arret.nom_gare, arret.ville \
                    FROM Trajet, Horaire, arret\
                        WHERE Trajet.id=%s AND Trajet.place=%s AND  trajet.horaire_arrivee=horaire.id  AND  horaire.rang=arret.rang AND arret.code_ligne=horaire.code_ligne;"
                % (raw[0], raw[1]) 
            ) 

            cur.execute(query)
            arrivee = cur.fetchone()
            print(
                f"*****    {arrivee[1]}      *****     {arrivee[2]}     *****    {arrivee[0]}"
            ) #puis les infos liées à la gare d'arrivée, tout cela sur une ligne

            i += 1
        print()
        print()
        return dico #retourne chaque numéro de siège associé à un incrementeur


def delete_trajet(num_billet, cur, connexion):
    dico = afficher_trajet(num_billet, cur) 
    choix = int(input("Quel trajet voulez vous supprimer ?"))
    query = "DELETE FROM Trajet WHERE id='%s' AND place='%s'" % (
        num_billet,
        dico[choix], #on récupère de cette manière le numéro du siège associé au choix du trajet à supprimer
    )
    cur.execute(query)
    connexion.commit()
    print("Le trajet a été supprimé, Appuyez sur entrée :)")
    input("")


def afficher_billet(connexion):

    num_billet = input("Quel est le numéro de votre billet ? ")
    choix = int(
        input(
            "Voulez vous : \n 1 - Afficher mes trajets \n 2 - Ajouter un trajet à mon billet \n 3 - Supprimer un trajet à mon billet  "
        )
    )
    cur = connexion.cursor()

    if choix == 1:
        afficher_trajet(num_billet, cur)

    if choix == 2:
        recherche_trajet(connexion)

    if choix == 3:
        delete_trajet(num_billet, cur, connexion)


#