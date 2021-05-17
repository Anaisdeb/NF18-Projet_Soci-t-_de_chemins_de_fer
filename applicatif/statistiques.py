def choix(connection):
	print("Statistiques accessibles :")
	print("1. Taux de remplissage des trains")
	print("2. Gares les plus fréquentées")
	print("3. Lignes les plus empruntées")

	ch = int(input("Veuillez faire votre choix : "))

	if ch == 1:
		taux_remplissage(connection)
	elif ch == 2:
		frequentation_gares(connection)
	elif ch == 3:
		lignes_empruntees(connection)
	elif ch == 4:
		voyageurs_moyens(connection)

def taux_remplissage(connection):
	curs = connection.cursor()

	# 1 : Récupération des num de tous les trains
	query = "SELECT num,placemax FROM Train"
	curs.execute(query)
	row = curs.fetchone()

	nums = []
	freq = []

	while(row):
		nums.append([row[0],row[1]])
		row = curs.fetchone()

	for train in nums:
		print(train[0])
		query = f"""SELECT COUNT(*)
		FROM Trajet T
		JOIN Horaire H ON H.id = T.horaire_depart
		JOIN Train Tr ON Tr.num = H.train
		WHERE Tr.num = {train[0]}
		"""
		curs.execute(query)
		res = curs.fetchone()

		print(res[0])

		freq.append(res[0]/train[1])

	taux = sum(freq)/len(freq)
	print(taux*100)

	print("Le taux d'occupation des trains est de : %.3f%%." %(taux*100))

def frequentation_gares(connection):
	curs = connection.cursor()

	query = """SELECT A.nom_gare, A.ville, COUNT (*)
	FROM Trajet T
	JOIN Horaire H ON T.horaire_depart = H.id OR T.horaire_arrivee = H.id
	JOIN Arret A ON A.rang = H.rang AND A.code_ligne = H.code_ligne
	GROUP BY A.nom_gare, A.ville
	"""
	curs.execute(query)

	res = curs.fetchall()

	freq = []

	for gare in res:
		freq.append(gare[2])

	m = max(freq)

	maxfreq = []

	for gare in res:
		if(gare[2]==m):
			maxfreq.append([gare[0],gare[1]])

	print("Gare(s) la (les) plus fréquentée(s) :")
	for gare in maxfreq:
		print("- ",gare[0]+" : "+gare[1])

def lignes_empruntees(connection):
	curs = connection.cursor()

	query = """SELECT H.code_ligne, COUNT (*)
	FROM Horaire H
	JOIN Trajet T ON T.horaire_depart = H.id OR T.horaire_arrivee = H.id
	GROUP BY H.code_ligne
	"""

	curs.execute(query)

	res = curs.fetchall()

	freq = []

	for ligne in res:
		freq.append(ligne[1])
	
	m = max(freq)

	maxfreq = []

	for ligne in res:
		if(ligne[1]==m):
			maxfreq.append([ligne[0],ligne[1]])

	print("Ligne(s) la (les) plus fréquentée(s) :")
	for ligne in maxfreq:
		print("- Ligne n°"+str(ligne[0]))