from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import datetime
from sqlalchemy.orm import sessionmaker
 
engine = create_engine('sqlite:///vars/chat.sqlite', echo=False)
Base = declarative_base()

class Perguntas(Base):

    __tablename__ = "perguntas"
 
    id = Column(Integer, primary_key=True)
    pergunta = Column(String)
    resposta = Column(String)
    descricao = Column(String)
    user = Column(String)
 
    def __init__(self, pergunta, resposta,descricao,user ):
        """"""
        self.pergunta = pergunta
        self.resposta = resposta
        self.descricao = descricao
        self.user = user







def Create_session():
	Session = sessionmaker(bind=engine)
	return Session()

 
###Inserir

# session =Create_session()
# teste = Perguntas("Python","egal","teste ","fabio")
# session.add(teste)
# session.commit()

##Pesquisar

# session =Create_session()
# for pergunta in session.query(Perguntas).order_by(Perguntas.id):
#     print (pergunta.pergunta, pergunta.resposta)

# Remover
#remove=session.query(Perguntas).filter_by(user='fabio').first()
#session.delete(remove)


#Objeto
# session.query(Perguntas).filter_by(user='fabio').first()