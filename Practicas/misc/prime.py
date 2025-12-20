"""
Módulo para identificar y mostrar números primos menores a 100.
"""

import math


def is_prime(number: int) -> bool:
    """
    Determina si un número es primo.

    Args:
        number (int): Número a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if number <= 1:
        return False

    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True


def main():
    """
    Lógica principal del programa.
    Imprime los números primos menores a 100.
    """
    for value in range(100):
        if is_prime(value):
            print(value, end=" ")
    print()


if __name__ == "__main__":
    main()
