"""
Explicacao Tecnica: Verificacao de Numero Primo (Clean Code)

O que e um numero primo?
    Um numero primo e um numero natural maior que 1 que possui exatamente
    dois divisores: 1 e ele mesmo.
    Exemplos: 2, 3, 5, 7, 11, 13...
"""

# ============================================================
# ANALISE DAS FUNCOES
# ============================================================

# A logica foi dividida em funcoes auxiliares privadas (prefixo _),
# cada uma com responsabilidade unica e nome que descreve sua intencao.

# --- is_prime(n) ---
#
# Funcao principal. Coordena as verificacoes na seguinte ordem:
#   1. Descarta numeros abaixo do minimo (< 2)
#   2. Trata numeros pares: apenas 2 e primo
#   3. Verifica se existe divisor impar ate sqrt(n)

# --- _is_below_minimum(n) ---
#
# Retorna True se n < 2.
# Numeros menores que 2 nao sao primos por definicao matematica.

# --- _is_even(n) ---
#
# Retorna True se n e divisivel por 2.
# Centraliza a verificacao de paridade, evitando repeticao de n % 2 == 0.

# --- _has_odd_divisor(n) ---
#
# Itera de 3 ate math.isqrt(n), apenas em impares (passo 2).
# Retorna True se encontrar qualquer divisor, False caso contrario.
#
# Por que math.isqrt em vez de int(n ** 0.5)?
#   math.isqrt calcula a raiz quadrada inteira de forma exata, sem
#   imprecisao de ponto flutuante. Ex: int(9999999**0.5) pode retornar
#   3162 ao inves de 3162, enquanto math.isqrt garante o valor correto.
#
# Por que iterar apenas em impares (passo 2)?
#   Pares ja foram descartados em _is_even, entao testar 4, 6, 8...
#   seria redundante. O passo 2 reduz as iteracoes pela metade.
#
# Por que basta ir ate sqrt(n)?
#   Se n tem divisor d > sqrt(n), entao n/d < sqrt(n) tambem e divisor.
#   Todo divisor composto aparece em par, entao sqrt(n) e o limite seguro.

# ============================================================
# COMPLEXIDADE
# ============================================================

# Tempo : O(sqrt(n))  -- muito melhor que a abordagem ingenua O(n)
# Espaco: O(1)        -- nenhuma estrutura de dados extra

# ============================================================
# EXEMPLOS DE USO
# ============================================================

from num_primos import is_prime

exemplos = [1, 2, 9, 13, 100]
for n in exemplos:
    print(f"is_prime({n}) => {is_prime(n)}")

# Saida esperada:
# is_prime(1)   => False  (menor que 2)
# is_prime(2)   => True   (unico primo par)
# is_prime(9)   => False  (9 = 3 x 3)
# is_prime(13)  => True   (primo)
# is_prime(100) => False  (100 = 2 x 50)
