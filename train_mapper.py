#!/usr/bin/env python3

import math
import os
import sys

from constants import MODEL_FILE, WEIGHT_COUNT, T

ETA = float(os.environ["ETA"])
MU = float(os.environ["MU"])
mu_2 = MU * 2

model = [1.0 for _ in range(WEIGHT_COUNT)]

try:
    # Read weights
    with open(MODEL_FILE) as f:
        # model = np.array(csv_file.readlines(), dtype=np.float64)
        model = [float(line) for line in f.readlines()]
except:
    pass

# input comes from STDIN (standard input)
for t in range(1, T+1):
    for line in sys.stdin:
        # remove leading and trailing whitespace
        datapoint = [float(xx) for xx in line.strip().split(',')]

        # Split into x and y
        x = datapoint[:-1]
        x.insert(0, 1)
        y = datapoint[-1]

        # Logistic regression equations
        lrate = ETA / float(t*t)
        y_h = sum([float(x[i]*model[i]) for i in range(WEIGHT_COUNT)])
        p = 1.0 / (1.0 + math.exp(-y_h)) if - \
            100.0 < y_h else sys.float_info.min
        model = [(model[i] * (1.0 - mu_2 * lrate)) + (lrate * (y - p) * x[i])
                 for i in range(WEIGHT_COUNT)]

# Output the final model to stdout
for j in range(len(model)):
    print(f'{j}\t{model[j]}')
