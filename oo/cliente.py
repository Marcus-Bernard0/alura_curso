class Cliente:
    def __init__(self, nome):
        self.nome = nome
        print(f"O nome do cliente é {self.nome}")

    #minha solução
    '''def get_nome(self):
        print(f"O nome do cliente é {self.nome.title()}")
        return self.nome''
'''
    #solução professor
    def get_nome(self):
        return self.nome.title()
        


        