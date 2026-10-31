"""Sistema sob teste: validadores de cadastro (senha, e-mail e CPF).

Módulo pequeno e propositalmente simples, usado como alvo do projeto de QA.
"""
import re

SENHA_MIN = 8
SENHA_MAX = 64
ESPECIAIS = "!@#$%^&*()-_=+[]{};:,.<>?/\\|~"


def validar_senha(senha):
    """Retorna (valida, lista_de_erros)."""
    erros = []
    if not isinstance(senha, str):
        return False, ["A senha deve ser um texto."]
    if len(senha) < SENHA_MIN:
        erros.append(f"Mínimo de {SENHA_MIN} caracteres.")
    if len(senha) > SENHA_MAX:
        erros.append(f"Máximo de {SENHA_MAX} caracteres.")
    if not any(c.isupper() for c in senha):
        erros.append("Precisa de uma letra maiúscula.")
    if not any(c.islower() for c in senha):
        erros.append("Precisa de uma letra minúscula.")
    if not any(c.isdigit() for c in senha):
        erros.append("Precisa de um número.")
    if not any(c in ESPECIAIS for c in senha):
        erros.append("Precisa de um caractere especial.")
    if any(c.isspace() for c in senha):
        erros.append("Não pode conter espaços.")
    return len(erros) == 0, erros


_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$")


def validar_email(email):
    """Retorna True se o e-mail tem formato válido."""
    if not isinstance(email, str) or len(email) > 254:
        return False
    if not _EMAIL_RE.match(email):
        return False
    local, dominio = email.rsplit("@", 1)
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False
    if dominio.startswith("-") or ".-" in dominio or "-." in dominio:
        return False
    return True


def validar_cpf(cpf):
    """Retorna True se o CPF é válido (com ou sem pontuação)."""
    if not isinstance(cpf, str):
        return False
    if not re.fullmatch(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", cpf):
        return False
    digitos = [int(c) for c in cpf if c.isdigit()]
    if len(set(digitos)) == 1:
        return False
    for tamanho in (9, 10):
        soma = sum(d * p for d, p in zip(digitos[:tamanho], range(tamanho + 1, 1, -1)))
        resto = (soma * 10) % 11
        if resto == 10:
            resto = 0
        if resto != digitos[tamanho]:
            return False
    return True
