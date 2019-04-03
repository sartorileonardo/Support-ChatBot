
import bot as corpus
#from db import *
#session =Create_session()

class Parole():
	def __init__(self):		
		pass

	def Response(self,message,user):
		# Aqui entram os modulos de inteligencia nas respostas

		self.user=user.decode('utf-8')
		self.resposta=corpus.parole(message).replace("{{user}}",self.user)	
		# termina 
		return self.resposta




