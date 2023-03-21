from Cep import Cep
class Endereco(Cep):
    def __init__(self, cep):
        super().__init__(cep)
        
    #Methods
    def verifica_campos_obrigatorios(self):
        if not(self.bairro):
            print("Bairro está vazio")