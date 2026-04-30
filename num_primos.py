import math


def is_prime(n: int) -> bool:
    """Verifica se um número inteiro é primo.

    Args:
        n: O número inteiro a ser verificado.

    Returns:
        True se ``n`` for primo, False caso contrário.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if _is_below_minimum(n):
        return False
    if _is_even(n):
        return n == 2
    return not _has_odd_divisor(n)


def _is_below_minimum(n: int) -> bool:
    return n < 2


def _is_even(n: int) -> bool:
    return n % 2 == 0


def _has_odd_divisor(n: int) -> bool:
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return True
    return False
