# Explicação Técnica: Análise de Lista Numérica

## O que o código faz?

O código calcula **quatro estatísticas** de uma lista de números: soma total, média, maior valor e menor valor.

---

## Análise do Código Original

```python
def c(l):
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
    return t,m,mx,mn

x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
print("total:",a)
print("media:",b)
print("maior:",c2)
print("menor:",d)
```

---

## Passo a Passo

### 1. Cálculo da soma e média

```python
t=0
for i in range(len(l)):
    t=t+l[i]
m=t/len(l)
```

Percorre todos os índices da lista acumulando os valores em `t` (total).
A média `m` é calculada dividindo o total pelo número de elementos.

### 2. Busca do maior e menor valor

```python
mx=l[0]
mn=l[0]
for i in range(len(l)):
    if l[i]>mx:
        mx=l[i]
    if l[i]<mn:
        mn=l[i]
```

Inicializa `mx` (máximo) e `mn` (mínimo) com o primeiro elemento da lista.
A cada iteração, compara o elemento atual e atualiza se for maior ou menor que o valor guardado.

### 3. Retorno múltiplo

```python
return t,m,mx,mn
```

Python permite retornar múltiplos valores como uma tupla. Na chamada, o unpacking `a,b,c2,d=c(x)` distribui cada valor em uma variável separada.

---

## Saída do Programa

Para a lista `[23, 7, 45, 2, 67, 12, 89, 34, 56, 11]`:

| Estatística | Valor |
|---|---|
| Total | 346 |
| Média | 34.6 |
| Maior | 89 |
| Menor | 2 |

---

## Problemas de Legibilidade

O código funciona, mas viola princípios básicos de legibilidade:

| Problema | Exemplo | Impacto |
|---|---|---|
| Nome de função sem significado | `c` | Não comunica o que a função faz |
| Variáveis com nomes curtos demais | `l`, `t`, `m`, `mx`, `mn` | Difícil de entender sem executar |
| Dois loops onde um bastaria | `range(len(l))` repetido | Percorre a lista duas vezes desnecessariamente |
| Iteração por índice em vez de valor | `for i in range(len(l))` | Idioma não-pythônico |
