#!/usr/bin/python3
""" The N queens puzzles  challenge  """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, x=0, a=[], b=[], c=[]):
    """ find possible positions """
    if x < n:
        for y in range(n):
            if y not in a and x + y not in b and x - y not in c:
                yield from queens(n, x + 1, a + [y], b + [x + y], c + [x - y])
    else:
        yield a

def solve(n):
    """ solve """
    ad = []
    x = 0
    for solution in queens(n, 0):
        for s in solution:
            ad.append([i, s])
            x += 1
        print(k)
        ad = []
        x = 0
solve(n)
