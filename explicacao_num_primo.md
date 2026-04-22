# Explicação Técnica: Verificação de Número Primo (Clean Code)

## O que é um número primo?

Um número primo é um número natural maior que 1 que possui exatamente dois divisores: **1** e **ele mesmo**.

Exemplos: 2, 3, 5, 7, 11, 13...

---

## Estrutura do Código

A lógica foi dividida em funções auxiliares privadas (prefixo `_`), cada uma com responsabilidade única e nome que descreve sua intenção.

### `is_prime(n)`

Função principal. Coordena as verificações na seguinte ordem:

1. Descarta números abaixo do mínimo (< 2)
2. Trata números pares: apenas 2 é primo
3. Verifica se existe divisor ímpar até `sqrt(n)`

### `_is_below_minimum(n)`

Retorna `True` se `n < 2`. Números menores que 2 não são primos por definição matemática.

### `_is_even(n)`

Retorna `True` se `n` é divisível por 2. Centraliza a verificação de paridade, evitando repetição de `n % 2 == 0`.

### `_has_odd_divisor(n)`

Itera de 3 até `math.isqrt(n)`, apenas em ímpares (passo 2). Retorna `True` se encontrar qualquer divisor, `False` caso contrário.

**Por que `math.isqrt` em vez de `int(n ** 0.5)`?**
`math.isqrt` calcula a raiz quadrada inteira de forma exata, sem imprecisão de ponto flutuante.

**Por que iterar apenas em ímpares (passo 2)?**
Pares já foram descartados em `_is_even`, então testar 4, 6, 8... seria redundante. O passo 2 reduz as iterações pela metade.

**Por que basta ir até `sqrt(n)`?**
Se `n` tem divisor `d > sqrt(n)`, então `n/d < sqrt(n)` também é divisor. Todo divisor composto aparece em par, então `sqrt(n)` é o limite seguro.

---

## Complexidade

| Métrica | Valor |
|---|---|
| Tempo | O(√n) |
| Espaço | O(1) |

---

## Exemplos de Uso

```python
from num_primos import is_prime

is_prime(1)   # False — menor que 2
is_prime(2)   # True  — único primo par
is_prime(9)   # False — 9 = 3 × 3
is_prime(13)  # True  — primo
is_prime(100) # False — 100 = 2 × 50
```
