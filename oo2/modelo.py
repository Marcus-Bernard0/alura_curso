from mailbox import NotEmptyError


class Filme():
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    # adicionado novo método para contagem e novos likes
    def dar_likes(self):
        self.likes += 1


class Serie():
    def __init__(self, nome, ano, temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada
        self.likes = 0

    def dar_likes(self):
        self.likes += 1


filme1 = Filme("batman", 2022, 300)

# dando like no filme

print(
    f'O nome é {filme1.nome} lançado em {filme1.ano}. {filme1.likes} pessoas gostaram')

serie1 = Serie("Peak Blinders", 2022, 6)
print(
    f'O nome é {serie1.nome}, lançada {serie1.temporada} temporadas, com a última em {serie1.ano}')
