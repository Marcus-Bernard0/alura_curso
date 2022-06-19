'''from abc import ABC
from collections.abc import MutableSequence
from numbers import Complex

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()
'''

from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    #resolvendo exercício, para executar len precisa do método abaixo adicionado.
    def __len__(self):
        return len(self.descricao)

    def __str__(self):
        return self.descricao

lista = MinhaListagem('Nova_lista')
print(lista)