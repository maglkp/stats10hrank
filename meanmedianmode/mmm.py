import sys
import re
import math
from collections import defaultdict

inputs = []
for line in sys.stdin:
    inputs.append(re.sub('[\n]', '', line))

n = float(inputs[0])
nums = inputs[1].split()
nums = list(map(int, nums))

# mean
avg = .0
for num in nums:
    avg += num / n

# median
nums = sorted(nums)
middle_ix = (n - 1) / 2
first_middle = nums[math.floor(middle_ix)]
second_middle = nums[math.ceil(middle_ix)]
median = (first_middle + second_middle) / 2

# mode
nums_dict = defaultdict(int)
for num in nums:
    nums_dict[num] += 1

mode_item = list(nums_dict.items())[0]
for item in nums_dict.items():
    if item[1] > mode_item[1] or (item[1] == mode_item[1] and item[0] < mode_item[0]):
        mode_item = item

print("%.1f" % avg)
print("%.1f" % median)
print(mode_item[0])
