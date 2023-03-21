from Cep import Cep
from Endereco import Endereco
cep3 = Cep('01001-000')
cep3.extrai_informacoes_cep()
print(cep3.cep_formatado)
print(cep3.localidade)

logradouro1 = Endereco('93700000')
print(logradouro1)