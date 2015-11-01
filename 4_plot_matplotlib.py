# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:59:42 2015

@author: chr7stos
"""

import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)
    
    if roll == 100:
        #print(roll, "Lose")
        return False
    elif roll <= 50:
        #print(roll, "Lose")
        return False
    else:
        #print(roll, "Win")
        return True
        
def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    wagerX = []
    valueY = []
    
    current_wager = 1 #this way it ends at 100 and not 99
    
    while current_wager <= wager_count:
        if rollDice():
            value += wager
            wagerX.append(current_wager)
            valueY.append(value)
        else:
            value -= wager
            wagerX.append(current_wager)
            valueY.append(value)
        current_wager += 1
        
    if value < 0:
        value = "broke"
        
    #print("Funds:", value) #shifting this, prints funds at the very end only

    plt.plot(wagerX,valueY)

#make a simple counter here

x = 0
while x < 1000:
    simple_bettor(10000,100,100000)
    x += 1
    
plt.ylabel("Account value")
plt.xlabel("Wager count")
plt.show()
                
            
