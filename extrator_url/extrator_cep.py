endereco = "Rua Bororós 30, apartamento 312, Vila Togni, Poços de caldas, Mg, 37704350"

import re 

#Cep 5 digitos + [-] + 3 digitos ou Cep 8 dígitos


padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

#verificando se o padrão foi encontrado
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)

