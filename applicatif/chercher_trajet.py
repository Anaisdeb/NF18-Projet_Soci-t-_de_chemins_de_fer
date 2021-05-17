import error_managing
import reserver_billet
import datetime
from datetime import date

def recherche_trajet(connection):
	curs = connection.cursor()
	# 1 : on affiche la liste des villes disponibles.
	query = "SELECT DISTINCT ville FROM Gare"
	curs.execute(query)

	row = curs.fetchone()
	if(not row):
		raise DBContentException("Erreur lors de la lecture de la base de données : aucune ville ne peut vous être proposée.\n")

	print("Villes desservies :")
	print("+---------------+")
	while(row):
		print("- ",row[0])
		row = curs.fetchone()
	print("+---------------+")

	# 2 : choix des gares de départ et d'arrivée.
	vdep = input("Ville de départ ? ")
	query = f"SELECT nom FROM Gare WHERE ville='{vdep}'"
	curs.execute(query)
	res = curs.fetchall()

	while(not res):
		print("Aucune gare à proposer. Veuillez vérifier l'orthographe de la ville saisie.\n")
		vdep = input("Ville de départ ? ")
		query = f"SELECT nom FROM Gare WHERE ville='{vdep}'"
		curs.execute(query)
		res = curs.fetchall()

	print(f"Gares desservies à {vdep} :")
	print("+---------------+")
	for i in range(len(res)):
		print(i+1," - ",res[i][0])
	print("+---------------+")

	gdep = int(input("N° de la gare de départ ? "))-1

	while(not(gdep >= 0 and gdep <= i)):
		print("Erreur : numéro saisi hors de portée, veuillez recommencer.")
		gdep = int(input("N° de la gare de départ ? "))-1

	gdep = res[gdep][0].replace("'","''")

	varr = input("Ville d'arrivée ? ")
	query = f"SELECT nom FROM Gare WHERE ville='{varr}'"
	curs.execute(query)
	res = curs.fetchall()

	while(not res):
		print("Aucune gare à proposer. Veuillez vérifier l'orthographe de la ville saisie.\n")
		varr = input("Ville d'arrivée ? ")
		query = f"SELECT nom FROM Gare WHERE ville='{varr}'"
		curs.execute(query)
		res = curs.fetchall()

	print(f"Gares desservies à {varr} :")
	print("+---------------+")
	for i in range(len(res)):
		print(i+1," - ",res[i][0])
	print("+---------------+")

	garr = int(input("N° de la gare de départ ? "))-1

	while(not(garr >= 0 and garr <= i)):
		print("Erreur : numéro saisi hors de portée, veuillez recommencer.")
		garr = int(input("N° de la gare de départ ? "))-1

	garr = res[garr][0].replace("'","''")

	# 3 : choix des horaires, prix, min et max, durée.

	print("VOS PRÉFÉRENCES :")
	hmin = input("Au plus tôt (HH:MM) ? ").split(":")
	hmax = input("Au plus tard (HH:MM) ? ").split(":")
	date = input("Date (JJ/MM/YYYY) ? ")
	jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
	jour = datetime.datetime.strptime(date,'%d/%m/%Y').weekday()
	jour = jours[jour]
	duree = input("Durée maximale (en min, à saisir sans unité) ? ")

	hmin = hmin[0]+":"+hmin[1]+":00"
	hmax = hmax[0]+":"+hmax[1]+":00"
	date = date.split("/")
	date = date[0]+"-"+date[1]+"-"+date[2]

	# 4 : affichage des trajets correspondant aux critères.
		#Là on pleure sur les requêtes. On va d'abord se contenter des trajets directs.
		#R1 = Restriction(Arret,nom_gare = gdep,ville=vdep)
		#R2 = Restriction(Arret, nom_gare = garr, ville=varr)
		#R3 = Jointure(Horaire,R1 : rang_arret=R1.rang AND code_ligne = R1.code_ligne) : les horaires de tous les arrêts à la gare de départ.
		#R4 = Jointure(Horaire,rang_arret=R2.rang AND code_ligne = R2.code_ligne) : les horaires de tous les arrêts à la gare d'arrivée.
		#R5 = Jointure(R3,R4 : R3.train = R4.train AND R4.arrivee est le plus proche de R3.depart) : les couples d'horaires pour un train reliant directement départ et arrivée.

	print("TRAJETS DISPONIBLES :")
	query = f"""SELECT H1.depart, H2.arrivee, H1.train, H1.id, H2.id
	FROM Horaire H1
	JOIN Horaire H2 ON H1.train = H2.train
	JOIN Arret A1 ON A1.rang = H1.rang AND A1.code_ligne = H1.code_ligne
	JOIN Arret A2 ON A2.rang = H2.rang AND A2.code_ligne = H2.code_ligne
	JOIN RegulierC RC1 ON H1.regulierC = RC1.id
	JOIN RegulierC RC2 ON H2.regulierC = RC2.id
	LEFT OUTER JOIN ExceptionnelC_Horaire ECH ON ECH.id_horaire = H1.id OR ECH.id_horaire = H2.id
	LEFT OUTER JOIN ExceptionnelC EC ON ECH.exceptionnelC = EC.id
	WHERE A1.nom_gare = '{gdep}' AND A1.ville = '{vdep}' AND A2.nom_gare = '{garr}' AND A2.ville = '{varr}'
	AND H1.depart BETWEEN '{hmin}' AND '{hmax}'
	AND (RC1.{jour} = true AND RC2.{jour} = true) OR ('{date}' BETWEEN EC.jour_debut AND EC.jour_fin AND ECH.id_horaire IS NOT NULL)
	"""

	# Gestion de la date : transformer la date numérique en jour de la semaine, vérifier si un calendrier régulier correspond au jour demandé ET s'il n'a pas été annulé par un calendrier exceptionnel + si un calendrier exceptionnel y correspond.

	curs.execute(query)

	res = curs.fetchall()

	query = """SELECT Tr.placemax, COUNT (*)
	FROM Trajet T
	JOIN Horaire H ON T.horaire_depart = H.depart AND T.horaire_arrivee = H.arrivee
	JOIN Train Tr ON H.train = Tr.id
	GROUP BY Tr.id"""

	for i in range(len(res)):
		print("Trajet ",i+1," : ")
		print("Départ : ",res[i][0])
		print("Arrivée : ", res[i][1])
		print("Train : ",res[i][2])

	# 5 : indication du nombre de places dans le train proposé : nb de places du train - SELECT COUNT * FROM Trajet T JOIN Horaire H ON T.horaire_depart = H.depart AND T.horaire_arrivee = H.arrivee JOIN Train Tr ON H.train = Tr.id

	# 6 : proposition de réservation d'un billet.
	choix = input("Souhaitez-vous réserver un billet ? (y/n)")

	if(choix == 'y'):
		choix = int(input("Veuillez indiquer le n° du trajet à réserver."))-1
		
		while(choix <0 or choix>i+1):
			choix = int(input("Erreur : le trajet entré ne figure pas dans la liste proposée. Veuillez réessayer."))

		choix2 = input("Ajouter le trajet à un billet existant ? (y/n)")

		if(choix2 == "y"):
			idBillet = input("Veuillez entrer le numéro du billet auquel ajouter le trajet.")
			reserver_billet.ajouter_trajet(connection,idBillet,res[choix][3], res[choix][4], date)
		
		else:
			idBillet = reserver_billet.creer_billet(connection)
			print("Numéro du billet créé : ",idBillet)
			reserver_billet.ajouter_trajet(connection, idBillet, res[choix][3], res[choix][4], date)
			query = f"""UPDATE Billet
			SET gare_depart = '{gdep}', gare_arrivee = '{garr}', depart = '{res[choix][0]}', arrivee = '{res[choix][1]}'
			WHERE id = {idBillet}"""
			curs.execute(query)
			connection.commit()

