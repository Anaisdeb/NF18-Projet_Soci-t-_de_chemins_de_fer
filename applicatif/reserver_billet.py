import random
import error_managing

def creer_billet(connection):
	cursor = connection.cursor()
	query = "INSERT INTO Billet (gare_depart, depart, gare_arrivee, arrivee, assurance, prix) VALUES ('N/A', '00:00:00', 'N/A', '00:00:00', false, 0) RETURNING id"
	cursor.execute(query)
	#Récupérer l'id du billet créé
	res = cursor.fetchone()

	connection.commit()

	# Demander si l'utilisateur est déjà enregistré, enregistrer le moyen de paiement, etc. avant de retourner l'id du billet créé.
	choix = input("Souhaitez-vous souscrire une assurance sur ce billet ? (y/n)")
	if(choix == "y"):
		cursor.execute(f"UPDATE Billet SET assurance = true WHERE id = {res[0]}")
		connection.commit()
	return res[0]

def ajouter_trajet(connection, idBillet, hDepart, hArrivee, date):
	cursor = connection.cursor()
	# 1 : déterminer la place.
		# 1.1 récupérer les places dans tous les trajets existant dans ce train entre les horaires de début et de fin
	query = f"""SELECT T.place
	FROM Trajet T
	JOIN Horaire HD ON T.horaire_depart = HD.id
	JOIN Horaire HA ON T.horaire_arrivee = HA.id
	WHERE HD.id = '{hDepart}' AND HA.id = '{hArrivee}'
	"""

	cursor.execute(query)
	res = cursor.fetchall()
	occupied = []
	for i in range(len(res)):
		occupied.append(res[i][0])

		# 1.2 choisir une place au pif entre 1 et le nombre de places dispo, privé de n° de places déjà attribués.
	query = f"""SELECT T.placemax
	FROM Train T
	JOIN Horaire H ON H.train = T.num
	WHERE H.id = {hDepart}
	"""
	cursor.execute(query)
	row = cursor.fetchone()
	
	places = list(range(row[0]))
	places = [i+1 for i in places]
	places = list(set(places)-set(occupied))

	newPlace = random.choice(places)
	# 2  : ajouter le trajet.

	query = f"INSERT INTO Trajet VALUES({idBillet}, {newPlace}, {hDepart}, {hArrivee})"
	cursor.execute(query)

	# 3 : proposer les hôtels, taxis, transports à proximité.

	query = f"""SELECT Ho.adresse, Ho.nom, Ho.nb_etoiles
	FROM Horaire H
	JOIN Arret A ON H.rang = A.rang AND H.code_ligne = A.code_ligne
	JOIN Hotel Ho ON Ho.ville = A.ville
	WHERE H.id = {hArrivee}
	"""

	print("-- Hôtels à proximité de la gare d'arrivée --")

	cursor.execute(query)
	row = cursor.fetchone()

	while(row):
		print(f"- Hôtel {row[1]}, {row[0]}, {row[2]} étoiles")
		row = cursor.fetchone()

	print("-- Taxis à proximité de la gare d'arrivée --")

	query = f"""SELECT T.numero, T.marque, T.tarif, T.tel
	FROM Horaire H
	JOIN Arret A ON H.rang = A.rang AND H.code_ligne = A.code_ligne
	JOIN Taxi T ON T.ville = A.ville
	WHERE H.id = {hArrivee}
	"""

	cursor.execute(query)
	row = cursor.fetchone()

	while(row):
		print(f"- Taxi n°{row[0]}, marque {row[1]}, tarif : {row[2]}, téléphone : {row[3]}")
		row = cursor.fetchone()

	print("-- Transports à proximité de la gare d'arrivée  --")
	query = f"""SELECT T.numero, T.compagnie, T.tarif, T.type
	FROM Horaire H
	JOIN Arret A ON H.rang = A.rang AND H.code_ligne = A.code_ligne
	JOIN Transport T ON T.ville = A.ville
	WHERE H.id = {hArrivee}
	"""

	cursor.execute(query)
	row = cursor.fetchone()

	while(row):
		print(f"- {row[0]} : {row[3]}, compagnie {row[1]}, tarif : {row[2]}")
		row = cursor.fetchone()

	if(error_managing.erreurTrain(connection)):
		print("Erreur d'insertion : les horaires de départ et d'arrivée ne sont pas liés au même train.")
		connection.rollback()
	else:
		connection.commit()