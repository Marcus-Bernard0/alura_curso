class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""  

    def valida_url(self):
        if not self.url: #if para verificar se a url está vazia
            raise ValueError("A url está vazia")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]  
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_comercial = self.url.find('&', indice_valor)

#condição para extrair a moeda destino e origem e outros paramêtros
        if indice_comercial == -1:
            valor = self.url[indice_valor:]
            
        else:
            valor = self.url[indice_valor:indice_comercial]
           

        return valor

extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

