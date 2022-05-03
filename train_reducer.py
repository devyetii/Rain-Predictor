#!/usr/bin/env python3
"""reducer.py"""

import sys
from constants import WEIGHT_COUNT


# What the reducer does is that it averages the model output of all mappers into an aggregated model
# model = np.zeros(WEIGHT_COUNT, dtype=np.float64)
model = [float(0.0) for _ in range(WEIGHT_COUNT)]
k = 0
for line in sys.stdin:
    arr = line.rstrip().split('\t', 1)
    j = int(arr[0])
    w = float(arr[1])
    if j == 0: k += 1
    model[j] += w

print(k)
[print(model[i] / k) for i in range(WEIGHT_COUNT)]