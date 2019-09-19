# -*- coding: utf-8 -*-

# import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import tkinter

# Create lists to read in environment data
environment = []


# Open in.txt in reader
# Read environment data into lists
# Close file
f = open('in.txt', newline='')

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
    
f.close()



# Assign number of agents variable to 10
# Assign neighbourhood to 20
num_of_agents = 10
neighbourhood = 20

# Create empty agents list to add co-ordinates to
agents=[]

# Create 10 random sets of agent co-ordinates 
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

# Set carry_on to true
carry_on = True	



    
# Run update function to update the graph
def update(frame_number):
    
    # Check to see if carry_on condition is true
    global carry_on
    
    # Clear the previous frame
    fig.clear ()
    
    # Set graph area
    matplotlib.pyplot.ylim(299,0)
    matplotlib.pyplot.xlim(0, 299)

    # Add environment to graph
    matplotlib.pyplot.imshow(environment)
   
    # Run move, eat and share_with_neighbours for each agent
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    
    # Stopping condition when all sheep have eaten 150 environment
    # Set count of full sheep to 0
    count_full = 0
    # Add 1 to count each time a sheep has eaten 150 and is full
    for i in range(num_of_agents):
        if agents[i].store >= 150:
            count_full += 1         
    # When all sheep are full, run the stopping motion 
    if count_full == num_of_agents:
        carry_on = False
        print("The sheep are full!")
        
        # Calculate how much the sheep have eaten in total
        grass_eaten = []
        for agent in agents:
            grass_eaten.insert(0, agent.store)
        print('The sheep have eaten: ' + (str(int(sum(grass_eaten)))))
            
    
    # Plot the agent co-ordinates
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)

# Continue to new frame if carry_on is true
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (carry_on) :
        yield a
        a = a + 1

# Add animation
# animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

# Add GUI
# Crete function 'run' to begin update loop
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

# Create figure
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Create menu and command to run 'run' function
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)   

tkinter.mainloop()

    





























