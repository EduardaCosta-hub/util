from Cep import Cep
from Logradouro import Logradouro
cep3 = Cep('01001-000')
cep3.extrai_informacoes_cep()
print(cep3.cep_formatado)
print(cep3.localidade)

logradouro1 = Logradouro('01001-000')
print(logradouro1.__cep.cep_formatado)