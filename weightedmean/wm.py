import sys
import re
import math
from collections import defaultdict

inputs = []
for line in sys.stdin:
    inputs.append(re.sub('[\n]', '', line))

# n, x-s and weights
n = float(inputs[0])
x = inputs[1].split()
x = list(map(int, x))
w = inputs[2].split()
w = list(map(int, w))
