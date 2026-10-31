import pytest
from src.validador import validar_cpf


@pytest.mark.parametrize("cpf", [
    "529.982.247-25",
    "52998224725",
    "111.444.777-35",
])
def test_cpfs_validos(cpf):
    assert validar_cpf(cpf) is True


@pytest.mark.parametrize("cpf", [
    "529.982.247-24",   # dígito verificador errado
    "111.111.111-11",   # todos iguais
    "000.000.000-00",
    "123.456.789-00",
    "529.982.247-2",    # curto
    "529.982.247-255",  # longo
    "abc.def.ghi-jk",   # letras
    "",
])
def test_cpfs_invalidos(cpf):
    assert validar_cpf(cpf) is False


@pytest.mark.parametrize("entrada", [None, 52998224725, ["52998224725"]])
def test_cpf_tipo_invalido(entrada):
    assert validar_cpf(entrada) is False
