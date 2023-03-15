import requests
class Cep():
    def __init__(self, cep):
        self.__cep = cep
        self.__rua = ""
        self.__cidade = ""
        self.__estado = ""
        self.__pais = self.pais()
    #Methods
    def busca_padrao_cep(self):
        pass
        #o usuário pode inserir o CEP com a formatação ou não

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

    @staticmethod
    def pais(self):
        pais = "Brasil"
        return pais