import pytest
from Cep import Cep
class TestClass:
    def test_init_cep_recebe_palvra_aletaoria_01001000_devolve_01001000(self):
        entrada = 'palavra aleatoria 01001000'
        esperado = '01001000'
        cep_teste = Cep(entrada)
        resultado = cep_teste.cep
        assert resultado == esperado

    def test_init_cep_recebe_cep_01001000_formatado_devolve_cep_01001000_sem_formatacao(self):
        entrada = '01001-000'
        esperado = '01001000'
        cep_teste = Cep(entrada)
        resultado = cep_teste.cep
        assert resultado == esperado

    def test_init_cep_recebe_123456789_devolve_12345678(self):
        entrada = '123456789'
        esperado = '12345678'
        cep_teste = Cep(entrada)
        resultado = cep_teste.cep
        assert resultado == esperado

    def test_init_cep_recebe_1234abcd_devolve_erro(self):
        with pytest.raises(ValueError):
            entrada = '1234abcd'
            cep_teste = Cep(entrada)
    
    def test_extrai_informacao_cep_recebe_01001000_devolve_cep_formatado_01001000(self):
        entrada = '01001000'
        esperado = '01001-000'

        cep_teste = Cep(entrada)
        cep_teste.extrai_informacoes_cep()

        resultado_cep_formatado = cep_teste.cep_formatado

        assert resultado_cep_formatado == esperado

    def test_extrai_informacao_cep_recebe_01001000_devolve_logradouro_praca_da_se(self):
        entrada = '01001000'
        esperado = 'Praça da Sé'
        cep_teste = Cep(entrada)
        cep_teste.extrai_informacoes_cep()
        resultado = cep_teste.logradouro
        assert resultado == esperado

    def test_extrai_informacao_cep_recebe_01001000_devolve_complemento_lado_impar(self):
        entrada = '01001000'
        esperado = 'lado ímpar'
        cep_teste = Cep(entrada)
        cep_teste.extrai_informacoes_cep()
        resultado = cep_teste.complemento
        assert resultado == esperado

    def test_extrai_informacao_cep_recebe_01001000_devolve_bairro_se(self):
        entrada = '01001000'
        esperado = 'Sé'
        cep_teste = Cep(entrada)
        cep_teste.extrai_informacoes_cep()
        resultado = cep_teste.bairro
        assert resultado == esperado

    def test_extrai_informacao_cep_recebe_01001000_devolve_localidade_sao_paulo(self):
        entrada = '01001000'
        esperado = 'São Paulo'
        cep_teste = Cep(entrada)
        cep_teste.extrai_informacoes_cep()
        resultado = cep_teste.localidade
        assert resultado == esperado

    def test_extrai_informacao_cep_recebe_01001000_devolve_uf_sp(self):
        entrada = '01001000'
        esperado = 'SP'
        cep_teste = Cep(entrada)
        cep_teste.extrai_informacoes_cep()
        resultado = cep_teste.uf
        assert resultado == esperado

    def test_extrai_informacao_cep_recebe_12345678_devolve_erro(self):
        with pytest.raises(Exception):
            entrada = '12345678'
            cep_teste = Cep(entrada)
            cep_teste.extrai_informacoes_cep()
