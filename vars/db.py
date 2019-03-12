import os
import sqlite3

DBNAME='db.sqlite'

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


class Perguntas(object):

    tb_name = 'perguntas'

    def __init__(self):
        self.db = Connect(DBNAME)
        self.tb_name

    def filters(self):
        r = self.db.cursor.execute('SELECT * FROM '+self.tb_name)
        return r

    def fechar_conexao(self):
        self.db.close_db()
        
  class Respostas(object):

    tb_name = 'respostas'

    def __init__(self):
        self.db = Connect(DBNAME)
        self.tb_name

    def filters(self):
        r = self.db.cursor.execute('SELECT * FROM '+self.tb_name)
        return r

    def fechar_conexao(self):
        self.db.close_db()



if __name__ == '__main__':
    c = Perguntas().filters()
    for line in c:
        print(line)
