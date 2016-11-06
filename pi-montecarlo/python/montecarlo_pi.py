#! /usr/bin/env python3
import sys
from math import sqrt
from random import random

def calculate_pi(iterations):
    inside_circle = 0
    for _ in range (0, iterations):
        x = random()
        y = random()
        distance_to_center = sqrt(x*x + y*y)
        if distance_to_center <= 1.0:
            inside_circle += 1

    pi = 4 * inside_circle / iterations
    print("Pi: {}".format(pi))

def main():
    calculate_pi(int(sys.argv[1]))

if __name__ == '__main__':
    main()
