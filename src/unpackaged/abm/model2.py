# -*- coding: utf-8 -*-

import random
import operator
import matplotlib.pyplot

# Create empty list to add co-ordinates to
agents=[]

# Create x0 and y0
# Add random x co-ordinate and y co-ordinate to list from 0 to 99

agents.append([random.randint(0,99),random.randint(0,99)])

# Algorithm
# import random
# if random_number < 0.5:
#     y0 = y0 + 1
# else:
#     y0 = y0 - 1

# Random walk one step
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
print ("y0 is " + str(agents[0][0]), ", x0 is " + str(agents[0][1]))


# Create x1 and y1
# Add random x co-ordinate and y co-ordinate to list from 0 to 99

agents.append([random.randint(0,99),random.randint(0,99)])

# Random walk one step
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
        
print ("y1 is " + str(agents[0][0]), ", x1 is " + str(agents[0][1]))

# Print agents list
print("The co-ordinates are " + str(agents))

# Print furthest east co-ordinate - largest x value
largest_x = (max(agents, key=operator.itemgetter(1)))
print("The co-ordinate furthest east is " + str(largest_x))

# Plot co-ordinates
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

# Colour the agent furthest east red
matplotlib.pyplot.scatter(largest_x[1],largest_x[0], color='red')
matplotlib.pyplot.show()

# Working out the distance between sets of co-ordinates
# Find difference between x0 and x1
# Square the x difference
# Find difference between y0 and y1
# Square the y difference
# Add the x difference square and the y difference square
# Square root the result


"""x_dist = x0 - x1
x_dist_sq = (x_dist)**2

y_dist = y0 - y1
y_dist_sq = (y_dist)**2

radicand = (x_dist_sq) + (y_dist_sq)

overall_distance = (radicand)**0.5
print ("The distance between the coordinates is " + str(overall_distance))"""




























