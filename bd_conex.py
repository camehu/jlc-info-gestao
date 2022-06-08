import mysql.connector


class Conexao:
    def __init__(self, host="cc866a@us-cdbr-east-05.cleardb.net", user="bf52639806dbf1", pwd="a0cc866a", db="heroku_28ce16c0c087c86"):
        self.host = host
        self.user = user
        self.password = pwd
        self.database = db

    def conn(self):
        self.conex = mysql.connector.connect(host=self.host, user=self.user, db=self.database)
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
