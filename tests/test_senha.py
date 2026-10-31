import pytest
from src.validador import validar_senha


def test_senha_valida():
    ok, erros = validar_senha("Abcdef1!")
    assert ok is True
    assert erros == []


@pytest.mark.parametrize("senha, trecho_erro", [
    ("Ab1!", "Mínimo"),                 # curta demais
    ("abcdefg1!", "maiúscula"),         # sem maiúscula
    ("ABCDEFG1!", "minúscula"),         # sem minúscula
    ("Abcdefgh!", "número"),            # sem número
    ("Abcdefg12", "especial"),          # sem especial
    ("Abc def1!", "espaços"),           # com espaço
])
def test_senha_invalida_retorna_erro_correto(senha, trecho_erro):
    ok, erros = validar_senha(senha)
    assert ok is False
    assert any(trecho_erro in e for e in erros)


@pytest.mark.parametrize("tamanho, esperado", [
    (7, False),   # limite inferior - 1
    (8, True),    # limite inferior
    (64, True),   # limite superior
    (65, False),  # limite superior + 1
])
def test_valores_limite_de_tamanho(tamanho, esperado):
    senha = "Aa1!" + "x" * (tamanho - 4)
    ok, _ = validar_senha(senha)
    assert ok is esperado


@pytest.mark.parametrize("entrada", [None, 12345678, ["Abcdef1!"]])
def test_tipos_invalidos(entrada):
    ok, erros = validar_senha(entrada)
    assert ok is False
    assert erros


def test_senha_vazia_acumula_varios_erros():
    ok, erros = validar_senha("")
    assert ok is False
    assert len(erros) >= 4
