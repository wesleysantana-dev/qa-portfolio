# Casos de teste (resumo)

| ID | Função | Entrada | Resultado esperado |
|---|---|---|---|
| CT-01 | validar_senha | `Abcdef1!` | válida |
| CT-02 | validar_senha | `Ab1!` | inválida: mínimo de caracteres |
| CT-03 | validar_senha | sem maiúscula / minúscula / número / especial | inválida, com a mensagem correspondente |
| CT-04 | validar_senha | 7, 8, 64 e 65 caracteres | inválida, válida, válida, inválida |
| CT-05 | validar_senha | `None`, número, lista | inválida |
| CT-06 | validar_email | `ana@exemplo.com`, `ana+teste@exemplo.com` | válido |
| CT-07 | validar_email | sem `@`, `@@`, sem domínio, ponto no início/fim, `..` | inválido |
| CT-08 | validar_email | mais de 254 caracteres | inválido |
| CT-09 | validar_email | `ana@exemplo.com\n` | inválido (**falha: BUG-001**) |
| CT-10 | validar_cpf | `529.982.247-25` com e sem pontuação | válido |
| CT-11 | validar_cpf | dígito errado, todos iguais, curto, longo, letras | inválido |
| CT-12 | validar_cpf | `None`, número, lista | inválido |

Os testes automatizados estão na pasta `tests/`.
