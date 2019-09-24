# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:29:06 2019

@author: gyrsw
"""
import random


class Agent():
    
    # If a co-ordinate is none, set random integer
    # Set store to 0
    def __init__ (self, environment, agents, x=None, y=None):
        if (x == None):
            self.x = random.randint(0,99)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,99)
        else:
            self.y = y
        self.environment=environment
        self.store = 0
        self.agents=agents
            
        pass


    # Random walk by 1 step
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
                    
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    """
    Move the x and y co-ordinates one higher or lower depending on a random number.
    
    Positional arguments:
    Self -- tuple of two integers
    
    Returns:
    New x and y value for self
    
    To run the doctest run “python -m doctest -v docs.py”
    
    >>> a=move()
    >>> random.random() == 0.1
    >>> a.sum(1,1)
    (2,2)
    
    
    """
    
    # Eat between 1 and 10 units
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            grass_amount = random.randint(1,10)
            self.environment[self.y][self.x] -= (grass_amount)
            self.store += (grass_amount)
    
    """
    If the environment is more than 10, remove a random amount from 1 to 10 and add to store.
    
    Positional arguments:
    Self -- tuple of two integers
    
    Returns:
    New values for environment and store.
    
    To run the doctest run “python -m doctest -v docs.py”
    
    >>> environment == 11
    >>> store == 5
    >>> random.randint(1,10) == 1
    >>> a = eat()
    >>> a.sum((1,1))
    >>> print([1][1].environment)
    10
    >>> print([1][1].store)
    6
    
    """
    
    # Calculate distance between agents
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) +
    ((self.y - agent.y)**2))**0.5

    """
    Calculate and return distance between two co-ordinates.
    
    Positional arguments:
    Self -- tuple of two integers
    Agent -- tuple of two integers
    
    Returns:
    Distance between co-ordinates.
    
    To run the doctest run “python -m doctest -v docs.py”
    
    >>> a=distance_between()
    >>> a.add((1,1)(2,2))
    1.414214
    
    """
  
    # Calculate distance between plants and agents
    # If distance < plant_radius, sheep is sick and store decreases by random 15:30
    def close_to_plant(self, plants, plant_radius):
        for plant in plants:
            dist = (((self.x - plant[0])**2) + ((self.y - plant[1])**2))**0.5
            if dist <= plant_radius:
                self.store -= random.randint(15,30)
                print('A sheep has eaten a poisonous plant! The sheep was sick.')
    
    """
    Calculate the distance between plants and agents and reduce store by a 
    random number between 15 and 30 if the distance is less than plant_radius.
    
    Positional arguments:
    Self -- tuple of two integers
    Plants -- tuple of two integers
    Plant_radius -- an integer
    
    Return: Reduction in store and print: 'A sheep has eaten a poisonous plant!
    The sheep was sick.'
    
    To run the doctest run “python -m doctest -v docs.py”

    >>> self.store = 15
    >>> random.randint(15,30) == 15
    >>> a=close_to_plant()
    >>> a.add((1,1)(2,2),2)
    'A sheep has eaten a poisonous plant! The sheep was sick.'
    >>> print([1][1].store)
    0
    
    """
    
    # Define share with neighbours
    # Agents share if the distance between them is less than neighbourhood
    # When agents share, their stores are set to the average of the sum of their stores
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum_stores = self.store + agent.store
                ave = sum_stores/2
                self.store = ave
                agent.store = ave

    """
    Calculate the distance between two agents. If the distance is less than neighbourhood,
    sum the agents stores and assign each agent's store the average of the sum.
    
    Positional arguments:
    Self -- tuple of two integers
    Neighbourhood -- an integer
    
    Return:
    Average store amount.
    
    To run the doctest run “python -m doctest -v docs.py”
    
    >>> self.store == 10
    >>> agent.store == 12
    >>> agent == (2,2)
    >>> a=share_with_neighbours()
    >>> a.sum((1,1), 2)
    >>> print([1][1].store)
    11
    >>> print(agent.store)
    11
    
    
    """

                









