
import bot as corpus
import re
from aiml_read import readAiml

from models import *
#session =Create_session()


class Parole():
	def __init__(self):		
		self.session=Create_session()
		self.aiml = readAiml()


	def Response(self,message,user):
		# Aqui entram os modulos de inteligencia nas respostas
		self.user=user.decode('utf-8')

		self.resposta=self.aiml.response(message.decode('utf-8')).replace("{{user}}",self.user)
		if self.resposta is '':
			self.resposta=corpus.parole(message).replace("{{user}}",self.user)
		teste = Perguntas(message,self.resposta,"teste",self.user)	
		self.session.add(teste)
		self.session.commit()
		# termina 
		return re.sub('{{[^}}]+?}}', '', self.resposta)




