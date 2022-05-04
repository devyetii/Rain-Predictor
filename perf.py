import math
import sys
from constants import WEIGHT_COUNT

model = []
with open('model.txt') as f:
    model =  [ float(wi) for wi in f.readlines() ]

print(model)


total = 0
diff = 0
with open('test.csv') as f:
    for l in f.readlines():
        total += 1
        datapoint = [ float(p) for p in l.strip().split(',') ]
        x = datapoint[:-1]
        x.insert(0, 1)
        y = datapoint[-1]
        dot = sum( [float(x[i]) * float(model[i]) for i in range(WEIGHT_COUNT) ] )
        pb = 1.0 / (1.0 + math.exp(-dot)) if -100.0 < dot else sys.float_info.min
        y_h = pb > 0.5
        print(diff)
        diff +=  1 if (y != y_h) else 0

print(((total - diff) / total) * 100)