import jwt

class Token:

    def itens(self, sub, name, chave):
        self.sub = sub
        self.name = name
        self.chave = chave

    def setSub(self, sub):
        self.sub = sub

    def setName(self, name):
        self.name = name

    def setChave(self, nickname):
        self.chave = nickname

    def getSub(self):
        return self.sub

    def getName(self):
        return self.name

    def criarToken(self):
        payload_data = {"sub": self.sub,
                        "name": self.name}

        chaveToken = jwt.encode(payload=payload_data,
                                key='my-secret-super')

        return chaveToken

    def decode(self):
        codigo = jwt.decode(self.criarToken(), key="my-secret-super", algorithms=["HS256", ])

        return codigo