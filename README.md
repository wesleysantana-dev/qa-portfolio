# Projeto de QA: validação de cadastro

Projeto de portfólio de **qualidade de software** feito em Python. Ele mostra como eu planejo, automatizo e documento testes.

**Autor:** Wesley Santana

## O que tem aqui
| Pasta / arquivo | Conteúdo |
|---|---|
| `src/validador.py` | Sistema sob teste: validação de senha, e-mail e CPF |
| `tests/` | Testes automatizados com pytest (partição de equivalência, valores limite, tipos inválidos) |
| `docs/plano_de_testes.md` | Estratégia, escopo, técnicas e critérios de aceite |
| `docs/casos_de_teste.md` | Casos de teste documentados |
| `docs/relatorio_de_bugs.md` | Bug real encontrado (BUG-001) e modelo de relatório |
| `.github/workflows/tests.yml` | Integração contínua: roda os testes a cada push e gera relatório HTML |

## Destaque: bug encontrado
Em teste exploratório, descobri que `validar_email("ana@exemplo.com\n")` retorna `True`. O caso está documentado em [`docs/relatorio_de_bugs.md`](docs/relatorio_de_bugs.md) e coberto por um teste `xfail`, que vai avisar quando o bug for corrigido.

## Como rodar
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    |  Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest
python -m pytest --html=report.html --self-contained-html   # relatório visual
```

## Metodologia
Organizei o trabalho em etapas: planejamento de testes, casos de teste, execução automatizada e registro de bugs.

## Uso de IA
Usei ferramentas de IA como apoio para estruturar o projeto. Estou estudando cada parte para entender o que foi feito e conseguir explicar.

## Próximos passos
- Corrigir o BUG-001 e remover o `xfail`
- Adicionar testes de API com `requests`
- Adicionar testes de interface com Playwright
