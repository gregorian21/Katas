#! /usr/bin/env python3
"""Calculates Primes upto a certain maximum number using the Sieve of Eratosthenes

    Usage:
        python3 sieve.py <max_number>
"""
import sys
import math

def calculate_primes(max_number):
    """Calculates Primes uptil a certain maximum number using the Sieve of
    Eratosthenes.

    Args:
        The upper bound for the calculation of primes. The number should be greater
        than 1.

    Returns:
        Prime numbers uptil the maximum number provided.
    """
    if max_number < 2:
        print("Please provide a number greater than 1")
        sys.exit()

    numbers = [True] * (max_number+1)
    numbers[0] = False
    numbers[1] = False

    hard_stop = math.ceil(math.sqrt(max_number))

    for i in range(2, hard_stop):
        if not numbers[i]:
            continue
        _sieve(i, numbers)

    primes = []
    for i in range (2, max_number):
        if numbers[i]:
            primes.append(i)

    return primes

def _sieve(i, numbers):
    multiple = 2
    while (i* multiple) < len(numbers):
        numbers[i*multiple] = False
        multiple += 1
    return numbers

def main(max_number):
    primes = calculate_primes(max_number)
    print(primes)

if __name__ == "__main__":
    main(int(sys.argv[1]))
