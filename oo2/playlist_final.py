#playlist final em construção, ver modelo.

#criando classe mãe
from msilib.schema import Property
from pickletools import read_unicodestring1


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
        return self._nome
    
    @nome.setter
    def nome(self, nome, novo_nome):
        self.nome = novo_nome()

    def __str__(self):
        return f'{programas._nome} {programas.ano} {programas.likes}'

#criando playlist
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas
    @property
    def tamanho(self):
        return len(self._programas)

class Filme(Programa):
    def __init__(self, nome, ano, duracao,):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'{self._nome} lançada em {self._ano} {self.duracao} temporadas - {self._likes} likes'
       
        
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
    def __str__(self):
        return f'{self._nome} lançada em {self._ano} - {self.temporada} temporadas - {self._likes} likes'  


#inserindo dados no objeto
filme1 = Filme("velozes e furiosos - rio", 200, 2022)
filme2 = Filme("harry potter", 2009, 160)
filme3 = Filme("procurando nemo", 2009, 90)

#dando like no filme
filme1.dar_likes()

serie1 = Serie('the walking dead', 2000, 6)

filmeseSeries = [filme1, filme2, filme3, serie1]

playlistFimdeSemana = Playlist('fim de smana', filmeseSeries) 

mensagem = "Filmes contam com duração em minutos e série em temporadas. "
print(f'{mensagem} \n')

for programas in playlistFimdeSemana.listagem:
    print(programas)