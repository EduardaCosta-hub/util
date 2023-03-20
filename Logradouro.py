from Cep import Cep
class Logradouro(Cep):
    def __init__(self, cep):
        self.__cep = Cep(cep)
    
    #Methods
    def extrai_informacoes_cep(self):
        pass
    
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