# Plano de testes

## Objetivo
Garantir que os validadores de cadastro (senha, e-mail e CPF) aceitem entradas corretas e rejeitem entradas inválidas.

## Escopo
- **Dentro:** `validar_senha`, `validar_email`, `validar_cpf`.
- **Fora:** interface, banco de dados, desempenho.

## Técnicas aplicadas
- **Partição de equivalência:** classes válidas e inválidas (ex.: sem maiúscula, sem número).
- **Análise de valor limite:** senha com 7, 8, 64 e 65 caracteres.
- **Teste exploratório:** caracteres de controle, tipos errados (`None`, número, lista), entradas vazias.
- **Teste de regressão automatizado:** todos os casos rodam a cada `push` via GitHub Actions.

## Ferramentas
Python 3, pytest, pytest-html (relatório), GitHub Actions (CI), GitHub Projects (quadro Kanban).

## Critério de aceite
100% dos testes passando, exceto bugs conhecidos marcados como `xfail` e documentados em `docs/relatorio_de_bugs.md`.

## Riscos
O módulo valida só o formato do e-mail, não se a caixa de entrada existe.
