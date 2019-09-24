# -*- coding: utf-8 -*-

import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import agentframework_web
import csv
import matplotlib.animation
import tkinter
import requests
import bs4

# Get data from web page
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

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
num_of_plants = 10
plant_radius = 2


# Create empty agents list to add co-ordinates to
agents=[]
plants=[]

# Get 10 sets of agent co-ordinates from data
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework_web.Agent(environment, agents, x, y))
    # print(x,y)

# Get 10 random sets of plant co-ordinates
for j in range(num_of_plants):
    plants.append([random.randint(0,99),random.randint(0,99)])

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
   
    
    # Run move, eat, share_with_neighbours, and close_to_plant for each agent
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        agents[i].close_to_plant(plants, plant_radius)


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
        print("All the sheep are full!")
        
        # If sheep have eaten 165 or more they are overfull
        # Find and return number of overfull sheep
        overfull_sheep = []
        for i in range(num_of_agents):
            if agents[i].store >= 165:
                overfull_sheep.insert(0, agents[i])
        if len(overfull_sheep) == 1:
            print ("Only 1 sheep is too full and needs a nap.")
        elif len(overfull_sheep) > 1:
            print (str(len(overfull_sheep)) + " are too full and need a nap.")
        else:
            print("No sheep are too full.")
        
        # Show how much each sheep has eaten
        # Tests overfull_sheep and grass_eaten
        #for i in range(num_of_agents):
            #print(agents[i].store)
        
            
        # Calculate how much the sheep have eaten in total
        grass_eaten = []
        for agent in agents:
            grass_eaten.insert(0, agent.store)
        print('The sheep have eaten: ' + (str(int(sum(grass_eaten)))))
          
    
    # Plot the agent co-ordinates
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color='white')
    # Plot the plant co-ordinates in black
    for j in range(num_of_plants):
        matplotlib.pyplot.scatter(plants[j][1], plants[j][0], color='black')

# Continue to new frame if carry_on is true
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (carry_on) :
        yield a
        a = a + 1

# Add GUI
# Crete function 'run' to begin update loop
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

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

    





























