# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:59:42 2015

@author: chr7stos
"""

import random

def rollDice():
    roll = random.randint(1,100)
    
    if roll == 100:
        print(roll, "Lose")
        return False
    elif roll <= 50:
        print(roll, "Lose")
        return False
    else:
        print(roll, "Win")
        return True
        
def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    current_wager = 0
    
    while current_wager < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager
        current_wager += 1
        print("Funds:", value)

            
#simple_bettor(10000,100,100)