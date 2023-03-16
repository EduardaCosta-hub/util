import requests
import re
class Cep():
    def __init__(self, cep):
        self.__cep = cep
        self.__rua = ""
        self.__cidade = ""
        self.__estado = ""
        self.__pais = "Brasil"
        self.encontra_padrao_cep()
    #Methods
    def encontra_padrao_cep(self):
        #o usuário pode inserir o CEP com a formatação ou não
        padrao = '[0-9]{5}(-)?[0-9]{3}'
        encontra = re.search(padrao, self.__cep)
        print(encontra.group())
        pass
        
    def higieniza_cep(self, cep):
        cep = str(cep)
        cep = cep.strip()
        return cep
        
    def requisicao_via_cep(self):
        pass
        #busca o cep em https://viacep.com.br/

    def valida_cep(self):
        pass
        #verifica se o formato de dado inserido é valido para um CEP        

    def formata_cep(self):
        pass
        #devolve o cep formatado

    def extrai_informacoes_cep(self):
        pass
        #separa os dados do json retornado pela via cep entre os atributos da classe
