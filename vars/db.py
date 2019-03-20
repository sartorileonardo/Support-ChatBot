
#Autor: Fabio Alberti
#Contact: fabiocax@gmail.com
import os
import sqlite3

DBNAME='db.sqlite'

#Exemplo de Uso
#
#import db
#
#rsp = db.Respostas()
#res=rsp.filters('teste')


class Connect(object):

    def __init__(self, db_name):
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


class Perguntas:

    tb_name = 'perguntas'

    def __init__(self):
        self.db = Connect(DBNAME)
        self.tb_name

    def filters(self,pesquisa=''):
        r = self.db.cursor.execute('SELECT * FROM '+self.tb_name+' WHERE  descricao LIKE  "%'+pesquisa+'%"' )
        return r

    def fechar_conexao(self):
        self.db.close_db()
        
class Respostas:

    tb_name = 'respostas'

    def __init__(self):
        self.db = Connect(DBNAME)
        self.tb_name

    def filters(self,pesquisa=''):
        r = self.db.cursor.execute('SELECT * FROM '+self.tb_name+' WHERE  descricao LIKE  "%'+pesquisa+'%"' )
        return r

    def fechar_conexao(self):
        self.db.close_db()

