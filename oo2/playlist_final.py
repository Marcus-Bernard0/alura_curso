#playlist final em construção, ver modelo

#criando classe mãe
class Programa:
    def __init__(self, nome, ano,):
        self._nome = nome.title() 
        self._ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes

    #criando método de likes para ser mudada de acordo com a execução da mesma.
    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome, novo_nome):
        self.nome = novo_nome()

class Filme(Programa):
    def __init__(self, nome, ano, duracao,):
        super().__init__(nome, ano)
        self.duracao = duracao
        
       
        
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.duracao = temporada
        


filme1 = Filme("velozes e furiosos - rio", 200, 2022)
#dando like no filme
filme1.dar_likes()
print(f'{filme1._nome} - likes: {filme1.likes}')

serie1 = Serie('the walking dead', 2000, 6)
       