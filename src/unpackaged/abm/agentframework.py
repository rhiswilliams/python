# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:29:06 2019

@author: gyrsw
"""
import random



class Agent():
    
    # Set random agents
    def __init__ (self, environment, agents):
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)
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
            self.environment[self.y][self.x] -= 10
            self.store += random.randint(1,10)
    
    # Calculate distance
    
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) +
    ((self.y - agent.y)**2))**0.5
    
    # Share with neighbours
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum_stores = self.store + agent.store
                ave = sum_stores/2
                self.store = ave
                agent.store = ave
                # print("sharing " + str(dist) + " " + str(ave))
                









