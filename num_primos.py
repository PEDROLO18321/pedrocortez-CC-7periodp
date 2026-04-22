import math


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
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
