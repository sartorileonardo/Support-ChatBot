
import bot

class Parole():
	def __init__(self):		
		pass

	def Response(self,message,user):
		# Aqui entram os modulos de inteligencia nas respostas 
		self.user=user
		self.message=bot.parole(message)	

		# termina 
		return self.message


