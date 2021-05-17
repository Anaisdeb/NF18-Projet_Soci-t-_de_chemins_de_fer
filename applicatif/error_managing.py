class DBContentException:
	"""Cette classe est dédiée à la gestion de toutes les erreurs qui sont dues à un défaut de contenu dans la BDD (pas assez de contenu e.g.)"""
	message = ''
	def __init__(self,m):
		self.message = m
	def getMessage():
		return self.message
