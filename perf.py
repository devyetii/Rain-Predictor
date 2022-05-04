import math
import sys
from constants import WEIGHT_COUNT

def perf(fname: str):
    model = []
    with open('model.txt') as f:
        model =  [ float(wi) for wi in f.readlines() ]
    total = 0
    diff = 0
    with open(fname) as f:
        for l in f.readlines():
            total += 1
            datapoint = [ float(p) for p in l.strip().split(',') ]
            x = datapoint[:-1]
            x.insert(0, 1)
            y = datapoint[-1]
            dot = sum( [float(x[i]) * float(model[i]) for i in range(WEIGHT_COUNT) ] )
            pb = 1.0 / (1.0 + math.exp(-dot)) if -100.0 < dot else sys.float_info.min
            y_h = pb > 0.5
            diff +=  1 if (y != y_h) else 0

    return ((total - diff) / total) * 100

if __name__ == '__main__':
    print(perf(sys.argv[1]))