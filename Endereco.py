from Cep import Cep
class Endereco(Cep):
    def __init__(self, cep):
        super().__init__(cep)
        self.__numero = None
        self.extrai_informacoes_cep()
        self.verifica_campos_obrigatorios()

    #Methods
    def verifica_campos_obrigatorios(self):
        while not(self.logradouro):
            print("O CEP informado não possui logradouro associado.")
            logradouro = input("Por favor, informe o logradouro: ")
            self.logradouro = logradouro
        
        while not(self.numero):
            numero = int(input("Informe o número da sua casa/apartamento: "))
            self.numero = numero

        while not(self.bairro):
            print("O CEP informado não possui um bairro associado.")
            bairro = input("Por favor, informe um bairro: ")
            self.bairro = bairro

        if not(self.complemento):
            print("O CEP informado não possui complemento associada.")
            complemento = input("Informe um complemento (opcional): ")
            self.complemento = complemento

    #Special methods
    def __str__(self):
        texto = f"{self.logradouro}, {str(self.numero)}, {self.bairro} - {self.localidade}, {self.uf}"
        if self.complemento:
            texto += f"\nComplemento: {self.complemento}"
        return texto

    #Property
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, new):
        self.__numero = new