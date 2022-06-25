endereco = "Rua Bororós 30, apartamento 312, Vila Togni, Poços de caldas, Mg, 37704-350"

import re 

#Cep 5 digitos + [-] + 3 digitos ou Cep 8 dígitos


padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

#verificando se o padrão foi encontrado
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)

