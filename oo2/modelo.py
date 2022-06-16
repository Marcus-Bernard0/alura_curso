
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

    #criando método para polimorfismo
     #def imprime(self):
        #print(f'{self._nome} - {self._ano} - {self.duracao} - {self._likes}')

    def __str__(self):
        return f'{programa._nome} {programa.ano} {programa.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #inserindo superclasse para remover erros
        super().__init__(nome, ano)
        #self._nome = nome.title()
        #self.ano = ano
        self.duracao = duracao
        #self._likes = 0
        
   
    #defindo o método com __str__
    
    def __str__(self):
        return f'{self._nome} - {self._ano} - {self.duracao} - {self._likes}'

    
    


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        #self._nome = nome.title()
        #self.ano = ano
        self.temporada = temporada
        #self._likes = 0

    def __str__(self):
       return f'{self._nome} - {self._ano} - {self.temporada} - {self._likes}'


class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self.programa = programa
        
    def tamanho(self, tamanho):
        self.tamanho = len(tamanho)

       

#atribuindo dados
filme1 = Filme("homem aranha - de volta para a casa", 2022, 300)

#dando like no filme
filme1.dar_likes()
#print(f'{filme1._nome} - {filme1._ano} - {filme1._likes} likes')


serie1 = Serie("peak blinders", 2022, 6)

#usando set para mudar nome
serie1.nome = "Eu a patroa e as crianças"
serie1.dar_likes()
serie1.dar_likes()
#print(f'{serie1._nome} - {serie1.temporada} - {serie1.likes} likes')

print(26*'###')
#criando uma lista e armazenando variáveis filme e serie
filmes_e_series = [filme1, serie1]

#polimorfismo, listas do mesmo tipo. Ou seja, filme e serie contém compartilham variáveis como
#nome e likes
print("Filmes contam com duração em minutos e série temporadas.")
for programa in filmes_e_series:
    print(programa)

    #programa.imprime()
    #criando variável para imprimir especificade do filme ou serie (temporada, duracao)
    #foi criado um método na classe mãe para facilitar o polimorfismo, ou seja
    #quanto mais especificidade, mas if's seriam necessários

    '''
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
    print(f'{programa._nome} - D {detalhes} - {programa.likes}')'''

    