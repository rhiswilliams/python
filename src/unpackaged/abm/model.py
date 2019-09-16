# -*- coding: utf-8 -*-

import random

# Assign variables - random number from 0 to 99
y0 = random.randint(0,99)
x0 = random.randint(0,99)

# Test variables
# print(y0)
# print(x0)

# Algorithm
# import random
# if random_number < 0.5:
#     y0 = y0 + 1
# else:
#     y0 = y0 - 1

# Test random number
# print ("The random number is " + str(random.random()))

# Random walk one step
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
print ("x0 is " + str(x0), ", y0 is " + str(y0))

# Assign variables - random number from 0 to 99
y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Random walk one step
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
print ("x1 is " + str(x1), ", y1 is " + str(y1))





# Working out the distance between sets of co-ordinates
# Find difference between x0 and x1
# Square the x difference
# Find difference between y0 and y1
# Square the y difference
# Add the x difference square and the y difference square
# Square root the result


x_dist = x0 - x1
x_dist_sq = (x_dist)**2

y_dist = y0 - y1
y_dist_sq = (y_dist)**2

radicand = (x_dist_sq) + (y_dist_sq)

overall_distance = (radicand)**0.5
print ("The distance between the coordinates is " + str(overall_distance))




























