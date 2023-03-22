import re, requests
class Cep():
    def __init__(self, cep):
        self.__cep = cep
       # self.__cep = self.higieniza_cep(cep)
       # self.extrai_informacoes_cep()
        
    #Methods
    def busca_padrao_cep(self, cep):
        padrao = '[0-9]{5}(-)?[0-9]{3}' #o usuário pode inserir o CEP como 12345678 ou 12345-678
        encontra = re.search(padrao, cep)
        if not encontra:
            raise ValueError("Nenhum formato válido de CEP encontrado! Formatos válidos: 12345678 ou 12345-678.")
        else:
            cep = encontra.group()
            return cep
    
    def higieniza_cep(self, cep):
        cep = str(cep)
        cep = self.busca_padrao_cep(cep)
        cep = cep.replace('-','') #deixa o CEP no formato 12345678 
        return cep
    
    def __requisicao_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.__cep}/json/'
        req = requests.get(url)  #busca o cep em https://viacep.com.br/
        retorno_req = req.json() #atribui o json retornado a uma variável
        if self.__verifica_requisicao(retorno_req):
            return retorno_req
        else: 
            raise Exception('CEP inexistente')    

        
    def __verifica_requisicao(self, retorno_req):
        if 'erro' in retorno_req:
            return False #se encontra o chave "erro" a verificação retorna falso 
        else:
            return True #se não econtra erro, retorna verdadeiro

    def extrai_informacoes_cep(self):
        #separa os dados do json retornado pela via cep entre as propriedades da classe
        dados = self.__requisicao_via_cep()
        self.__dados = dados
        self.__cep_formatado = str(dados['cep'])
        self.__logradouro = str(dados['logradouro'])
        self.__complemento = str(dados['complemento'])
        self.__bairro = str(dados['bairro'])
        self.__localidade = str(dados['localidade'])
        self.__uf = str(dados['uf'])

    #Special methods
    def __str__(self):
        texto = f"CEP: {self.cep_formatado}"
        texto += f"\nLogradouro: {self.logradouro}"
        texto += f"\nComplemento: {self.complemento}"
        texto += f"\nBairro: {self.bairro}"
        texto += f"\nLocalidade: {self.localidade}"
        texto += f"\nUF: {self.uf}"
        return texto

    #Properties
    @property
    def dados(self):
        return self.__dados
    @dados.setter
    def dados(self, new):
        self.__dados = new
        
    @property
    def cep(self):
        return self.__cep
    
    @property
    def cep_formatado(self):
        return self.__cep_formatado
    
    @property
    def logradouro(self):
        return self.__logradouro
    @logradouro.setter
    def logradouro(self, new):
        self.__logradouro = new
    
    @property
    def complemento(self):
        return self.__complemento
    @complemento.setter
    def complemento(self, new):
        self.__complemento = new

    @property
    def bairro(self):
        return self.__bairro
    @bairro.setter
    def bairro(self, new):
        self.__bairro = new

    @property
    def localidade(self):
        return self.__localidade
    
    @property
    def uf(self):
        return self.__uf