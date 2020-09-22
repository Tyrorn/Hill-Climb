import numpy as np

import math
import time
import copy


def func(x):
    ret = (x[0]**2) + (2*(x[1]**2)) - (0.3*math.cos(3*math.pi*x[0])) - (0.4*math.cos(4*math.pi*x[1]))+0.7
    return ret


def grad(x1, x2):
    grad = np.zeros(2,)
    grad[0] = 2*x1+0.9*math.pi * math.sin(3*math.pi * x1)
    grad[1] = 4*x2+1.6*math.pi * math.sin(4*math.pi * x2)
    return grad

def random_start():
    numbers = []
    for i in range(10):
        numbers.append(np.random.uniform(-100, 100, 2))
    return numbers
list = []
list_x1 =[]
list_x2 = []
start = time.time()
#Alpha = learning rate
alphas = 0.01
difference = 0.000001
max_iterations = 10000
attempts = 0
numbers = random_start()
# Gradient descent begins

while attempts < 10:
    x = numbers[attempts]
    count = 0
    while True:
        count += 1
        new_x = x-alphas*grad(x[0], x[1])
        if (abs(x[0] - new_x[0]) < difference) & (abs(x[1] - new_x[1]) < difference):
            break
        if abs(x[0] - new_x[0]) > difference:
            x[0] = new_x[0]

        if abs(x[1] - new_x[1]) > difference:
            x[1] = new_x[1]
        if count > max_iterations:
            break
    attempts += 1
    list.append(x)
    list_x1.append(x[0])
    list_x2.append(x[1])
end = time.time()
print("Time taken:", (start-end))
print("mean of X1:", np.mean(list_x1))
print("mean of X2:", np.mean(list_x2))
print("std of X1: ", np.std(list_x1))
print("std of X2: ", np.std(list_x2))

#gradient descent ends

#Hill climbing begins

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

start = time.time()
max_iterations = 1000000
# rate of change
alpha = 0.01
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
# Gradient descent ends

#Hill Climb Begins
