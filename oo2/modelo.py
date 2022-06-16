from mailbox import NotEmptyError
from xml.sax.handler import property_declaration_handler

#criando herança
#classe mãe
class Programa:
    def __init__(self, nome, ano ):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

#adicionado novo método para contagem e novos likes
    @property
    def likes(self):
        return self._likes 

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #inserindo superclasse para remover erros
        super().__init__(nome, ano)
        #self._nome = nome.title()
        #self.ano = ano
        self.duracao = duracao
        #self._likes = 0
        

    


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        #self._nome = nome.title()
        #self.ano = ano
        self.temporada = temporada
        #self._likes = 0

   

#atribuindo dados
filme1 = Filme("batman das trevas", 2022, 300)

# dando like no filme
filme1.dar_likes()
print(f'O nome é {filme1._nome} lançado em {filme1._ano}. {filme1._likes} pessoas gostaram')


serie1 = Serie("peak blinders", 2022, 6)
#usando set para mudar nome
serie1.nome = "Eu a patroa e as crianças"
print(f'O nome é {serie1._nome}, lançada {serie1.temporada} temporadas, com a última em {serie1._ano}')
