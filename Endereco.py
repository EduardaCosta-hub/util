from Cep import Cep
class Logradouro():
    def __init__(self, cep):
        self.__cep = Cep(cep)
    
    #Methods
    def extrai_informacoes_cep(self):
        self.__cep.extrai_informacoes_cep()
        
    #Properties
    @property
    def cep(self):
        return self.__cep