import math
import sys
from constants import WEIGHT_COUNT

x = [ float(xi) for xi in sys.argv[1][1:-1].split(',') ]
print(x)
model = []
with open('model.txt') as f:
    model = [float(wi) for wi in f.readlines() ]

dot = sum([model[i] * x[i] for i in range(WEIGHT_COUNT)])

p = 1.0 / (1.0 + math.exp(dot)) if dot < 100.0 else sys.float_info.min

print(p > 0.5)