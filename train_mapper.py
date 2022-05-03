#!/usr/bin/env python3

import math
import sys
from constants import ETA, WEIGHT_COUNT

model = [1.0 for _ in range(WEIGHT_COUNT)]

try:
    # Read weights
    with open('model.txt') as csv_file:
        # model = np.array(csv_file.readlines(), dtype=np.float64)
        model = [float(line) for line in csv_file.readlines()]
except:
    pass
    # logger.error("FUCK")
 
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    datapoint = [float(xx) for xx in line.strip().split(',')]

    # Split into x and y
    x = datapoint[:-1]
    x.insert(0, 1)
    y = datapoint[-1]

    # Logistic regression equations
    y_h = sum([ float(x[i]*model[i]) for i in range(WEIGHT_COUNT)])
    p = 1.0 / (1.0 + math.exp(-y_h)) if -100.0 < y_h else sys.float_info.min
    model = [model[i] + ETA * (y - p) * x[i] for i in range(WEIGHT_COUNT)]

# Output the final model to stdout
for j in range(len(model)):
    print(f'{j}\t{model[j]}')
