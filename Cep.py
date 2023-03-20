import re, requests
class Cep():
    def __init__(self, cep):
        self.__cep = self.higieniza_cep(cep)
        self.__rua = ""
        self.__cidade = ""
        self.__estado = ""
        self.__pais = "Brasil"
        
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
        cep = self.busca_padrao_cep(cep)
        cep = cep.replace('-','') #deixa o CEP no formato 12345678 
        return cep
    
    def requisicao_via_cep(self):
        #busca o cep em https://viacep.com.br/
        url = f'https://viacep.com.br/ws/{self.__cep}/json/'
        req = requests.get(url)
        print(req.json())
        
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