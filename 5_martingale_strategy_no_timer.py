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
       
def doubler_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    wagerX = []
    valueY = []
    
    currentWager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager
    
    while currentWager <= wager_count:
        if previousWager == "win":
            print("won the last wager, great")
            if rollDice():
                value += wager
                print(value)
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                value -= wager
                previousWager = "loss"
                print(value)
                previousWagerAmount = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value < 0:
                    print("went broke after".currentWager,"bets")
                    break
                    
        elif previousWager == "loss":
            print("we lost last, so will now double the next")
            if rollDice():
                wager = previousWagerAmount * 2
                print("we won",wager)
                value += wager
                print(value)
                wager = initial_wager
                previousWager == "Win"
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                wager = previousWagerAmount * 2
                print("we lost",wager)
                value -= wager
                if value <= 0:
                    print("we went broke after",currentWager,"bets")
                    break
                
                print(value)
                previousWager = "loss"
                
                previousWagerAmount = wager
                wagerX.append(currentWager)
                valueY.append(value)
            
        currentWager += 1

    print(value)
    plt.plot(wagerX, valueY)
    
    
    
doubler_bettor(10000,100,100)
plt.show()

                
            
#simple_bettor(10000,100,100)