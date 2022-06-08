import mysql.connector


class Conexao:
    def __init__(self, user="bf52639806dbf1", password="a0cc866a", host="us-cdbr-east-05.cleardb.net", db='heroku_28ce16c0c087c86'):
        self.user = user
        self.password = password
        self.host = host
        self.database = db

    def conn(self):
        self.conex = mysql.connector.connect(user=self.user , senha=self.password, host=self.host, db=self.database)
        self.cur = self.conex.cursor()

    def logout(self):
        self.conex.close()

    def inserir(self, sql):
        self.conn()
        self.cur.execute(sql)
        self.conex.commit()
        self.logout()

    def pesquisar(self, sql):
        self.conn()
        self.cur.execute(sql)
        myresult = self.cur.fetchall()
        self.logout()
        return myresult
