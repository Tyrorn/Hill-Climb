from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib.pyplot as plt
import math
import time
import copy
def func(x1,x2):
    ret = (x1**2) + (2*(x2**2)) - (0.3*math.cos(3*math.pi*x1)) - (0.4*math.cos(4*math.pi*x2))+0.7
    return ret

def grade(x, alpha):
    temp = copy.deepcopy(x)
    temp_up = copy.deepcopy(x)
    temp_down = copy.deepcopy(x)
    temp_up[0] = temp_up[0] + alpha
    x1_score = func(temp_up[0], temp[1])
    temp_down[0] = temp_down[0] - alpha
    x2_score = func(temp_down[0], temp[1])
    if x1_score < x2_score:
        temp[0] = temp_up[0]
    else:
        temp[0] = temp_down[0]
    temp_up[1] = temp_up[1] + alpha
    x1_score = func(temp[0], temp_up[1])
    temp_down[1] = temp_down[1] - alpha
    x2_score = func(temp[0], temp_down[1])
    if x1_score < x2_score:
        temp[1] = temp_up[1]
    else:
        temp[1] = temp_down[1]
    return temp

def random_start():
    numbers = []
    for i in range(10):
        numbers.append(np.random.uniform(-100, 100, 2))
    return numbers


numbers = random_start()
start = time.time()
max_iterations = 1000000
# rate of change
alpha = 1.15
attempts = 0
hc_list = []
hc_list_x1 = []
hc_list_x2 = []
# direction = initial(x, best_score)
while attempts < 10:
    best_x = numbers[attempts]
    count = 0
    while count < max_iterations:
        temp = copy.deepcopy(best_x)
        temp = grade(temp, alpha)
        if func(temp[0], temp[1]) < func(best_x[0], best_x[1]):
            best_x = temp
        else:
            break
        count += 1
    attempts += 1
    hc_list.append(best_x)
    hc_list_x1.append(best_x[0])
    hc_list_x2.append(best_x[1])
end = time.time()
print("Hill Climbing results")
print("time taken: ", (end - start))
print("mean of X1:", np.mean(hc_list_x1))
print("mean of X2:", np.mean(hc_list_x2))
print("std of X1: ", np.std(hc_list_x1))
print("std of X2: ", np.std(hc_list_x2))
