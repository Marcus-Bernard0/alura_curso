import time
endereco = input("Digite seu endereço aqui com CEP: ")

import re 

#Cep 5 digitos + [-] + 3 digitos ou Cep 8 dígitos


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

#verificando se o padrão foi encontrado
busca = padrao.search(endereco)
time.sleep(2)
if busca:
    cep = busca.group()
    print(f'O CEP do cliente é: {cep}')
elif not busca:
    print('O endereço não tem CEP.')

