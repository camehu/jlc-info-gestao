from urllib import request
from bd_conex import Conexao
from main import templates


class Login:
    def __init__(self, usuario, senha, token):
        self.user = usuario
        self.pwd = senha
        self.token = token

    def setUser(self, user_user):
        self.user = user_user

    def setPWD(self, pwd_login):
        self.pwd = pwd_login

    def setToken(self, token_login):
        self.token = token_login()

    def getToken(self):
        return self.token

    def validarusuario(self):
        self.userlog = self.user
        self.pwdlogo = self.pwd

    def inserirUser(self):
        pass

    def atualizaar(self):
        pass

    def deletarUser(self):

        pass













