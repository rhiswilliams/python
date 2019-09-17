# -*- coding: utf-8 -*-

import random
# import operator
import matplotlib.pyplot




# Assign number of agents variable to 10
num_of_agents = 10
num_of_iterations = 100

# Create empty list to add co-ordinates to
agents=[]

# Create 10 random sets of co-ordinates 
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])




# Algorithm
# import random
# if random_number < 0.5:
#     step y and x 1 larger
# else:
#     step y and x 1 smaller
# loop algorithm 100 times

# Random walk y co-ordinate 100 steps
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] + 1) % 100

# Random walk x co-ordinate 100 steps
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] + 1) % 100
        

# Print agents list
print("The co-ordinates are " + str(agents))

# Print furthest east co-ordinate - largest x value
# largest_x = (max(agents, key=operator.itemgetter(1)))
# print("The co-ordinate furthest east is " + str(largest_x))




# Create x and y axis, 0 to 100
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)

# Plot all co-ordinates
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

# Colour the agent furthest east red
# matplotlib.pyplot.scatter(largest_x[1],largest_x[0], color='red')

# Show graph
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




























