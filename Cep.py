import requests
import re
class Cep():
    def __init__(self, cep):
        self.__cep = self.busca_padrao_cep(cep)
        self.__rua = ""
        self.__cidade = ""
        self.__estado = ""
        self.__pais = "Brasil"
    #Methods
    def busca_padrao_cep(self, cep):
        #o usuário pode inserir o CEP com a formatação ou não
        padrao = '[0-9]{5}(-)?[0-9]{3}'
        encontra = re.search(padrao, cep)
        if not encontra:
            raise ValueError("Nenhum formato válido de CEP encontrado! Formatos válidos: 12345678 ou 12345-678.")
        else:
            cep = encontra.group()
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

    #Properties
    @property
    def cep(self):
        return self.__cep