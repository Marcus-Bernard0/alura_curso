from mailbox import NotEmptyError


class Filme():
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

filme1 = Filme("batman", 2022, 300)
print(f'O nome é {filme1.nome} lançado em {filme1.ano}')
    

class Serie():
    def __init__(self, nome, ano,temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada

serie1 = Serie("Peak Blinders" , 2022, 6)
print(f'O nome é {serie1.nome}, lançada {serie1.temporada} temporadas, com a última em {serie1.ano}')
