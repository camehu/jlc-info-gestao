class Token:

    def itens(self, sub, name, chave, token):
        self.sub = sub
        self.name = name
        self.chave = chave
        self.token = token

    def setSub(self, sub):
        self.sub = sub

    def setName(self, name):
        self.name = name

    def setChave(self, nickname):
        self.chave = nickname

   # def setToken(self, token_login):
      #  self.token = token_login

    def getSub(self):
        return self.sub

    def getName(self):
        return self.name

    ''' def getToken(self):
        return self.token

    def criarToken(self):
        payload_data = {"sub": self.sub, "name": self.name, "chave": self.chave}

        chaveToken = jwt.encode( payload=payload_data, key='my-secret-super')
        return chaveToken

    def decode(self, cd_token):
        codigo = jwt.decode(cd_token, key="my-secret-super", algorithms=["HS256", ])

        return codigo '''