# -*- coding: utf-8 -*-

import random
# import operator
import matplotlib.pyplot
# import time

# Test time - start
# start = time.clock()

# Define distance_between coordinates
def distance_between(agents_row_a, agents_row_b):
    return(((agents_row_a[0]-agents_row_b[0])**2) + ((agents_row_a[1]-agents_row_b[1])**2))**0.5



# Assign number of agents variable to 10
num_of_agents = 10
num_of_iterations = 100

# Create empty list to add co-ordinates to
agents=[]

# Create 10 random sets of co-ordinates 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])




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
            agents[i][0] = (agents[i][0] - 1) % 100

# Random walk x co-ordinate 100 steps
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
        

# Print agents list
print("The co-ordinates are " + str(agents))





# Work out the distance between co-ordinates
# Loop through all co-ordinate combinations

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        # print("The distance is " + str(distance))



# Print furthest east co-ordinate - largest x value
# largest_x = (max(agents, key=operator.itemgetter(1)))
# print("The co-ordinate furthest east is " + str(largest_x))



# Create x and y axis, 0 to 100
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# Plot all co-ordinates
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])

# Colour the agent furthest east red
# matplotlib.pyplot.scatter(largest_x[1],largest_x[0], color='red')

# Show graph
matplotlib.pyplot.show()

"""
#Test time - end and print
end = time.clock()
print("time = " + str(end - start))"""





























