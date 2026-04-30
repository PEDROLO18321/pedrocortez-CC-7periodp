# Debug: Erros Encontrados em debug.py

Foram identificados **4 erros** no código:

---

## Erro 1 — String sem aspas no `input()` (linha 5)

```python
# ERRADO
item1 = float(input(Preço do item 1? ))

# CORRETO
item1 = float(input("Preço do item 1? "))
```

**Tipo:** `SyntaxError`
**Causa:** O texto passado para `input()` precisa ser uma string entre aspas. Sem elas, o Python tenta interpretar `Preço do item 1?` como código, e falha.

---

## Erro 2 — `input()` sem conversão para número (linha 22)

```python
# ERRADO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))

# CORRETO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
```

**Tipo:** `TypeError`
**Causa:** `input()` sempre retorna uma `string`. Nas linhas 23 e 42, o valor é usado em divisão (`/ 100`) e comparação (`> 0`), operações que exigem um número. Sem o `float()`, o programa quebra em tempo de execução.

---

## Erro 3 — f-string sem o prefixo `f` (linha 36)

```python
# ERRADO
print(" Item 2:        R$ {total_item2:.2f}")

# CORRETO
print(f" Item 2:        R$ {total_item2:.2f}")
```

**Tipo:** Erro lógico (sem exceção)
**Causa:** Sem o `f` antes das aspas, Python trata a string como texto literal. O valor de `total_item2` não é interpolado — a saída imprime `{total_item2:.2f}` literalmente.

---

## Erro 4 — Indentação ausente no bloco `if` (linha 43)

```python
# ERRADO
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

# CORRETO
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Tipo:** `IndentationError`
**Causa:** Em Python, o corpo de um `if` obrigatoriamente deve ser indentado. Sem a indentação, o interpretador não consegue associar o `print` ao bloco condicional.
