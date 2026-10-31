# Relatório de bugs

## BUG-001 — E-mail com quebra de linha no final é aceito como válido

| Campo | Detalhe |
|---|---|
| **Módulo** | `src/validador.py` → `validar_email` |
| **Severidade** | Média |
| **Prioridade** | Média |
| **Status** | Aberto (coberto por teste `xfail` em `tests/test_email.py`) |

**Passos para reproduzir**
1. Abrir um terminal Python na raiz do projeto.
2. Executar: `from src.validador import validar_email`
3. Executar: `validar_email("ana@exemplo.com\n")`

**Resultado esperado:** `False` (o `\n` não faz parte de um e-mail válido).

**Resultado obtido:** `True`.

**Causa provável:** o `$` da expressão regular aceita uma quebra de linha logo antes do fim do texto. Usar `re.fullmatch` (como já é feito em `validar_cpf`) ou `\Z` resolveria.

**Impacto:** dados sujos podem entrar no cadastro (por exemplo, vindos de um campo copiado e colado), causando falha de envio de e-mail mais adiante.

**Como foi encontrado:** teste exploratório de caracteres de controle nas entradas, depois transformado em teste automatizado.

---

## Modelo para novos bugs

```
## BUG-00X — Título curto e objetivo
Módulo / tela:
Severidade / Prioridade:
Ambiente:
Passos para reproduzir:
Resultado esperado:
Resultado obtido:
Evidência (print, log):
Status:
```
