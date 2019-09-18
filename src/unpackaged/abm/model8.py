# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 


# Create lists to read in data
environment = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Open in.txt in reader
# Read data into lists
# Close file
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
    
f.close()

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()


# Assign number of agents variable to 10
num_of_agents = 10
# num_of_iterations = 100
neighbourhood = 20

# Create empty list to add co-ordinates to
agents=[]

# Create 10 random sets of co-ordinates 
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

carry_on = True	

def update(frame_number):
    global carry_on
    
    fig.clear ()
    
    matplotlib.pyplot.ylim(299,0)
    matplotlib.pyplot.xlim(0, 299)

    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    # Stopping condition when 100 environment is eaten
    if agents[i].store >= 150:
        carry_on = False
        print("The sheep are full!")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        # print (agents[i].x, agents[i].y)

    matplotlib.pyplot.show()
        

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (carry_on) :
        yield a
        a = a + 1

# Create x and y axis, 0 to 100
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

# Plot all co-ordinates
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

# Add environment to graph
matplotlib.pyplot.imshow(environment)

# Add animation
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

# Show graph
matplotlib.pyplot.show()





























