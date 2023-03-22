import pytest
from Cep import Cep
class TestClass():
    def test_busca_padrao_cep_recebe_palvraaletaoria01001000_devolve_01001000(self):
        entrada = 'palavraaleatoria 01001000'
        esperado = '01001000'
        cep_teste = Cep(entrada)
        resultado = cep_teste.busca_padrao_cep(entrada)
        assert resultado == esperado