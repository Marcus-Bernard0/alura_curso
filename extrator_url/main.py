#url = 'https//bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
url = " "

#sanitização da url
url = url.replace(" ", "")
print(url)

if url =="":
    raise ValueError("A url está vazia")

indice_interrogacao = url.find('?')
print(indice_interrogacao)

#Separa a base
url_base = url[:indice_interrogacao]
print(url_base)


url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)

#Encontrando posição do paramêtro
parametro = ('quantidade')
parametro_busca =  url.find(parametro)
print(parametro_busca)

indice_valor = parametro_busca + len(parametro) + 1
indice_comercial = url.find('&', indice_valor)

#condição para extrair a moeda destino e origem e outros paramêtros
if indice_comercial == -1:
    valor = url[indice_valor:]
    print(valor)
else:
    valor = url[indice_valor:indice_comercial]
    print(valor)
