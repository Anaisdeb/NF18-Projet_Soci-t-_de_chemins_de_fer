class DBContentException:
	"""Cette classe est dédiée à la gestion de toutes les erreurs qui sont dues à un défaut de contenu dans la BDD (pas assez de contenu e.g.)"""
	message = ''
	def __init__(self,m):
		self.message = m
	def getMessage():
		return self.message

def erreurLigne(connexion):
	curs = connexion.cursor()

	query = "SELECT * FROM verifLigne"

	curs.execute(query)
	res = curs.fetchone()

	if(res[0]!=0):
		return True

	return False

def erreurTrain(connexion):
	curs = connexion.cursor()

	query = "SELECT * FROM verifTrain"

	curs.execute(query)
	res = curs.fetchone()

	if(res[0]!=0):
		return True

	return False