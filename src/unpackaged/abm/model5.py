# -*- coding: utf-8 -*-

# import random
# import operator
import matplotlib.pyplot
import agentframework


# Define distance_between coordinates
def distance_between(agents_row_a, agents_row_b):
    return(((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5
           

# Assign number of agents variable to 10
num_of_agents = 10
num_of_iterations = 100

# Create empty list to add co-ordinates to
agents=[]

"""      
# Test agentframework by creating single agent 
a = agentframework.Agent()
print(a.y, a.x)
a.move()
print(a.y, a.x)
"""


# Create 10 random sets of co-ordinates 
for i in range(num_of_agents):
    agents.append(agentframework.Agent())



# Random walk co-ordinates 100 steps
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()



# Work out the distance between co-ordinates
# Loop through all co-ordinate combinations

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        # print("The distance is " + str(distance))




# Create x and y axis, 0 to 100
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# Plot all co-ordinates
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

# Show graph
matplotlib.pyplot.show()





























