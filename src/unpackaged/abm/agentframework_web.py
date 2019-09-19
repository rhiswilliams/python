# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:29:06 2019

@author: gyrsw
"""
import random


class Agent():
    
    # Set agents from data
    # If a data point is none, set random integer
    def __init__ (self, environment, agents, x=None, y=None):
        if (x == None):
            self.x = random.randint(0,299)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,299)
        else:
            self.y = y
        self.environment=environment
        self.store = 0
        self.agents=agents
            
        pass


    # Random walk by 1 step
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
                    
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300


    # Eat between 1 and 10 units
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            grass_amount = random.randint(1,10)
            self.environment[self.y][self.x] -= (grass_amount)
            self.store += (grass_amount)
            
    def sick(self):
        if self.store > 120:
            self.store = 0
            print('A sheep was sick!')
    
    # Calculate distance between agents
    
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) +
    ((self.y - agent.y)**2))**0.5

  

    
    # Define share with neighbours
    # Agents share if the distance between them is less than neighbourhood
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum_stores = self.store + agent.store
                ave = sum_stores/2
                self.store = ave
                agent.store = ave


                









