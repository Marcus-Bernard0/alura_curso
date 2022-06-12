#boa prática cololocar letras maisculas
class Conta:
#self tem o mesmo valor que rodar somente a variavel, mesma referência
    def __init__(self, numero, titular, saldo, limite):
        #print(f"Construindo objeto... {self}")
        print(f"Construindo objeto... {self}")
        self.__numero = numero #__ deixando a variavel privada
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.__titular} é {self.__saldo} ")
    
    def depositar(self, valor):
        self.__saldo += valor
    
    #elaborando um método a parte para valor a sacar
    #resolução de aula
    '''def __valor_permtido (self, valor_a_sacar):
        valor_disponivel = (self.__saldo) 
        print(f"Saque de {valor_a_sacar} realizado com sucesso")
        return valor_a_sacar <= valor_disponivel'''
    
    def __valor_permtido (self, valor_a_sacar):
        valor_disponivel = (self.__saldo)
        if valor_disponivel <= (self.__saldo):
            print(f"Saque de {valor_a_sacar} realizado com sucesso")
        else: 
            print(f"Valor indisponivel para saque. Valor permitido de {self.__saldo}")
            
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if(self.__valor_permtido(valor)):
            self.__saldo -= valor
       
    
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    #get usado para retornar
    '''def get_saldo (self):
        print(f"O saldo do titular {self.__titular} é {self.__saldo}")
        return self.__saldo'''
   
    @property
    def saldo (self):
        print(f"O saldo do titular {self.__titular} é {self.__saldo}")
        return self.__saldo

    def get_titular (self):
        print(f"Essa conta é titular de {self.__titular}")
        return self.__titular

    @property
    def limite (self):
        print(f"Seu limite é {self.__limite}")
        return self.__limite

    '''def get_limite (self):
        print(f"Seu limite é {self.__limite}")
        return self.__limite'''

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print(f"Seu novo limite é {self.__limite}")
    
    #set usado para receber um novo valor
    '''def set_limite(self, limite):
        self.__limite = limite
        print(f"Seu novo limite é {self.__limite}")'''

    def set_titular(self, titular):
        self.__titular = titular
        print(f"O titular foi alterado com sucesso. O novo titular é {self.__titular}")

    @staticmethod
    def codigo_banco():
        return '008'