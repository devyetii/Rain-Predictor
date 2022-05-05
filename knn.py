#!/usr/bin/env python3

import heapq
import os
import sys
from typing import List

from constants import WEIGHT_COUNT


def mapper(x: List[float]):
    for line in sys.stdin:
        record = [float(pi) for pi in line.strip().split(',')]
        c = record[-1]
        p = record[:-1]
        p.insert(0, 1.0)

        d = sum([x[i]*x[i] - p[i]*p[i] for i in range(WEIGHT_COUNT)]) # Detching unnecessary sqrt
        print("%17.14f\t%d" % (d if d > 0 else -d, int(c)))


def reducer():
    ds = []
    for line in sys.stdin:
        d, c = line.rstrip().split('\t')
        ds.append((float(d), int(c)))
    heapq.heapify(ds)
    knns = heapq.nsmallest(int(os.environ["K"]),  ds)
    votes = [0,0]
    for (d,c) in knns: votes[c] += 1
    print(f'{0 if votes[0] > votes[1] else 1}')

if __name__ == '__main__':
    funct = sys.argv[1]
    if funct == 'map':
        x = [float(xi) for xi in sys.argv[2].strip().split(',')]
        mapper(x)
        exit(0)
    elif funct == 'reduce':
        reducer()
        exit(0)
    else:
        print("Unsupported function")
        exit(1)