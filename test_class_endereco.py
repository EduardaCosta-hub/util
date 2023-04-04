import pytest
import builtins
from pytest import MonkeyPatch
from Endereco import Endereco
class TestClass():
    def test_verifica_logradouro_recebe_cep_9370000_pede_logradouro_e_recebe_rua_de_teste(self):
        endereco_teste = Endereco(93700000)
        recebe = 'Rua de teste'
        esperado = 'Rua de teste'
        with MonkeyPatch.context() as monkeypatch:
            monkeypatch.setattr(builtins, 'input', lambda _: recebe)
            endereco_teste.verifica_logradouro()
            resultado = endereco_teste.logradouro
        assert resultado == esperado
    