#! /usr/bin/env python3
"""Calculates π (Pi) using Monte Carlo approximation

Usage:

    python3 montecarlo_pi <iterations>
"""
import sys
from math import sqrt
from random import random

def calculate_pi(iterations):
    """Calculates π using Monte Carlo approximation. Takes random points within
    a unit square and checks whether they fall inside or outside a unit quarter
    circle circumscribed within the square.

    Args:
        iterations: The number of iterations of the algorithm. The greater the
        number, the more accurate the estimate of π.

    Returns:
        An estimate for the value of π.
    """
    inside_circle = 0
    for _ in range (0, iterations):
        x = random()
        y = random()
        distance_to_center = sqrt(x*x + y*y)
        if distance_to_center <= 1.0:
            inside_circle += 1

    pi = 4 * inside_circle / iterations
    return pi

def main():
    pi = calculate_pi(int(sys.argv[1]))
    print("Pi: {}".format(pi))

if __name__ == '__main__':
    main()
