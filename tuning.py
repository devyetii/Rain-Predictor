import subprocess
import os
from constants import WEIGHT_COUNT

from perf import perf


eta_range = [0.01 + 0.01*i for i in range(100)]
mu_range = [0.0001 + 0.0001 * i for i in range(100)]
print('Running ....')
os.environ['T'] = '1000'

maxperf = 0
chosen_eta = 0.01
chosen_mu = 0.001

for eta in eta_range:
    os.environ['ETA'] = f'{eta}'
    for mu in mu_range:
        with open('model.txt', 'w') as f:
            f.writelines(["1.00000\n" for _ in range(WEIGHT_COUNT)])
        os.environ['MU'] = f'{mu}'
        subprocess.run(['./logreg.sh', 'train'], env=os.environ,
                       stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        subprocess.run(['./logreg.sh', 'import'], env=os.environ,
                       stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        curperf = perf('validate.csv')
        print(f'curperf={curperf}, eta={eta}, mu={mu}')
        if curperf > maxperf:
            maxperf = curperf
            chosen_eta = eta
            chosen_mu = mu
print('Done!')
print(f'maxperf={maxperf}, eta={chosen_eta}, mu={chosen_mu}')
