import re, requests
class Cep():
    def __init__(self, cep):
        self.__cep = self.higieniza_cep(cep)
        
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
        #separa os dados do json retornado pela via cep entre os atributos da classe
        dados = self.__requisicao_via_cep()
        self.__cep_formatado = dados['cep']
        self.__logradouro = dados['logradouro']
        self.__complemento = dados['complemento']
        self.__bairro = dados['bairro']
        self.__localidade = dados['localidade']
        self.__uf = dados['uf']
        
    #Properties
    @property
    def cep(self):
        return self.__cep
    
    @property
    def cep_formatado(self):
        return self.__cep_formatado
    
    @property
    def logradouro(self):
        return self.__logradouro
    
    @property
    def complemento(self):
        return self.__complemento
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def localidade(self):
        return self.__localidade
    
    @property
    def uf(self):
        return self.__uf