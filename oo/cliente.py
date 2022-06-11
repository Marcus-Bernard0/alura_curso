class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        #print(f"O nome do cliente é {self.nome}")

    #usado para subistituir o get
    @property
    def nome(self):
        print(f"O nome do cliente é {self.__nome.title()}")
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        print(f"O novo nome é {nome}")
    
        


        