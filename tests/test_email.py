import pytest
from src.validador import validar_email


@pytest.mark.parametrize("email", [
    "ana@exemplo.com",
    "ana.silva@exemplo.com.br",
    "ana+teste@exemplo.com",
    "a_b-c@sub.dominio.org",
])
def test_emails_validos(email):
    assert validar_email(email) is True


@pytest.mark.parametrize("email", [
    "",
    "semarroba.com",
    "@exemplo.com",
    "ana@",
    "ana@exemplo",
    "ana@exemplo.c",
    "ana@@exemplo.com",
    "ana silva@exemplo.com",
    ".ana@exemplo.com",
    "ana.@exemplo.com",
    "ana..silva@exemplo.com",
    "ana@-exemplo.com",
    "ana@exemplo..com",
])
def test_emails_invalidos(email):
    assert validar_email(email) is False


def test_email_muito_longo():
    assert validar_email("a" * 250 + "@x.com") is False


@pytest.mark.parametrize("entrada", [None, 123, []])
def test_email_tipo_invalido(entrada):
    assert validar_email(entrada) is False


@pytest.mark.xfail(reason="BUG-001: e-mail com quebra de linha no final é aceito (ver docs/relatorio_de_bugs.md)", strict=True)
def test_email_com_quebra_de_linha_no_final_deve_ser_invalido():
    assert validar_email("ana@exemplo.com\n") is False
