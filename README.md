# Exercícios de Python — Faculdade (4º Período)

Coleção de exercícios práticos cobrindo verificação de primos, análise estatística de listas e depuração de código. Cada arquivo `.py` acompanha um documento `.md` com explicação técnica detalhada.

---

## Arquivos

| Arquivo | Descrição |
|---|---|
| `num_primos.py` | Verificação de número primo com Clean Code |
| `refatoracao.py` | Análise estatística de lista — versão refatorada |
| `debug.py` | Emissão de cupom fiscal com erros corrigidos |
| `explicacao_num_primo.md` | Explicação técnica de `num_primos.py` |
| `explicacao_refatoracao.md` | Análise do código original e da refatoração |
| `explicacao-debug.md` | Registro dos 4 erros encontrados e corrigidos em `debug.py` |

---

## num_primos.py

Verifica se um inteiro é primo usando divisão por tentativa otimizada.

**Complexidade:** O(√n) de tempo, O(1) de espaço.

**Estratégia:**
1. Descarta `n < 2` imediatamente.
2. Trata pares: apenas 2 é primo.
3. Testa divisores ímpares de 3 até `√n` (passo 2).

```python
from num_primos import is_prime

is_prime(2)   # True
is_prime(9)   # False  — 9 = 3 × 3
is_prime(13)  # True
```

> `math.isqrt` é usado no lugar de `int(n ** 0.5)` para evitar imprecisão de ponto flutuante.

---

## refatoracao.py

Calcula soma, média, maior e menor valor de uma lista numérica.

A versão original usava nomes de variáveis de uma letra (`c`, `l`, `t`, `mx`, `mn`) e dois loops onde um basta. A versão refatorada usa `sum()`, `max()` e `min()` nativos do Python e nomes descritivos.

```python
from refatoracao import calculate_list_statistics

numbers = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
total, average, maximum, minimum = calculate_list_statistics(numbers)
# total=346, average=34.6, maximum=89, minimum=2
```

---

## debug.py

Calcula o total de uma compra com 3 itens, aplicando imposto fixo de 10% e desconto opcional por cupom.

**Fórmula:** `total = subtotal + imposto (10%) − desconto do cupom`

O desconto é calculado sobre o subtotal (antes do imposto). A linha de desconto só aparece no recibo se o cliente informar um percentual maior que zero.

**Erros corrigidos (ver `explicacao-debug.md`):**

| # | Linha | Tipo | Descrição |
|---|---|---|---|
| 1 | 5 | `SyntaxError` | String sem aspas no `input()` |
| 2 | 22 | `TypeError` | `input()` sem conversão para `float` |
| 3 | 36 | Lógico | f-string sem prefixo `f` |
| 4 | 43 | `IndentationError` | `print` fora do bloco `if` |

---

## Como executar

Requer **Python 3.8+** (uso de `math.isqrt` e type hints com `list[float]`).

```bash
python num_primos.py
python refatoracao.py
python debug.py
```
