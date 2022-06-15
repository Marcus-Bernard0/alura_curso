from mailbox import NotEmptyError
from xml.sax.handler import property_declaration_handler


class Filme():
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    # adicionado novo método para contagem e novos likes
    @property
    def likes(self):
        return self.__likes 

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie():
    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.__likes = 0

    def dar_likes(self):
        self.likes += 1

    @property 
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
       self.__nome = novo_nome.title()


filme1 = Filme("batman das trevas", 2022, 300)

# dando like no filme
filme1.dar_likes()
print(
    f'O nome é {filme1.nome} lançado em {filme1.ano}. {filme1.likes} pessoas gostaram')

serie1 = Serie("peak blinders", 2022, 6)
print(
    f'O nome é {serie1.nome}, lançada {serie1.temporada} temporadas, com a última em {serie1.ano}')
